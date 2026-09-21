lists=[["EMPLOYE ID","NAME","EXPENCE CATEGORY","Climed Amount","Eligible AMT","STATUS"]]
reject=[["EMPLOYE ID","NAME","EXPENCE CATEGORY","Climed amount","Reason"]]
def expence(n):
    if n=="1":
        limit2=10000
        exp_name="Hotel"
    elif n=="2":
        limit2=50000
        exp_name="flights"
    elif n=="3":
        limit2=5000
        exp_name="transportation"
    elif n=="4":
        limit2=2000
        exp_name="meals"
    elif n=="5":
        limit2=2000
        exp_name="office supplies"
    elif n=="6":
        limit2=1000
        exp_name="internet/mobile expences"
    elif n=="7":
        limit2=15000
        exp_name="training/conferences"
    else:
        print(" WRONG INPUT ")
    return exp_name,limit2

def submit():
    report=input(" is it pre aproved by manager?:(yes/no) ")
    spent=int(input("ENTER THE SPENT AMOUNT"))
    limit=int(input("Enter the max limit aproved by the manager"))
    choice=input('''
                     1)Hotel
                     2)flights
                     3)transpotation
                     4)meals
                     5)office supplies
                     6)mobile expence
                     7)training conference
                     ''')
    exp_name,lim2=expence(choice)
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
    eid=int(input("Enter your eployee id : "))
    name=input("Enter the name of the emplyee : ")
    dept=int(input("enter the dept no"))
    eligibility=min(limit,spent,lim2)
    if report=="yes":
        discount_amount = eligibility * discount_rate
        final_price = eligibility - discount_amount
        if r=="yes":
            if (spent<=limit and spent<=lim2):
                print("Your expense is within the limit for pre-approved expenses. Reimbursement will be processed.")
                status="aproved"
                l=[eid,name,exp_name,spent,final_price,status]
                lists.append(l)
            elif spent>limit and spent>lim2:
                print(f'''You have exceeded the limit for {exp_name} expenses. +
            Reimbursement will be processed for the maximum limit of {eligibility}.
            contact your manager for further assistance.''')
                status='partially aproved'
                l=[eid,name,exp_name,spent,final_price,status]
                lists.append(l)
            elif spent>limit and spent<=lim2:
                print(f'''You have exceeded the limit for pre-approved expenses.
            Reimbursement will be processed for the maximum limit of {eligibility}.
            contact your manager for further assistance.''')
                status='partially aproved'
                l=[eid,name,exp_name,spent,final_price,status]
                lists.append(l)
            else:
                print(f'''Your expense is within the limit for pre-approved expenses. 
            Reimbursement will be processed for the amount of {spent}. because its
            not with in the limit of {lim2} for {exp_name} expenses.''')
                status="partially aproved"
                l=[eid,name,exp_name,spent,lim2,status]
                lists.append(l)
        elif r=="no":
            reason="no proof of payment"
            status="rejected"
            l=[eid,name,exp_name,spent,0,status]
            l2=[eid,name,exp_name,spent,reason]
            lists.append(l)
            reject.append(l2)
    else:
        print("Your expense is not pre-approved by the manager. Reimbursement will not be processed directly .")
        reason="the expence is not pre aproved"
        status="rejected"
        l=[eid,name,exp_name,spent,0,status]
        l2=[eid,name,exp_name,spent,reason]
        lists.append(l)
        reject.append(l2)

def view():
    for i in lists:
        print(i)

def search():
    id=int(input("Enter the Id to be searched"))
    for i in lists[1:]:
        if i[0] == id:
            print(i)
        else:
            print("EMPLOYEE NOT FOUND") 

def rejected():
    for i in reject:
        print(i)

def summary():
    print("EXPENSE SUMMARY").center(30,"=")
    print("\n")
    app=par=re=cl=al=av=0
    for i in lists[1:]:
        if i[-1] == 'aproved':
            app+=1
        elif i[-1] == 'partially aproved':
            par+=1
        elif i[-1] != 'rejected':
            re+=i[-2]
        cl+=i[-3]   
    av=(cl/(len(lists)-1))
    print(f'''

Total Claims: {len(lists)-1}

Approved Claims: {app}
Partially Approved {par}
Rejected Claims: {len(reject)-1}

Total Amount Claimed: ₹{cl}
Total Amount Reimbursed: ₹{re}

Average Claim: ₹{av}''')


def totalexp():
    totalexpnce=0
    for i in lists[1:]:
        if i[-1] !='rejected':
            totalexpnce=i[-2]+totalexpnce
    print(f"Total reimbursement payable: {totalexpnce}")
    
print('''
========================================
     PRODUCTION INCIDENT ANALYZER
========================================

1. Submit
2. View
3. Search
4. Summary
5. Rejected 
6. Total Expence report
7. Exit''')
while True:
    choice=input("enter your chice ")
    match choice:
        case "1":
            submit()
        case "2":
            view()
        case "3":
            search()
        case "4":
            summary()
        case "5":
            rejected()
        case "6":
            totalexp()
        case "7":
            break
        case _:  
            print("wrong input")

