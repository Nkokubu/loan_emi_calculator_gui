import tkinter as tk
from tkinter import messagebox

def calculate_emi():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        years = float(entry_years.get())

        monthly_rate = rate / (12 * 100)
        months = years * 12

        emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
        total_payment = emi * months
        total_interest = total_payment - principal

        label_result.config(text=f"Monthly EMI: ₹{emi:.2f}\n"
                                 f"Total Payment: ₹{total_payment:.2f}\n"
                                 f"Total Interest: ₹{total_interest:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create window
root = tk.Tk()
root.title("Loan EMI Calculator")

# Layout
tk.Label(root, text="Loan Amount (Principal):").grid(row=0, column=0, sticky="w")
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1)

tk.Label(root, text="Annual Interest Rate (%):").grid(row=1, column=0, sticky="w")
entry_rate = tk.Entry(root)
entry_rate.grid(row=1, column=1)

tk.Label(root, text="Loan Tenure (Years):").grid(row=2, column=0, sticky="w")
entry_years = tk.Entry(root)
entry_years.grid(row=2, column=1)

tk.Button(root, text="Calculate EMI", command=calculate_emi).grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="", justify="left", font=("Arial", 12), fg="blue")
label_result.grid(row=4, column=0, columnspan=2)

root.mainloop()
