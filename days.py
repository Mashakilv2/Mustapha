from datetime import datetime, timedelta

def generate_calendar_file():
    try:
        # Ask user for input
        x = int(input("Enter the number of past days to print: "))

        # Calculate the date range
        end_date = datetime.today()
        start_date = end_date - timedelta(days=x)

        # Create and write to the file
        file_name = "calendar_dates.txt"
        with open(file_name, "w") as file:
            file.write(f"Calendar from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}\n\n")
            for i in range(x + 1):
                date = end_date - timedelta(days=i)
                file.write(f"{date.strftime('%Y-%m-%d')} - {date.strftime('%A')}\n")

        print(f"Calendar file '{file_name}' created successfully.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Run the function
generate_calendar_file()
# Minor update for PR review
