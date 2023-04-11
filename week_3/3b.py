import snowflake.connector
import os
import pandas as pd

conn = snowflake.connector.connect(
                user='sushma.k@anko.com',
                account='kmartau.ap-southeast-2.privatelink',
                warehouse='KSF_DATA_SCIENTIST_WH',
                database='DATABASE',
                schema='SCHEMA',
                authenticator='externalbrowser'
                )
cur = conn.cursor()
# Execute SQL statement
query=cur.execute("""SELECT t1.rbu_description, t1.product_code, t1.product_name, t1.month, t1.total_quantity_sold
FROM (
  SELECT RBU_DESCRIPTION, PRODUCT_CODE, PRODUCT_NAME, MONTH(transaction_timestamp) AS month, SUM(QUANTITY_SOLD) AS TOTAL_QUANTITY_SOLD,
    ROW_NUMBER() OVER (PARTITION BY RBU_DESCRIPTION, MONTH(transaction_timestamp) ORDER BY SUM(QUANTITY_SOLD) DESC) AS rn
  FROM KSF_SOPHIA_DATA_INTELLIGENCE_HUB_PROD.SALES.FACT_SALES_DETAIL s
  JOIN KSF_SOPHIA_DATA_INTELLIGENCE_HUB_PROD.COMMON_DIMENSIONS.DIM_PRODUCT p
  ON s.FK_PRODUCT_ID = p.SK_PRODUCT_ID
  WHERE YEAR(transaction_timestamp) = 2022
  GROUP BY RBU_DESCRIPTION, PRODUCT_CODE, PRODUCT_NAME, MONTH(transaction_timestamp)
) t1
WHERE t1.rn = 1
ORDER BY t1.month, t1.total_quantity_sold DESC;
""")
# Fetch result
df = cur.fetch_pandas_all()
df