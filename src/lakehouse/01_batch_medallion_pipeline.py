# Databricks notebook source
# COMMAND ----------
# MAGIC %md
# MAGIC # Lakehouse Batch Medallion Pipeline
# MAGIC
# MAGIC This notebook demonstrates a **Delta Live Tables medallion pipeline**:
# MAGIC - **Bronze**: ingest raw COVID CSV data
# MAGIC - **Silver**: clean & standardise schema
# MAGIC - **Gold**: aggregated daily metrics for analytics
# MAGIC
# MAGIC Inspired by the Microsoft Learn lab *"Create a data pipeline with Delta Live tables"*.

# COMMAND ----------
# DBFS location for raw CSV created by a separate ingestion step
raw_csv_path = "dbfs:/delta_lab/covid_data.csv"

# You can tweak these for your environment
pipeline_storage = "dbfs:/pipelines/delta_lab"
target_schema = "default"

print(f"Raw data: {raw_csv_path}")
print(f"Pipeline storage: {pipeline_storage}, target schema: {target_schema}")

# COMMAND ----------
# MAGIC %md
# MAGIC ## 1. Define Delta Live Tables (Bronze / Silver / Gold)
# MAGIC These `CREATE OR REFRESH LIVE TABLE` statements will be used by a
# MAGIC Delta Live Tables pipeline configured to point at this notebook.

# COMMAND ----------
# MAGIC %sql
# MAGIC CREATE OR REFRESH LIVE TABLE raw_covid_data
# MAGIC COMMENT "COVID sample dataset ingested from CSV"
# MAGIC AS
# MAGIC SELECT
# MAGIC   Last_Update,
# MAGIC   Country_Region,
# MAGIC   Confirmed,
# MAGIC   Deaths,
# MAGIC   Recovered
# MAGIC FROM read_files('dbfs:/delta_lab/covid_data.csv', format => 'csv', header => true);

# COMMAND ----------
# MAGIC %sql
# MAGIC CREATE OR REFRESH LIVE TABLE processed_covid_data(
# MAGIC   CONSTRAINT valid_country_region EXPECT (Country_Region IS NOT NULL) ON VIOLATION FAIL UPDATE
# MAGIC )
# MAGIC COMMENT "Cleaned & typed COVID data ready for analytics."
# MAGIC AS
# MAGIC SELECT
# MAGIC   TO_DATE(Last_Update, 'MM/dd/yyyy') AS Report_Date,
# MAGIC   Country_Region,
# MAGIC   Confirmed,
# MAGIC   Deaths,
# MAGIC   Recovered
# MAGIC FROM live.raw_covid_data;

# COMMAND ----------
# MAGIC %sql
# MAGIC CREATE OR REFRESH LIVE TABLE aggregated_covid_data
# MAGIC COMMENT "Gold table – daily totals."
# MAGIC AS
# MAGIC SELECT
# MAGIC   Report_Date,
# MAGIC   SUM(Confirmed) AS Total_Confirmed,
# MAGIC   SUM(Deaths)    AS Total_Deaths,
# MAGIC   SUM(Recovered) AS Total_Recovered
# MAGIC FROM live.processed_covid_data
# MAGIC GROUP BY Report_Date;

# COMMAND ----------
# MAGIC %md
# MAGIC ## 2. Explore the Gold table (for ad-hoc analysis)

# COMMAND ----------
# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM live.aggregated_covid_data
# MAGIC ORDER BY Report_Date;