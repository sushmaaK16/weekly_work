import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

df = pd.read_csv('C:/Users/ssushma/OneDrive - Kmart Australia Limited/KHome/Downloads/final_month_comparision.csv')

fig, ax = plt.subplots(figsize=(10, 6))

for rbu in df['RBU_DESCRIPTION'].unique():
    df_rbu = df[df['RBU_DESCRIPTION'] == rbu]
    ax.plot(df_rbu['MONTH'], df_rbu['TOTAL_QUANTITY_SOLD'], label=rbu)

ax.set_xlabel('Month')
ax.set_ylabel('Total Quantity Sold (log scale)')
ax.set_yscale('log')

ax.legend()

plt.show()