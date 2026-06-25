# Set the initial total to 0
total = 0.0

print("=== DecodeLabs Expense Tracker ===")
print("System Initialized. Awaiting data...")
print("Type 'quit' at any time to halt execution.")
print("=" * 34 + "\n")

# Keep asking for expenses until the user decides to quit
while True:
    
    # Get the expense amount from the user
    raw_data = input("Enter expense amount: ")
    
    # Check if the user wants to stop
    if raw_data.strip().lower() == 'quit':
        print("\n[!] 'quit' entered. Stopping the tracker...")
        break
        
    # Make sure the user entered a valid number
    try:
        # Convert the text into a decimal number (float) so we can handle cents
        new_expense = float(raw_data)
        
        # Add the new expense to our running total
        total += new_expense
        print(f"  --> Logged: ${new_expense:.2f}. Running Total: ${total:.2f}\n")
        
    except ValueError:
        # If they didn't type a number, let them know instead of crashing
        print("  [X] Invalid Data: Please enter a valid numerical value.\n")

# Show the final total when the loop ends
print("\n" + "=" * 34)
print(f"FINAL TOTAL: ${total:.2f}")
print("=" * 34)
