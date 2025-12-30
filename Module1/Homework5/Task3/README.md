# Data-Specific CI/CD Challenges

My day-to-day work is not directly related to Data Engineering, but rather to backend development with OLTP workloads.  
Typically, I encounter two main data-related challenges:

- Schema evolution
- Data migration

---

## Schema evolution

In most cases, I use Liquibase, as it is the default tool in the Spring ecosystem.  
It allows me to define changesets in SQL format and apply them to the database.

By default, Liquibase changesets are executed during application startup, but I prefer to run them through the CI/CD pipeline (Jenkins).  
This approach allows multiple service instances to be redeployed concurrently without having to wait for one instance to finish schema migration.

---

## Data migration

Depending on the complexity of the migration and the data volume, I use one of the following approaches:

1. **Liquibase changeset**
    - SQL modification statements (`INSERT`, `UPDATE`, `DELETE`)
    - [Custom change](https://docs.liquibase.com/reference-guide/customchange), which allows writing custom Java code for data manipulation

2. **Spring Batch**  
   Spring Batch is an ETL tool in the Spring ecosystem that allows implementing complex data processing logic.

---

## Zero-downtime deployment example

Consider the case where a new non-nullable column needs to be added to a table.  
The steps to apply this change without downtime are:

1. **Add the new column using a Liquibase changeset.**  
   At this stage, the new column is created as nullable, because existing rows must be updated before the non-null constraint can be applied.

2. **Deploy an application version that writes data to the new column.**  
   From this point on, the application sets a value for the new column for all newly created records. Existing records still have `NULL` in this column.

3. **Run a data migration using either Liquibase or Spring Batch.**  
   All rows with a `NULL` value in the new column are initialized with valid data. After this step, there should be no `NULL` values remaining in the column.

4. **Add the non-nullable constraint using a Liquibase changeset.**  
   Now that all data has been backfilled, the column can safely be made non-nullable.
