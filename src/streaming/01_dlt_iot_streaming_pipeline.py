# Databricks notebook source
# COMMAND ----------
# MAGIC %md
# MAGIC # Streaming Ingestion with Delta Live Tables
# MAGIC
# MAGIC **Purpose**
# MAGIC
# MAGIC This notebook demonstrates a streaming pipeline using:
# MAGIC
# MAGIC - **Auto Loader** for incremental ingestion of new files
# MAGIC - **Delta Live Tables (DLT)** for streaming transformations
# MAGIC - Materialised views for curated analytical tables
# MAGIC
# MAGIC **Key focus areas**
# MAGIC
# MAGIC - Structured Streaming with Auto Loader  
# MAGIC - Declarative transformations with DLT  
# MAGIC - Managing streaming vs materialised views

# COMMAND ----------
# Example Auto Loader stream (adapt to your lab code)

from pyspark.sql.functions import *

source_path = "/mnt/landing/iot"
bronze_table = "live.raw_iot_data"

raw_stream_df = (
    spark.readStream
         .format("cloudFiles")
         .option("cloudFiles.format", "json")
         .load(source_path)
)

(
    raw_stream_df
        .withColumn("ingestion_ts", current_timestamp())
        .writeStream
        .option("checkpointLocation", "/mnt/checkpoints/raw_iot_data")
        .option("mergeSchema", "true")
        .table(bronze_table)
)