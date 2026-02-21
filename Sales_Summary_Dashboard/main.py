from model import SalesDashboard
from Utils import display_menu, get_choice


def main():
    dashboard = SalesDashboard("data.txt")
    summary = None

    while True:
        display_menu()
        choice = get_choice()

        if choice == 1:
            dashboard.load_data()

        elif choice == 2:
            summary = dashboard.calculate_total_sales()
            if summary is not None:
                print("\nTotal Sales Per Product:")
                print(summary)

        elif choice == 3:
            dashboard.generate_line_chart(summary)

        elif choice == 4:
            dashboard.export_report(summary)

        elif choice == 5:
            print("Exiting program.")
            break

        else:
            print("Invalid input. Please enter 1-5.")


if __name__ == "__main__":
    main()