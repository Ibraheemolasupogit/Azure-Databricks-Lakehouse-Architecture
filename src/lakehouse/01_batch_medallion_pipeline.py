# Databricks notebook source
# COMMAND ----------
# MAGIC %md
# MAGIC # Lakehouse Batch Medallion Pipeline
# MAGIC
# MAGIC **Purpose**
# MAGIC
# MAGIC This notebook demonstrates a batch Lakehouse pipeline in Azure Databricks:
# MAGIC
# MAGIC - Ingest raw data into a **Bronze** Delta table
# MAGIC - Transform and clean into a **Silver** table
# MAGIC - Aggregate into a **Gold** table for analytics
# MAGIC
# MAGIC **Key focus areas**
# MAGIC
# MAGIC - Delta Lake ACID transactions and schema evolution  
# MAGIC - Medallion architecture (Bronze / Silver / Gold)  
# MAGIC - Partitioning and optimisation for downstream BI workloads

# COMMAND ----------
# Bronze ingestion example (replace with your real logic)
from pyspark.sql.functions import *

raw_path = "/mnt/raw/sales"
bronze_path = "/mnt/lakehouse/bronze/sales"

(
    spark.read.format("csv")
         .option("header", True)
         .load(raw_path)
         .withColumn("ingestion_ts", current_timestamp())
         .write.mode("append")
         .format("delta")
         .save(bronze_path)
)

# COMMAND ----------
# Silver transformation placeholder...

# COMMAND ----------
# Gold aggregation placeholder...