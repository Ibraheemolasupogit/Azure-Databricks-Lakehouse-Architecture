# Databricks notebook source
# COMMAND ----------
# MAGIC %md
# MAGIC # MLflow Classification Pipeline
# MAGIC
# MAGIC This notebook:
# MAGIC - Trains a simple classifier with Spark ML
# MAGIC - Logs parameters, metrics, and the model with **MLflow**
# MAGIC - Registers the model in the MLflow Model Registry
# MAGIC
# MAGIC Inspired by the Microsoft Learn lab *"Use MLflow in Azure Databricks"*.

# COMMAND ----------
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
import mlflow
import mlflow.spark

# Example: load penguin data Delta table if you've created it already
data = spark.read.table("default.penguins")  # adjust to your table name

feature_cols = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
label_col = "species_index"

assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
data_assembled = assembler.transform(data).select("features", col(label_col).alias("label"))

train_df, test_df = data_assembled.randomSplit([0.8, 0.2], seed=42)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Train & log with MLflow

# COMMAND ----------
with mlflow.start_run(run_name="penguin_logreg"):
    lr = LogisticRegression(maxIter=50, featuresCol="features", labelCol="label")
    model = lr.fit(train_df)

    predictions = model.transform(test_df)
    evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)

    mlflow.log_param("maxIter", 50)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.spark.log_model(model, "model")

    print(f"Test accuracy: {accuracy:.4f}")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Register best model in MLflow Model Registry

# COMMAND ----------
run_id = mlflow.active_run().info.run_id if mlflow.active_run() else None
print("Last run id:", run_id)

# In practice, you'd pick the best run from an experiment.
if run_id:
    model_uri = f"runs:/{run_id}/model"
    registered_model = mlflow.register_model(model_uri, "penguin-classifier")
    print("Registered model version:", registered_model.version)