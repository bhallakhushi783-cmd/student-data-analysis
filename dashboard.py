import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# Create Total Sales column
df["Total_Sales"] = df["Price"] * df["Quantity"]

# City-wise total sales
city_sales = df.groupby("City")["Total_Sales"].sum().reset_index()

# Product-wise total sales
product_sales = df.groupby("Product")["Total_Sales"].sum().reset_index()

#Top Product in each city
top_product_per_city = (
    df.groupby(["City", "Product"])["Total_Sales"]
    .sum()
    .reset_index()
    .sort_values(["City", "Total_Sales"], ascending=[True, False])
    .groupby("City")
    .head(1)
)

# Clean Output
print("\n=== SALES ANALYSIS DASHBOARD ===")
print("\nCity-wise Total Sales:\n", city_sales)
print("\nProduct-wise Total Sales:\n", product_sales)
print("\nTop Product in Each City:\n", top_product_per_city)

# Create Dashboard (2 graphs in one screen)
plt.figure(figsize=(10,5))

# Graph 1: City-wise Sales
plt.subplot(1, 2, 1)
plt.bar(city_sales["City"], city_sales["Total_Sales"])
plt.title("City-wise Sales")
plt.xlabel("City")
plt.ylabel("Total_Sales")

# Graph 2: Product-wise Sales
plt.subplot(1,2, 2)
plt.bar(product_sales["Product"], product_sales["Total_Sales"])
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total_Sales")

plt.tight_layout()
plt.show()




