# Databricks notebook source
# COMMAND ----------
# MAGIC %md
# MAGIC # RAG Demo with Unity Catalog & Mosaic AI Vector Search
# MAGIC
# MAGIC This notebook:
# MAGIC - Loads a small Wikipedia XML snapshot
# MAGIC - Stores cleaned text into a Unity Catalog Delta table
# MAGIC - Creates a **Vector Search** index
# MAGIC - Runs a simple similarity search for RAG-style retrieval
# MAGIC
# MAGIC Inspired by the Microsoft Learn lab *"Retrieval Augmented Generation using Azure Databricks"*.

# COMMAND ----------
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from databricks.vector_search.client import VectorSearchClient

catalog_name = "<your_catalog>"  # TODO: change this to your Unity Catalog
volume_path = f"/Volumes/{catalog_name}/default/rag_lab"
source_xml = f"{volume_path}/enwiki-latest-pages-articles.xml"

print("Volume path:", volume_path)
print("Source XML:", source_xml)

# COMMAND ----------
# MAGIC %md
# MAGIC ## 1. Load raw XML into a Delta table

# COMMAND ----------
spark = SparkSession.builder.appName("RAG-DataPrep").getOrCreate()

raw_df = (
    spark.read.format("xml")
         .option("rowTag", "page")
         .load(source_xml)
)

clean_df = (
    raw_df.select(
        col("title"),
        col("revision.text._VALUE").alias("text")
    ).na.drop()
)

clean_df.write.format("delta").mode("overwrite").saveAsTable(f"{catalog_name}.default.wiki_pages")

# COMMAND ----------
# MAGIC %md
# MAGIC ## 2. Create Vector Search index

# COMMAND ----------
# Enable Change Data Feed for incremental sync
spark.sql(f"""
ALTER TABLE {catalog_name}.default.wiki_pages
SET TBLPROPERTIES (delta.enableChangeDataFeed = true)
""")

vsc = VectorSearchClient()

endpoint_name = "vector_search_endpoint"
index_name = f"{catalog_name}.default.wiki_index"

vsc.create_endpoint(name=endpoint_name, endpoint_type="STANDARD")

index = vsc.create_delta_sync_index(
    endpoint_name=endpoint_name,
    source_table_name=f"{catalog_name}.default.wiki_pages",
    index_name=index_name,
    pipeline_type="TRIGGERED",
    primary_key="title",
    embedding_source_column="text",
    embedding_model_endpoint_name="databricks-gte-large-en",
)

print("Index created:", index_name)

# COMMAND ----------
# MAGIC %md
# MAGIC ## 3. Run a similarity search query

# COMMAND ----------
query = "What is Azure Databricks used for?"
results = vsc.get_index(index_name=index_name).similarity_search(
    query_text=query,
    columns=["title", "text"],
    num_results=3,
)

print("Top matches for query:", query)
for r in results.get("result", {}).get("data_array", []):
    print("----")
    print("Title:", r[0])
    print("Snippet:", r[1][:200], "...")