# Comparison of data quality tools

I chose Soda, Open Metadata and Great Expectations.

### Rule definition
 - **Soda**:

   SodaCL (Yaml-based) configuration https://docs.soda.io/soda-cl-overview
```yaml
# Checks for basic validations
checks for dim_customer:
  - row_count between 10 and 1000
  - missing_count(birth_date) = 0
  - invalid_percent(phone) < 1 %:
      valid format: phone number
  - invalid_count(number_cars_owned) = 0:
      valid min: 1
      valid max: 6
  - duplicate_count(phone) = 0
```
 - **Open Metadata**:
   - no-code definition - https://docs.open-metadata.org/latest/how-to-guides/data-quality-observability/quality/test
   - Yaml-based config - https://docs.open-metadata.org/latest/how-to-guides/data-quality-observability/quality
 - **Great Expectations**:

   Python-based config - https://docs.greatexpectations.io/docs/core/define_expectations/create_an_expectation

### Alerts
- **Soda** (Cloud):

   Supports alerting only to Slack - https://docs.soda.io/collaborate#set-alert-notification-rules
- **Open Metadata**:

   Supports alerting to Slack, Email, Webhook, MS Teams - https://docs.open-metadata.org/latest/how-to-guides/data-quality-observability/observability/alerts
- **Great Expectations** (Cloud):
   
   Supports alerting to Email - https://docs.greatexpectations.io/docs/cloud/alerts/manage_email_alerts

### Data onservability
- **Soda**:

  Can track key data quality metrics like counts, recent timestamp, averages - https://docs.soda.io/soda-v4/data-observability
- **Open Metadata**:

  Look similar to Soda, but also supports Incident management capabilities - https://docs.open-metadata.org/latest/how-to-guides/data-quality-observability/observability
- **Great Expectations**:

   I didn't find any documentation on this topic.