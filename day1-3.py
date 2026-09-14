
def refund(n,spent):
    if n==1:
        limit=25000
        if spent>limit:
            print("You have exceeded the limit for client meetings. Reimbursement will be processed for the maximum limit of 25000.")
            print("contact your manager for further assistance.")
        else:
            print("Your expense is within the limit for client meetings. Reimbursement will be processed.")
            return spent
    elif n==2:
        limit=50000
        if spent>limit:
            print("You have exceeded the limit for business travel. Reimbursement will be processed for the maximum limit of 50000.")
            print("contact your manager for further assistance.")
        else:
            print("Your expense is within the limit for business travel. Reimbursement will be processed.")
            return spent
    elif n==3:
        limit=1000
        if spent>limit:
            print("You have exceeded the limit for food expenses. Reimbursement will be processed for the maximum limit of 1000.")
            print("contact your manager for further assistance.")
        else:
            print("Your expense is within the limit for food expenses. Reimbursement will be processed.")
            return spent
    elif n==4:
        limit=500
        if spent>limit:
            print("You have exceeded the limit for taxi expenses. Reimbursement will be processed for the maximum limit of 500.")
            print("contact your manager for further assistance.")
        else:
            print("Your expense is within the limit for taxi expenses. Reimbursement will be processed.")
            return spent
    elif n==5:
        limit=10000
        if spent>limit:
            print("You have exceeded the limit for hotel expenses. Reimbursement will be processed for the maximum limit of 10000.")
            print("contact your manager for further assistance.")
        else:
            print("Your expense is within the limit for hotel expenses. Reimbursement will be processed.")
            return spent
    elif n==6:
        limit=2000
        if spent>limit:
            print("You have exceeded the limit for office supplies. Reimbursement will be processed for the maximum limit of 2000.")
            print("contact your manager for further assistance.")
        else:
            print("Your expense is within the limit for office supplies. Reimbursement will be processed.")
            return spent
    elif n==7:
        limit=15000
        if spent>limit:
            print("You have exceeded the limit for conference expenses. Reimbursement will be processed for the maximum limit of 15000.")
            print("contact your manager for further assistance.")
        else:
            print("Your expense is within the limit for conference expenses. Reimbursement will be processed.")
            return spent
    

print("******************************************")
print("EMPLOYEE EXPENSE MANAGEMENT SYSTEM")
print("******************************************")
print("1. Client meetings limit 25000")
print("2. business travel limit 50000")
print("3. food limit 1000")
print("4. taxis limit 500")
print("5. hotels limit 10000")
print("6. office supplies limit 2000")
print("7. conferences limit 15000")
n = int(input("Enter your choice: "))
r=input("Do have receipt?:(yes/no) ")
report=input(" is it pre aproved by manager?:(yes/no) ")
if report=="yes":
    limit=int(input("Enter the pre aproved expence amount: "))
    spent=int(input("Enter the amount spent: "))
    if spent>limit:
        print("You have exceeded the pre-approved expense limit reembursement will be processed.")

    else:
        print("Your expense is within the pre-approved limit. do you want to submit the expense report for reimbursement? (yes/no)")
        submit=input()
        if submit=="yes":
            print("Expense report submitted for reimbursement. You will be notified once the reimbursement is processed.")
            amt=refund(n, spent)
        else:
            print("Expense report not submitted. so rejected")
elif report=="no":
    spent=int(input("Enter the amount spent: "))
    print("Your expense report is not pre-approved by the manager. Please seek approval before submitting for reimbursement.")
    job=input("enter your job title:  ")
    if job in ["manager","developer","tester","designer","sales"]:
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
                    amt=refund(n, spent)
            else:
                print("Expense report not submitted. so rejected")

