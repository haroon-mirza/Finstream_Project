-- transform_stock_data.sql

WITH base AS (
    SELECT 
        symbol,
        timestamp,
        CAST("1. open" AS FLOAT) AS open_price,
        CAST("2. high" AS FLOAT) AS high_price,
        CAST("3. low" AS FLOAT) AS low_price,
        CAST("4. close" AS FLOAT) AS close_price,
        CAST("5. volume" AS INT) AS volume
    FROM raw_stock_data_table  -- Replace with your actual S3 table name
),
transformed AS (
    SELECT 
        symbol,
        timestamp,
        high_price - low_price AS price_range,
        close_price - open_price AS price_change,
        volume
    FROM base
)
SELECT * FROM transformed;
