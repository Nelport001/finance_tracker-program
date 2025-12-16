def Choose_section(ledger):
    while True:
        section = input("Choose a section (Revenue/Expense): ").strip().title()
        if not section in ledger:
            print("Value not found in ledger")
            print(f"This are the section vailable:")
            for sec in ledger:
                print("-", sec)
            continue
        return section        
def choose_category(ledger, section):
        while True:
            print("Available categories: ")
            for cat in ledger[section]:
                print("-", cat)
        
            category = input("Enter category: ").strip().lower()
            if category not in ledger[section]:
                print("category not found in section. Try again.")
                continue
            return category
def Enter_amount(ledger):
        while True:
            try:
                amount = float(input("Enter amount: "))
                
                if amount <=  0:
                    print("The amount needs to be greater than $0")
                    continue
                return amount
            except ValueError:
                print("Enter a valid number: ")
                
    

def main():
     ledger = {'Revenue':{'sales': 0.00, 'job': 0.00, 'side hustle': 0.00 },
              'Expenses': {'rent': 0.00, 'electricity': 0.00, 'inventory': 0.00}}
     while True:
        option = input("1) Add entry 2) Print P&L 3)Quit: ")
        if option == "1":
            section = Choose_section(ledger)
            category = choose_category(ledger, section)
            amount = Enter_amount(ledger)

            ledger[section][category] += amount
            print(f"Added ${amount: .2f} to {section} -> {category}")
        elif option == '2':
            print("\n---P&L---")
            total_rev = sum(ledger["Revenue"].values())
            total_exp = sum(ledger["Expenses"].values())
            profit = total_rev - total_exp
            print("Revenue: ")
            for k, v in ledger["Revenue"].items():
                print(f"{k}: ${v: .2f}")
            
            print("Expenses: ")
            for k, v in ledger["Expenses"].items():
                print(f"{k}: {v: .2f}")
            
            print(f"\nTotal Revenue: ${total_rev: .2f}")
            print(f"Total Expenses: ${total_exp: .2f}")
            print(f"Total Profits: ${profit: .2f}\n")
        elif option == '3':
            break
main()