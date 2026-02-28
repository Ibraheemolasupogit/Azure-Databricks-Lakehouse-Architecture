# Databricks notebook source
# COMMAND ----------
# MAGIC %md
# MAGIC # End-to-End Streaming with Delta Live Tables (IoT)
# MAGIC
# MAGIC This notebook demonstrates:
# MAGIC - Ingesting simulated IoT CSV data as a **Spark Structured Streaming** source
# MAGIC - Writing to a **Delta** sink
# MAGIC - Using **Delta Live Tables** to build a simple medallion-style streaming pipeline
# MAGIC
# MAGIC Inspired by the Microsoft Learn lab *"End-to-End Streaming Pipeline with Delta Live Tables"*.

# COMMAND ----------
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, DoubleType

input_path = "/device_stream/"
delta_sink_path = "/tmp/delta/iot_data"
checkpoint_path = "/tmp/checkpoints/iot_data"

schema = StructType([
    StructField("device_id", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("temperature", DoubleType(), True),
    StructField("humidity", DoubleType(), True),
])

print(f"Input path: {input_path}")
print(f"Delta sink: {delta_sink_path}")

# COMMAND ----------
# MAGIC %md
# MAGIC ## 1. Create a streaming source and write to Delta

# COMMAND ----------
from pyspark.sql.functions import col

iotstream = (
    spark.readStream
         .schema(schema)
         .option("header", "true")
         .csv(input_path)
)

query = (
    iotstream.writeStream
             .format("delta")
             .option("checkpointLocation", checkpoint_path)
             .start(delta_sink_path)
)

print("Streaming from CSV → Delta started. Use query.stop() to stop the stream.")

# COMMAND ----------
# MAGIC %md
# MAGIC ## 2. Delta Live Tables definitions
# MAGIC These functions are used by a Delta Live Tables pipeline
# MAGIC (configure a DLT pipeline to use this notebook as the source).

# COMMAND ----------
import dlt
from pyspark.sql.functions import current_timestamp

@dlt.table(
    name="raw_iot_data",
    comment="Raw IoT device data from Delta sink"
)
def raw_iot_data():
    return spark.readStream.format("delta").load(delta_sink_path)

@dlt.table(
    name="transformed_iot_data",
    comment="Transformed IoT metrics with derived fields"
)
def transformed_iot_data():
    return (
        dlt.read("raw_iot_data")
           .withColumn("temperature_fahrenheit", col("temperature") * 9/5 + 32)
           .withColumn("humidity_percentage", col("humidity") * 100)
           .withColumn("event_time", current_timestamp())
    )

# COMMAND ----------
# MAGIC %md
# MAGIC ## 3. Ad-hoc query of transformed stream (for exploration)

# COMMAND ----------
# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM transformed_iot_data
# MAGIC LIMIT 50;