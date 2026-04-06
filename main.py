import pandas as pd

# Load data
df = pd.read_csv("sales_data.csv")

# Create Total Sales column
df["Total_Sales"] = df["Price"] * df["Quantity"]

# City-wise total sales
city_sales = df.groupby("City")["Total_Sales"].sum().reset_index()

# Top product in each city
top_product_per_city = (
    df.groupby(["City", "Product"])["Total_Sales"]
    .sum()
    .reset_index()
    .sort_values(["City", "Total_Sales"], ascending=[True, False])
    .groupby("City")
    .head(1)
)

# Output
print("City-wise Total Sales:\n", city_sales)
print("\nTop Product in Each City:\n", top_product_per_city)