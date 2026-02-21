import pandas as pd
import matplotlib.pyplot as plt


class SalesDashboard:

    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.filename, sep="\t")
            self.data["SALES"] = pd.to_numeric(self.data["SALES"], errors="coerce")
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("Error: data.txt file not found.")
        except Exception as e:
            print("Error loading data:", e)

    def calculate_total_sales(self):
        if self.data is None:
            print("Please load data first.")
            return None

        summary = self.data.groupby("PRODUCTLINE")["SALES"].sum()
        return summary

    def generate_line_chart(self, summary):
        if summary is None:
            print("No data available to plot.")
            return

        summary.plot(kind="line", marker="o")
        plt.title("Total Sales Per Product")
        plt.xlabel("Product Line")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def export_report(self, summary):
        if summary is None:
            print("No data available to export.")
            return

        try:
            with open("report.txt", "w") as file:
                file.write("SALES SUMMARY REPORT\n")
                file.write("====================\n")
                for product, total in summary.items():
                    file.write(f"{product} : {total}\n")

            print("Report exported successfully.")
        except Exception as e:
            print("Error writing report:", e)