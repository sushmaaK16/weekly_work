import snowflake.connector
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


conn = snowflake.connector.connect(
                user='sushma.k@anko.com',
                account='kmartau.ap-southeast-2.privatelink',
                warehouse='KSF_DATA_SCIENTIST_WH',
                database='KSF_SOPHIA_DATA_INTELLIGENCE_HUB_PROD',
                schema='SCHEMA',
                authenticator='externalbrowser'
                )


cur = conn.cursor()

# Execute SQL statement
cur.execute("""  SELECT state, location_name, SUM(TOTAL_SELLING_PRICE_WITHOUT_GST) AS total_sales 
FROM KSF_SOPHIA_DATA_INTELLIGENCE_HUB_PROD.COMMON_DIMENSIONS.DIM_LOCATION DL
INNER JOIN KSF_SOPHIA_DATA_INTELLIGENCE_HUB_PROD.SALES.FACT_SALES_DETAIL FSD 
ON DL.SK_LOCATION_ID = FSD.FK_LOCATION_ID 
WHERE EXTRACT(MONTH FROM FSD.TRANSACTION_TIMESTAMP) = 3 AND EXTRACT(YEAR FROM FSD.TRANSACTION_TIMESTAMP) = 2023 
GROUP BY state, location_name 
QUALIFY ROW_NUMBER() OVER ( PARTITION BY state 
ORDER BY SUM(TOTAL_SELLING_PRICE_WITHOUT_GST) DESC ) <= 3 
ORDER BY state, total_sales DESC, location_name;

           

""")

# Fetch result
data = cur.fetch_pandas_all()


# Load data from CSV file
#data = pd.read_csv('sales_data.csv', delimiter='\t')

# Create barplot using seaborn
sns.set(style="whitegrid")
ax = sns.barplot(x="STATE", y="TOTAL_SALES", hue="LOCATION_NAME", data=data)

# Rotate x-axis labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')