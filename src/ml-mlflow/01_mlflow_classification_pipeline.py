# Databricks notebook source
# COMMAND ----------
# MAGIC %md
# MAGIC # ML Classification with MLflow Tracking
# MAGIC
# MAGIC **Purpose**
# MAGIC
# MAGIC This notebook demonstrates:
# MAGIC
# MAGIC - Training a classification model in Azure Databricks
# MAGIC - Tracking experiments and metrics with **MLflow**
# MAGIC - Registering the best model in the MLflow Model Registry
# MAGIC
# MAGIC **Key focus areas**
# MAGIC
# MAGIC - Reproducible ML experiments  
# MAGIC - Metrics and parameter logging  
# MAGIC - Model registration and versioning

# COMMAND ----------
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

# Load your data (replace with penguins / covid / etc.)
data = spark.table("main.sales.products").toPandas()

X = data.drop("label_column", axis=1)  # replace
y = data["label_column"]               # replace

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with mlflow.start_run(run_name="rf-classifier"):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, "model")

    print(f"Accuracy: {acc}")