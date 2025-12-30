# Run juffle shop via DBT

I used BigQuery as a warehouse.

### Log of executed commands
```shell
dbt debug
```
![screenshot1](screenshots/screenshot1.png)

```shell
dbt seed
```
![screenshot2](screenshots/screenshot2.png)

```shell
dbt run
```
![screenshot3](screenshots/screenshot3.png)

```shell
dbt test
```
![screenshot4](screenshots/screenshot4.png)
![screenshot5](screenshots/screenshot5.png)

### Lineage graph
![screenshot6](screenshots/screenshot6.png)

### Tables overview

Datasets:
![screenshot7](screenshots/screenshot7.png)

Jaffle dataset tables:
![screenshot8](screenshots/screenshot8.png)

Data in the customer table:
![screenshot9](screenshots/screenshot9.png)