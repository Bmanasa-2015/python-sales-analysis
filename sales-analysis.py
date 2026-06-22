import pandas as pd
import matplotlib.pyplot as plt
import os



class SalesDataAnalysis:

    def __init__(self):
        self.df = None

    # Load Dataset
    def load_data(self):
        url = "https://github.com/Bmanasa-2015/python-flask-project/raw/refs/heads/main/Retail_sales_data.csv"
        self.df = pd.read_csv(url)
        print("\nData Loaded Successfully!")
        print("Rows:", len(self.df))
        print("Columns:", self.df.columns.tolist())

    
    # Display Dataset
    def display_dataset(self):

        if self.df is None:
            print("Please load data first.")
            return

        print("\nDataset Head")
        print(self.df.head())

        print("\nDataset Info")
        self.df.info()

        print("\nShape")
        print(self.df.shape)

        print("\nColumns")
        print(self.df.columns)

        print("\nData Types")
        print(self.df.dtypes)

        print("\nMissing Values")
        print(self.df.isnull().sum())

    # Clean Dataset
    def clean_dataset(self):

        if self.df is None:
            print("Please load data first.")
            return

        self.df['Date'] = pd.to_datetime(self.df['Date'])

        self.df.drop_duplicates(inplace=True)

        self.df['Quantity Sold'].fillna(
            self.df['Quantity Sold'].mean(),
            inplace=True
        )

        self.df['Unit Price'].fillna(
            self.df['Unit Price'].mean(),
            inplace=True
        )

        self.df['Total Sales Amount'].fillna(
            self.df['Total Sales Amount'].mean(),
            inplace=True
        )

        self.df['Payment Method'].fillna(
            self.df['Payment Method'].mode()[0],
            inplace=True
        )

        self.df['Customer Segment'].fillna(
            self.df['Customer Segment'].mode()[0],
            inplace=True
        )

        print("\nData Cleaned Successfully!")

    # Verify Dataset
    def verify_data(self):

        if self.df is None:
            print("Please load data first.")
            return

        print("\nData Types")
        print(self.df.dtypes)

        print("\nMissing Values")
        print(self.df.isnull().sum())

    # Payment Analysis
    def payment_analysis(self):

        if self.df is None:
            print("Please load data first.")
            return

        payment_count = self.df['Payment Method'].value_counts()

        print("\nPayment Method Analysis")
        print(payment_count)

        print(
            "\nMost Common Payment Method:",
            self.df['Payment Method'].mode()[0]
        )

    # Top Spending Customers
    def top_spending_customers(self):

        if self.df is None:
            print("Please load data first.")
            return

        top_customers = (
            self.df.groupby("Customer ID")
            ["Total Sales Amount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        print("\nTop 10 Spending Customers")
        print(top_customers)

    # Customer Purchase Behaviour
    def customer_purchase_behavior(self):

        if self.df is None:
            print("Please load data first.")
            return

        customer_orders = (
            self.df.groupby("Customer ID")
            ["Order ID"]
            .nunique()
        )

        repeat_buyers = (customer_orders > 1).sum()
        one_time_buyers = (customer_orders == 1).sum()

        print("\nRepeat Buyers:", repeat_buyers)
        print("One-Time Buyers:", one_time_buyers)
    os.makedirs("Visualization", exist_ok=True) 
    # Daily Order Volume Trend
    def daily_order_volume(self):

        if self.df is None:
            print("Please load data first.")
            return

        self.df['Date'] = pd.to_datetime(self.df['Date'])

        daily_orders = (
            self.df.groupby(self.df['Date'].dt.date)
            ['Order ID']
            .nunique()
            .reset_index(name='Order Count')
        )

        plt.figure(figsize=(10, 5))

        plt.plot(
            daily_orders['Date'],
            daily_orders['Order Count'],
            marker='o'
        )

        plt.title("Daily Order Volume Trend")
        plt.xlabel("Date")
        plt.ylabel("Orders")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.savefig("Visualization/daily-order.png")

        plt.show()

    # Top Products Revenue
    def top_products_revenue(self):

        if self.df is None:
            print("Please load data first.")
            return

        product_revenue = (
            self.df.groupby("Product Name")
            ["Total Sales Amount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        print("\nTop 10 Products by Revenue")
        print(product_revenue)

        plt.figure(figsize=(10, 5))
        product_revenue.plot(kind='bar')

        plt.title("Top Products Revenue")
        plt.xlabel("Product")
        plt.ylabel("Revenue")

        plt.tight_layout()
        plt.savefig("Visualization/top-products.png")
        plt.show()

    # Orders by Segment
    def orders_by_segment(self):

        if self.df is None:
            print("Please load data first.")
            return

        segment_orders = (
            self.df['Customer Segment']
            .value_counts()
        )

        print("\nOrders By Customer Segment")
        print(segment_orders)

        plt.figure(figsize=(8, 5))

        segment_orders.plot(kind='bar')

        plt.title("Orders By Customer Segment")
        plt.xlabel("Customer Segment")
        plt.ylabel("Orders")

        plt.tight_layout()
        plt.savefig("Visualization/orders-by-customersegment.png")
        plt.show()

    # Export Reports
    def export_reports(self):

        if self.df is None:
            print("Please load data first.")
            return

        top_customers = (
            self.df.groupby("Customer ID")
            ["Total Sales Amount"]
            .sum()
            .sort_values(ascending=False))
        product_revenue = (
            self.df.groupby("Product Name")
            ["Total Sales Amount"]
            .sum()
            .sort_values(ascending=False) )   
        city_sales = (
            self.df.groupby("City")
            ["Total Sales Amount"]
            .sum()
            .sort_values(ascending=False))

        os.makedirs("reports", exist_ok=True)

        top_customers.to_csv("reports/top_customers_report.csv")

        product_revenue.to_csv("reports/product_revenue_report.csv")

        city_sales.to_csv("reports/city_sales_report.csv")

        print("\nReports Exported Successfully!")

        print("top_customers_report.csv")
        print("product_revenue_report.csv")
        print("city_sales_report.csv")


# ------------------------
# Main Program
# ------------------------
if __name__ == "__main__":
    analyzer = SalesDataAnalysis()
    analyzer.load_data()
    analyzer.clean_dataset()

    analyzer.top_spending_customers()

    analyzer.customer_purchase_behavior()

    analyzer.daily_order_volume()

    analyzer.top_products_revenue()

    analyzer.orders_by_segment()

    analyzer.export_reports()

     

   
