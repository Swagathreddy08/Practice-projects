def expense(n):
    if n=="1":
        limit2=10000
        expense_name="Hotel"
    elif n=="2":
        limit2=50000
        expense_name="flights"
    elif n=="3":
        limit2=5000
        expense_name="transportation"
    elif n=="4":
        limit2=2000
        expense_name="meals"
    elif n=="5":
        limit2=2000
        expense_name="office supplies"
    elif n=="6":
        limit2=1000
        expense_name="internet/mobile expences"
    elif n=="7":
        limit2=15000
        expense_name="training/conferences"
    return expense_name,limit2

def display(name, eid, Dept, expense_name, spent, report, promo_code, discount_amount, final_price):
            print(f'''
            Employee Name:       {name}
            Employee ID:         {eid}
            Department:          {Dept}
            expense category:    {expense_name}      
            Amount Spent:        {spent}
            Eligibility :        {report}
            Promotional Code:    {promo_code}
            Discount Amount:     {discount_amount}
            Final Price:         {final_price}
            status:              Reimbursement will be processed for the amount of {final_price}''')
def refund(limit2,spent,discount_rate):
    eligibility=min(spent,limit2)
    discount_amount = eligibility * discount_rate
    final_price = eligibility - discount_amount
    if (eligibility<=limit2):
        print("Your expense is within the limit for pre-approved expenses. Reimbursement will be processed.")
        return eligibility,discount_amount,final_price
    else:
        print(f'''Your expense is not within the limit for pre-approved expenses. 
            Reimbursement will be processed for the amount of {spent}. because its
            not with in the limit of {limit2} for {expense_name} expenses.''')


print("******************************************")
print("EMPLOYEE EXPENSE MANAGEMENT SYSTEM")
print("******************************************")
print("1. Hotel")
print("2. flights")
print("3. transportation")
print("4. meals")
print("5. office supplies")
print("6. internet/mobile expences")
print("7. training/conferences")

print("******************************************")
print("User Input Section")
print("******************************************")
name=input("Enter your name: ")
eid=input("Enter your employee id: ")
Dept=input("Enter your department: ")
n = input("Enter your choice: ")
spent = int(input("Enter the amount spent: "))
Day=input("Enter the day of expense: ")
r=input("Do have receipt?:(yes/no) ")
pr=input("Do you have a promotional code? (yes/no): ").lower()
if pr=="yes":
    promo_code=input("Enter the promotional code: ")
    if promo_code=="DISCOUNT10":
        discount_rate=0.10
    elif promo_code=="DISCOUNT20":
        discount_rate=0.20
    elif promo_code=="DISCOUNT30":
        discount_rate=0.30
    else:
        print("Invalid promotional code")
        discount_rate=0
else:
    print("no promotional code")
    discount_rate=0
eligibility=0
expense_name,limit2=expense(n)
report=input(" is it pre aproved by manager?:(yes/no) ")
if report=="yes":
    limit=int(input("Enter the pre aproved expence amount: "))
    eligibility=min(limit,spent,limit2)
    discount_amount = eligibility * discount_rate
    final_price = eligibility - discount_amount
    if r=="yes":
        if (spent<=limit and spent<=limit2):
            print("Your expense is within the limit for pre-approved expenses. Reimbursement will be processed.")
            display(name, eid, Dept, expense_name, spent, report, promo_code, discount_amount, final_price)
        elif spent>limit and spent>limit2:
            print(f'''You have exceeded the limit for {expense_name} expenses. 
            Reimbursement will be processed for the maximum limit of {eligibility}.
            contact your manager for further assistance.''')
        elif spent>limit and spent<=limit2:
            print(f'''You have exceeded the limit for pre-approved expenses.
            Reimbursement will be processed for the maximum limit of {eligibility}.
            contact your manager for further assistance.''')
        else:
            print(f'''Your expense is within the limit for pre-approved expenses. 
            Reimbursement will be processed for the amount of {spent}. because its
            not with in the limit of {limit2} for {expense_name} expenses.''')
    elif r=="no":
        if spent<=limit and spent<=limit2:
            print(f'''Your expense is within the limit for pre-approved expenses. 
            but do not have a receipt.
            Reimbursement will not be processed for the amount of {spent}.''')
        elif spent>limit and spent>limit2: 
            print(f'''You have exceeded the limit for {expense_name} expenses. 
            Reimbursement will be processed for the maximum limit of {eligibility}.
            contact your manager for further assistance.''')
        elif spent>limit and spent<=limit2:
            print(f'''You have exceeded the limit for pre-approved expenses.
            Reimbursement will be processed for the maximum limit of {eligibility}.
            contact your manager for further assistance.''')
        else:
            print(f'''Your expense is within the limit for pre-approved expenses. 
            but do not have a receipt. 
            Reimbursement will not be processed for the amount of {spent}.''')
else:
    print("Your expense is not pre-approved by the manager. Reimbursement will not be processed directly .")
    job=input("enter your job title:  ")
    if eid!="":
        print("You are eligible to submit the expense report for reimbursement. Please seek approval from your manager before submitting.")
        if spent<=200:
            print("refund is not possible as the amount is less than 200")
        else:
            print("do you want to submit the expense report for reimbursement? (yes/no)")
            submit=input()
            if submit=="yes":
                print("Expense report submitted for reimbursement. You will be notified once the reimbursement is processed.")
                proof=input("do you have proof of expense? (yes/no) ")
                if proof=="yes":
                    eligibility,discount_amount,final_price=refund(limit2,spent,discount_rate)
                    display(name, eid, Dept, expense_name, spent, report, promo_code, discount_amount, final_price)
                else:
                    print("Expense report not submitted. so rejected")

