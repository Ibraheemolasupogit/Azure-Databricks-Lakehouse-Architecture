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

> (Optionally drop in an architecture diagram later, but text is fine for now.)

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
