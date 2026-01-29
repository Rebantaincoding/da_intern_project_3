
#Load the dataset
import pandas as pd 
df = pd.read_csv(
    r"d:\developers_arena\week3\sales_data.csv"
)
#Checks the number of missing values in each column
print("\nNULL VALUES PER COLUMN\n")
print(df.isnull().sum())

#drops all the missing values
df.dropna(inplace=True)

#Checks all the duplicated values 
print("\nTOTAL DUPLICATED VALUES\n")
print(df.duplicated().sum())

#Deletes all the duplicated values
df.drop_duplicates(keep=False) 

#Calculation of total revenue of all products combined 
print('\nTOTAL REVENUE OF ALL PRODCUTS\n')
total_revenue = df['Total_Sales'].sum() 
print(total_revenue) 

#Calculation of total revenue of each product 
print('\nTOTAL REVENUE OF ALL PRODCUTS\n')
total_revenue_per_product=df.groupby('Product')['Total_Sales'].sum()
print(total_revenue_per_product)

#Calculate the average price of each product 
print("\nTOTAL REVENUE OF EACH PRODUCT\n")
avg_price=df.groupby('Product')['Price'].mean()
print(avg_price)