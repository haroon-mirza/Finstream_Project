-- your_dbt_model.sql

WITH base AS (
    SELECT 
        current_timestamp() AS ingestion_timestamp,
        JSON: "1. open"::STRING AS open_price,
        JSON: "2. high"::STRING AS high_price,
        JSON: "3. low"::STRING AS low_price,
        JSON: "4. close"::STRING AS close_price,
        JSON: "5. volume"::STRING AS volume
    FROM TRANSFORMEDSTOCKDATA
)
SELECT 
    ingestion_timestamp,
    CAST(open_price AS FLOAT) AS open_price,
    CAST(high_price AS FLOAT) AS high_price,
    CAST(low_price AS FLOAT) AS low_price,
    CAST(close_price AS FLOAT) AS close_price,
    CAST(volume AS INT) AS volume
FROM base
