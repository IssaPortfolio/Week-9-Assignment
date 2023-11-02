import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import json

# Requirement: Creates an empty list called "sales_data"
def process_csv(file_path):
    sales_data = []  # Empty list created here

    # Requirement: Opens up this file (SalesJan2009.csv - you need to download it to your hard drive) and converts the data within it to JSON format.
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # Read the header row
        for row in csv_reader:
            transaction_date, product, price, payment_type, name, city, state, country = row

            # Requirement: Clean up extra quote characters from each piece of data you process.
            transaction_date = transaction_date.strip('"')
            product = product.strip('"')
            price = price.strip('"')
            payment_type = payment_type.strip('"')
            name = name.strip('"')
            city = city.strip('"')
            state = state.strip('"')
            country = country.strip('"')

            # Requirement: Create a dictionary for each line. As you create each dictionary, you will append it to the sales_data list.
            data = {
                "Transaction_date": transaction_date,
                "Product": product,
                "Price": price,
                "Payment_Type": payment_type,
                "Name": name,
                "City": city,
                "State": state,
                "Country": country
            }

            sales_data.append(data)  # Appending dictionary to the list

    # Convert the data to JSON
    json_data = json.dumps(sales_data, indent=4)

    # Requirement: At the end of your processing, you will save your sales_data list to a file called "transaction_data.json"
    with open("transaction_data.json", 'w') as json_file:
        json_file.write(json_data)

    # Requirement: Utilize the ‘messagebox’ widget at least once in your UI.
    messagebox.showinfo("Success", "CSV data processed and saved to JSON")

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        process_csv(file_path)

# Requirement: Must have a UI showing a TOP LEVEL (main) window, as well as at least one OTHER supporting window.
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.configure(bg="green")
    tk.Label(new_window, text="This is a new window", bg="green", fg="gold").pack()

root = tk.Tk()
root.title("Sales Data Processor")

# Requirement: The color scheme of the UI must reflect your personal work (firm) at which you work OR Wayne State University, or your High School.
root.configure(bg="green")  # Green background and gold text color for Wayne State University

# Define your custom color for buttons
button_color = "gold"

# Requirement: This MAIN window must have a QUIT button that uses the “.quit()” method (kills all the windows).
quit_button = tk.Button(root, text="Quit", command=root.quit, bg=button_color, fg="green")
quit_button.pack()

open_file_button = tk.Button(root, text="Open CSV File", command=open_file_dialog, bg=button_color, fg="green")
open_file_button.pack()

new_window_button = tk.Button(root, text="Open New Window", command=open_new_window, bg=button_color, fg="green")
new_window_button.pack()

root.mainloop()
