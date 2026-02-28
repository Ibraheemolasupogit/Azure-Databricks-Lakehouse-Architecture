
## Databricks Lakehouse Workflows – Overview

This repository groups curated, production-style workflows demonstrating key architectural patterns in Azure Databricks.

Detailed Microsoft Learn lab walkthroughs are preserved in `labs_msl/`.  
Curated, runnable implementations are located in `src/`.

---

## 1. Data Lakehouse & Engineering

Implements a medallion (Bronze → Silver → Gold) architecture using Delta Lake and Delta Live Tables.

- Apache Spark transformations  
- Delta Live Tables pipelines  
- Schema enforcement and expectations  
- Performance optimisation patterns  

Implementation:  
`src/lakehouse/01_batch_medallion_pipeline.py`

### Pipeline Visualisation

![Delta Live Tables medallion pipeline](../evidence/lakehouse/dlt-medallion-pipeline.png)

---

## 2. Real-Time Analytics & Streaming

Implements streaming ingestion and transformation pipelines.

- Spark Structured Streaming  
- Auto Loader with schema evolution  
- Delta Live Tables for streaming pipelines  
- Production-style orchestration patterns  

Implementation:  
`src/streaming/01_dlt_iot_streaming_pipeline.py`

### Streaming Ingestion – Auto Loader

![Auto Loader schema evolution](../evidence/streaming/autoloader-schema-evolution.png)

---

## 3. Machine Learning & MLOps

Demonstrates end-to-end model lifecycle management using MLflow.

- Model training with Spark ML  
- Experiment tracking  
- Metric logging  
- Model registration  

Implementation:  
`src/ml-mlflow/01_mlflow_classification_pipeline.py`

### MLflow Experiment Tracking

![MLflow experiment tracking](../evidence/ml-mlflow/mlflow-experiment-tracking.png)

---

## 4. Generative AI & LLMOps

Implements Retrieval Augmented Generation (RAG) workflows governed by Unity Catalog.

- Vector Search indexing  
- Catalog-level governance  
- AI workload integration  
- Responsible AI considerations  

Implementation:  
`src/llm/01_rag_demo_unity_catalog.py`

### RAG Workflow & Governance

![Unity Catalog lineage for RAG tables](../evidence/governance/unity-catalog-lineage.png)

---