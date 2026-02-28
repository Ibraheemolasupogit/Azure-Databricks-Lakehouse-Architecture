# Enterprise Lakehouse & ML Platform Architecture on Azure Databricks

This repository implements a governed Azure Databricks Lakehouse and Machine Learning platform designed for enterprise workloads.

It demonstrates:
- Delta Lakehouse architecture (Bronze / Silver / Gold)
- Auto Loader streaming ingestion with schema evolution
- Delta Live Tables (DLT) pipeline orchestration
- Unity Catalog governance and access controls
- Job orchestration and scheduling
- SQL analytics for downstream consumption
- MLflow experiment tracking and model lifecycle management
- CI/CD integration via GitHub Actions

The repository is structured around key architectural domains rather than individual labs.

---

## Architecture at a Glance

This project implements a governed Azure Databricks Lakehouse that supports batch, streaming, ML, and Generative AI workloads.

- **Storage & Format** – ADLS Gen2 with Delta Lake in a Medallion (Bronze / Silver / Gold) layout  
- **Processing** – Azure Databricks (Spark clusters and SQL Warehouses)  
- **Governance** – Unity Catalog for catalogs, schemas, tables, permissions, and lineage  
- **Orchestration** – Databricks Jobs / Workflows for scheduled and dependency-based pipelines  
- **ML & LLM** – MLflow, AutoML, and Azure OpenAI integration  
- **Consumption** – SQL Warehouses serving curated Gold datasets for BI and analytics  
- **DevOps** – GitHub integration with CI/CD validation via GitHub Actions  

👉 For the full architecture write-up and design rationale, see the [architecture overview](docs/architecture.md).


---

## Key Architectural Design Decisions

### Medallion Architecture (Bronze / Silver / Gold)
A layered Lakehouse model was implemented to separate raw ingestion from curated analytical datasets, ensuring data quality, traceability, and downstream performance optimisation.

### Delta Live Tables (DLT) for Declarative Pipelines
DLT was selected to simplify transformation logic, enforce data expectations, and enable managed orchestration of streaming and batch workloads.

### Unity Catalog for Governance
Unity Catalog was implemented to:
- Centralise metadata
- Enable fine-grained access controls
- Support lineage visibility
- Separate storage from compute

### Managed Identity Integration
Azure Managed Identity was used for secure storage access, eliminating credential sprawl and aligning with enterprise security best practices.

### CI/CD Integration
GitHub Actions was integrated to support version control and automated validation of workflow changes.

---

## Architectural Outcomes

The implemented platform demonstrates:

- Scalable ingestion with schema evolution support
- Declarative transformation pipelines using DLT
- Governed access control via Unity Catalog
- Reproducible ML experimentation with MLflow
- Operationalised model serving endpoints
- Automated workflow orchestration
- CI/CD-enabled change management

This architecture reflects production-oriented data platform design.
---

## 📚 Reference


> [All Workflows](https://microsoftlearning.github.io/mslearn-databricks/) <br>
> [Implement a data lakehouse analytics solution with Azure Databricks](https://learn.microsoft.com/en-us/training/paths/data-engineer-azure-databricks/) <br>
> [Implement a machine learning solution with Azure Databricks](https://learn.microsoft.com/en-us/training/paths/build-operate-machine-learning-solutions-azure-databricks/) <br>
> [Implement a data engineering solution with Azure Databricks](https://learn.microsoft.com/en-us/training/paths/azure-databricks-data-engineer/) <br>
> [Implement Generative AI engineering with Azure Databricks](https://learn.microsoft.com/en-us/training/paths/implement-generative-ai-engineering-azure-databricks/)

---
