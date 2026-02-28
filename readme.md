# Enterprise Lakehouse & ML Platform Architecture on Azure Databricks

This repository demonstrates the design and implementation of a production-oriented Lakehouse and Machine Learning platform built on Azure Databricks.

The implementation covers:

- Delta Lakehouse architecture (Bronze/Silver/Gold)
- Auto Loader streaming ingestion with schema evolution
- Delta Live Tables (DLT) pipeline orchestration
- Unity Catalog governance and access controls
- Job orchestration and scheduling
- SQL analytics layer for consumption
- MLflow experiment tracking and model lifecycle management
- CI/CD integration via GitHub Actions

The repository is structured to reflect architectural domains.


---

## Architecture Overview

The platform follows a layered Lakehouse architecture:

### 1. Ingestion Layer
- Auto Loader streaming ingestion
- Schema evolution handling
- Delta write operations

📂 Evidence:
- evidence/lakehouse/autoloader-new-columns.png

---

### 2. Transformation & Lakehouse Modelling
- Delta Live Tables (DLT)
- Medallion architecture (Bronze → Silver → Gold)

📂 Evidence:
- evidence/lakehouse/delta-live-table-pipeline.png

---

### 3. Governance & Security
- Unity Catalog schema management
- Fine-grained table permissions
- Managed Identity integration

📂 Evidence:
- evidence/governance/unity-catalog-lineage.png
- evidence/governance/grant-permissions.png
- evidence/governance/managed-identity.png

---

### 4. Orchestration & Automation
- Scheduled Databricks jobs
- Workflow orchestration

📂 Evidence:
- evidence/workflows/job-orchestration-schedule.png

---

### 5. Analytics & Consumption
- SQL warehouse queries on curated datasets

📂 Evidence:
- evidence/sql/query-results.png

---

### 6. DevOps & CI/CD
- GitHub Actions pipeline integration
- Automated validation workflows

📂 Evidence:
- evidence/cicd/github-actions.png



---

## 📚 Reference


> [All Workflows](https://microsoftlearning.github.io/mslearn-databricks/) <br>
> [Implement a data lakehouse analytics solution with Azure Databricks](https://learn.microsoft.com/en-us/training/paths/data-engineer-azure-databricks/) <br>
> [Implement a machine learning solution with Azure Databricks](https://learn.microsoft.com/en-us/training/paths/build-operate-machine-learning-solutions-azure-databricks/) <br>
> [Implement a data engineering solution with Azure Databricks](https://learn.microsoft.com/en-us/training/paths/azure-databricks-data-engineer/) <br>
> [Implement Generative AI engineering with Azure Databricks](https://learn.microsoft.com/en-us/training/paths/implement-generative-ai-engineering-azure-databricks/)

---
