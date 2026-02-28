# Azure Databricks Lakehouse Architecture

## 1. Scenario

Design and optimise a governed Lakehouse on Azure Databricks to support batch, streaming, ML, and Generative AI workloads.

## 2. High-Level Architecture

- **Storage**: ADLS Gen2 (Bronze / Silver / Gold)
- **Processing**: Azure Databricks (Spark clusters, SQL Warehouse)
- **Data Format**: Delta Lake
- **Governance**: Unity Catalog (catalogs, schemas, tables, permissions)
- **Orchestration**: Jobs / Workflows (optionally Data Factory)
- **ML & LLM**: MLflow, AutoML, Azure OpenAI integration
- **Consumption**: SQL Warehouses serving curated Gold datasets for BI / analytics
- **DevOps**: GitHub integration with CI/CD workflow validation


### Structural Overview

```mermaid
flowchart LR

    subgraph Sources
        A1[Batch Data]
        A2[Streaming Data]
        A3[External Knowledge Sources]
    end

    subgraph Ingestion
        B1[Auto Loader]
        B2[Spark Structured Streaming]
    end

    subgraph Lakehouse
        C1[Bronze Delta Tables]
        C2[Silver Delta Tables]
        C3[Gold Delta Tables]
    end

    subgraph ML
        D1[MLflow Tracking]
        D2[Model Registry]
    end

    subgraph LLM
        E1[Vector Search Index]
        E2[RAG Workflow]
    end

    subgraph Governance
        F1[Unity Catalog]
        F2[RBAC & Data Access Controls]
    end

    A1 --> B1
    A2 --> B2
    B1 --> C1
    B2 --> C1
    C1 --> C2
    C2 --> C3

    C2 --> D1
    D1 --> D2

    C2 --> E1
    E1 --> E2

    C1 --- F1
    C2 --- F1
    C3 --- F1
    D2 --- F1
    E2 --- F1



## 3. Design Decisions

- Medallion architecture to separate raw, curated, and consumption layers.
- Delta Lake for ACID, schema evolution, and efficient upserts.
- Unity Catalog for centralised governance across workspaces.
- SQL Warehouse used for BI / reporting workloads.

## 4. Security & Governance

- Access controlled via Unity Catalog roles and Azure RBAC.
- Secrets stored in Key Vault-backed scopes (if used).
- Private networking and VNet integration (where applicable).

## 5. Performance & Optimisation

- Partitioned large tables by date / key columns.
- Used `OPTIMIZE` and `ZORDER` on hot tables.
- Tuned cluster size and autoscaling based on workload patterns.
