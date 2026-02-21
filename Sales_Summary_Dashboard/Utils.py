def display_menu():
    print("\n===== SALES SUMMARY DASHBOARD =====")
    print("1. Load Sales Data")
    print("2. View Total Sales Per Product")
    print("3. Generate Line Chart")
    print("4. Export Summary Report")
    print("5. Exit")


def get_choice():
    try:
        return int(input("Enter your choice (1-5): "))
    except ValueError:
        return None