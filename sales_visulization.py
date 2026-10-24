
import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {
    "Product": ["Laptop", "Mobile", "Keyboard", "Mouse",
                "Monitor", "Laptop", "Mobile", "Mouse"],
    "Category": ["Electronics", "Electronics", "Accessories",
                 "Accessories", "Electronics", "Electronics",
                 "Electronics", "Accessories"],
    "Revenue": [60000, 40000, 5000, 3000,
                15000, 65000, 45000, 4000],
    "Profit": [8000, 6000, 1000, 700,
               2500, 9000, 7000, 900]
}

df = pd.DataFrame(data)

print("===== SALES DATA =====")
print(df)

# 1. Product-wise revenue
product_sales = df.groupby("Product")["Revenue"].sum()

plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Product-wise Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("product_revenue.png")
plt.show()

# 2. Category-wise sales
category_sales = df.groupby("Category")["Revenue"].sum()

plt.figure(figsize=(7, 5))
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category-wise Sales")
plt.ylabel("")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

# 3. Product-wise profit
product_profit = df.groupby("Product")["Profit"].sum()

plt.figure(figsize=(8, 5))
product_profit.plot(kind="bar")
plt.title("Product-wise Profit")
plt.xlabel("Product")
plt.ylabel("Profit (Rs.)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("product_profit.png")
plt.show()

# Final summary
print("\n===== SALES SUMMARY =====")
print("Total Revenue: Rs.", df["Revenue"].sum())
print("Total Profit: Rs.", df["Profit"].sum())
print("Best-Selling Product:",
      product_sales.idxmax())
print("Most Profitable Product:",
      product_profit.idxmax())

print("\nAll charts generated successfully!")
