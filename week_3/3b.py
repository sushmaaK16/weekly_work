import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data into a pandas dataframe
data = pd.read_csv('C:/Users/ssushma/OneDrive - Kmart Australia Limited/KHome/Downloads/FINAL_MON_FEB.csv')

# Group data by RBU_DESCRIPTION and sum the TOTAL_QUANTITY_SOLD
grouped_data = data.groupby('RBU_DESCRIPTION')['TOTAL_QUANTITY_SOLD'].sum().reset_index()

# Sort data by the total quantity sold in descending order
grouped_data = grouped_data.sort_values('TOTAL_QUANTITY_SOLD', ascending=False)

# Set a custom color palette
custom_palette = ['#009B9E', '#FFC75F', '#FF5F5F', '#8E54E9', '#4776E6', '#53BBF4' ,'#19376D', '#FFB4B4', '#E11299', '#867070']

# Create a horizontal bar chart with a logarithmic scale and custom color palette
sns.barplot(x='TOTAL_QUANTITY_SOLD', y='RBU_DESCRIPTION', data=grouped_data, log=True, palette=custom_palette)

# Set chart title and axis labels
plt.title('Total Quantity Sold by RBU Description', fontweight='bold', fontsize=14)
plt.xlabel('Total Quantity Sold (log scale)', fontweight='bold', fontsize=12)
plt.ylabel('RBU Description', fontweight='bold', fontsize=12)

# Add annotations to the plot
for i, v in enumerate(grouped_data['TOTAL_QUANTITY_SOLD']):
    plt.text(v, i, str(int(v/1000000)) + 'M', color='white', ha='left', va='center', fontweight='bold')  #total quantity is converted into millions, x-coordinate (v), y-coordinate (i),

    # Add product names to the right side of the plot
    product_names = data[data['RBU_DESCRIPTION'] == grouped_data.iloc[i]['RBU_DESCRIPTION']]['PRODUCT_NAME'].unique()
    plt.text(1.05, i, '\n'.join(product_names), transform=plt.gca().get_yaxis_transform(), fontsize=10, color='gray')

# Set background color and add a texture
ax = plt.gca()   #This retrieves the current axes of the plot.
ax.set_facecolor('#F7F7F7')   #his sets the background color of the plot to a light gray color.
ax.grid(False)   #this turns off the gridlines on the plot.
ax.set_axisbelow(True)    #This sets the axis ticks and labels to appear below the plotted data.
ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.2)  #This adds dashed gray gridlines to the y-axis with a transparency of 0.2.
ax.xaxis.grid(color='gray', linestyle='dashed', alpha=0.2)  #his adds dashed gray gridlines to the x-axis with a transparency of 0.2.
ax.patch.set_alpha(0.5)   #This sets the alpha (transparency) of the plot background to 0.5.

# Use a custom font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Montserrat']

# Show the chart
plt.show()