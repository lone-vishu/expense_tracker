import datetime
expense =[]
def expense_details(exp,idx= None):
    if idx is not None:
        print(f"\n === Expense Details {idx} ===")
    print(f"Date:      {exp['date']}")
    print(f"Category:  {exp['category'].title()}")
    print(f"Amount:    {exp['amount']}")
    print(f"Note:      {exp['note'].title()}")
    print("-"*30)

def search_expense(search_term, search_type):
    "Searches the expense list based on date or other criteria"
    search_term = str(search_term).strip().lower()
    results=[]

    for item in expense:
        found = False
        
        if search_type == 1:
            
            if search_term in str(item['date']):
                found = True

        elif search_type == 2:
            
            if search_term in item['category'] or search_term in item['note']:
                found = True

            try:
                if int(search_term) == item['amount']:
                    found = True
            except ValueError:
                pass

        if found:
            results.append(item)

    return results
        

def delete_expense(serach_term, search_type):
    """Delete expenses based on date or other criteria using list filtering"""
    global expense
    search_term = str(search_term).strip().lower()

    records_before = len(expense)

    if search_type == 1:

        expense = [i for i in expense if search_term not in str(i['date'])]

    elif search_type == 2:

        new_expense = []
        for i in expense:
            is_match = False

            if search_term == i['category'] or search_term == i['note']:
                is_match = True

            try:
                if int(search_term) == i['amount']:
                    is_match = True
            except ValueError:
                pass

            if not is_match:
                new_expense.append(i)

        expense[:] = new_expense

        records_deleted = records_before - len(expense)

        return records_deleted
while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. Search Expense")
    print("4. Summary")
    print("5. Delete Expense")
    print("6. Exit")
    try:
        op = int(input('Choose option'))
        if op == 1:
            while True:
                exp = {}
                try:
                    add = int(input('Type 1 to add and 2 to exit'))
                except ValueError:
                    print("Invalid input. Please enter 1 or 2.")
                    continue
                if add == 1:
                    exp['date'] = datetime.date.today()
                    exp['category']= input('Category:').strip().lower()
                    
                    while True:
                        try:
                            exp['amount']= int(input("Enter amount expended:"))
                            if exp['amount'] <= 0:
                                print("Amount must be positive")
                            else:
                                break
                        except ValueError:
                            print("Invalid amount. Please enter a number.")
                    exp['note']=input('Note:').strip().lower()
                    expense.append(exp)
                    print("Expense added successfully!")
                elif add == 2:
                    break
                else:
                    print("Choose correct option")

        elif op == 2:
            if not expense:
                print("No records available")
            else:
                for i, t in enumerate(expense, 1):
                    expense_details(t,i)
            
        elif op == 3:
            if not expense:
                print("No record available to search")
            else:
                try:
                    ch = int(input("Type 1 to find by date and 2 to find by other:"))
                except ValueError:
                    print("Invalid input. Please enter 1 or 2.")
                    continue
                if ch == 1:
                    dt = input("Search by date (e.g., 2025-10):").strip().lower()
                    c = search_expense(dt,1)
                        
                elif ch == 2:
                    ot = input("Search by Category/ Note/Amount:").strip().lower()
                    c = search_expense(ot,2)
                else:
                    print("Choose correct option(1 or 2)")
                    continue
                
                if not c:
                    print("No records found.")
                else:
                    print(f"\n ---{len(c)} Record(s) Found --- ")
                    for i, t in enumerate(c,1):
                        expense_details(t,i)


                        
        elif op == 4:
            if not expense:
                print("No records available")
            else:
                ad = 0
                mx = 0
                for i in expense:
                    ad = ad +i["amount"]
                    if mx <= i["amount"]:
                        mx = i["amount"]
                print("Toatal spend:",ad)
                print("Maximun spend:",mx)

        
        elif op == 5:
            if not expense:
                print("No record to be deleted")
            else:
                try:
                    ch = int(input('Type 1 to delete by date and 2 for other'))
                except ValueError:
                    print('Invalid input. Please enter 1 or 2')
                    continue

                if ch == 1:
                    sb = input('Enter the date(e.g., 2025-10-05)for which the record has to be deleted:').strip().lower()
                    delete_count = delete_expense(sb,1)
                elif ch == 2:
                    sb = input("Type specs of details that has to deleted(it can be category/note/amount)").strip().lower()
                    delete_count = delete_expense(sb,2)
                else:
                    print("Choose correct option(1 or 2)")
                    continue

                if delete_count >0:
                    print(f"{delete_count}record(s) deleted successfully.")
                else:
                    print("No record found to be deleted.")

        elif op == 6:
            print("Exiting Expense Tracker, Goodbye")
            break
        else:
            print("Invalid option. Please choose between 1 to 6.")
    
    except ValueError:
        print('Enter Valid input(a number) for the menu option')
