import sys

def clasify(a):
    if a==0:
        return "HEALTHY"
    elif a == 1:
        return "WARNING"
    else:
        return "CRITICAL" 

def basic_stats(logs):    
    errorline=warningline=infoline=count=0
    print("the basic format ")
    words=logs.split()
    lenth=len(logs)
    lines=logs.splitlines()
    for line in lines:
        if "error" in line:
            errorline+=1
        elif "warning" in line:
            warningline+=1
        elif "info" in line:
            infoline+=1
        count+=1
    print("************************************")
    print("Basic Statistics")
    print("************************************")
    print(f'''
      The total character in the ord are : {lenth}
      Total logs    :   {count}
      INFO          :   {infoline}
      WARNING       :   {warningline}
      ERROR         :   {errorline}
      \n''')
    print(" WORDS IN THE LOG ARE :\n")
    print(set(words))

def service_stats(logs):
    words=logs.split()
    wo1=payment=auth=order=inventory=notification=0
    for word in words:
        wo1+=1
        if "payment-service" in word:
            payment+=1
        elif "auth-service" in word:
            auth+=1
        elif "order-service" in word:
            order+=1
        elif "inventory-service" in word:
            inventory+=1
        elif "notification-service" in word:
            notification+=1
    print(f'''
     payment-service       :  {payment}
     auth-service          :  {auth}
     order-service         :  {order}
     inventory-service     :  {inventory}
     notification-service  :  {notification}
      \n''')
def error_logs(logs):
    lines=logs.splitlines()
    e1=e2=e3=e4=e5=0
    for line in lines:
        if "payment-service error" in line :
            e1+=1
        elif "auth-service error" in line:
            e2+=1
        elif "order-service error" in line:
            e3+=1
        elif "inventory-service error" in line:
            e4+=1
        elif "notification-service error" in line:
            e5+=1
    print(f'''
         payment-service-error       :  {e1}
         auth-service-error          :  {e2}
         order-service-error         :  {e3}
         inventory-service-error     :  {e4}
         notification-service-error  :  {e5}
    \n''')

    test=max(e1,e2,e3,e4,e5)
    if test ==e1:
        if test == e2:
            print(f"both payment-service and auth-service are occurring for sametime ie {test}")
        elif test == e3:
            print(f"both payment-service and order-service are occurring for sametime ie {test}")
        elif test == e4:
            print(f"both payment-service and inventory-service are occurring for sametime ie {test}")
        elif test == e5:
            print(f"both payment-service and notification-service are occurring for sametime ie {test}")
        else:
            print(f"Most problematic service: payment-service error count is :{test}")
    elif test ==e2:
        if test == e1:
            print(f"both payment-service and auth-service are occurring for sametime ie {test}")
        elif test == e3:
            print(f"both auth-service and order-service are occurring for sametime ie {test}")
        elif test == e4:
            print(f"both auth-service and inventory-service are occurring for sametime ie {test}")
        elif test == e5:
            print(f"both auth-service and notification-service are occurring for sametime ie {test}")
        else:
            print(f"Most problematic service: auth-service error count is :{test}")
    elif test ==e3:
        if test == e2:
            print(f"both order-service and auth-service are occurring for sametime ie {test}")
        elif test == e1:
           print(f"both order-service and payment-service are occurring for sametime ie {test}")
        elif test == e4:
            print(f"both order-service and inventory-service are occurring for sametime ie {test}")
        elif test == e5:
            print(f"both order-service and notification-service are occurring for sametime ie {test}")
        else:
            print(f"Most problematic service: order-service error count is :{test}")
    elif test ==e4:
        if test == e2:
            print(f"both inventory-service and auth-service are occurring for sametime ie {test}")
        elif test == e3:
            print(f"both inventory-service and order-service are occurring for sametime ie {test}")
        elif test == e1:
            print(f"both payment-service and inventory-service are occurring for sametime ie {test}")
        elif test == e5:
            print(f"both inventory-service and notification-service are occurring for sametime ie {test}")
        else:
            print(f"Most problematic service: inventory-service error count is :{test}")
    elif test ==e5:
        if test == e2:
            print(f"both notification-service and auth-service are occurring for sametime ie {test}")
        elif test == e3:
            print(f"both notification-service and order-service are occurring for sametime ie {test}")
        elif test == e4:
            print(f"both notification-service and inventory-service are occurring for sametime ie {test}")
        elif test == e1:
            print(f"both notification-service and payment-service are occurring for sametime ie {test}")
        else:
            print(f"Most problematic service: notification-service error count is :{test}")

def service_health(logs):
    lines=logs.splitlines()
    e1=e2=e3=e4=e5=0
    for line in lines:
        if "payment-service error" in line :
            e1+=1
        elif "auth-service error" in line:
            e2+=1
        elif "order-service error" in line:
            e3+=1
        elif "inventory-service error" in line:
            e4+=1
        elif "notification-service error" in line:
            e5+=1
    print(f'''
payment-service       : {clasify(e1)}
auth-service          : {clasify(e2)}
order-service         : {clasify(e3)}
inventory-service     : {clasify(e4)}
notification-service  : {clasify(e5)}
''')

def critical(logs):
    lines=logs.splitlines()
    i=w=e=score=0
    for line in lines:
        if "payment-service" in line:
            if "info" in line:
                i+=1
            elif "warning" in line:
                w+=1
            elif "error" in line:
                e+=1
            score=(1*0)+(w*1)+(e*2)
            if score>6:
                print("Payment-service status : CRITICAL")
                score=0
            elif score>=1:
                print("Payment-service : WARNING")
                score=0
            else:
                print("Payment-service : Healthy")
                score=0
        if "auth-service" in line:
            if "info" in line:
                i+=1
            elif "warning" in line:
                w+=1
            elif "error" in line:
                e+=1
            score=(1*0)+(w*1)+(e*2)
            if score>=6:
                print("Auth-service status : CRITICAL")
                score=0
            elif score>=1:
                print("Auth-service : WARNING")
                score=0
            else:
                print("Auth-service : Healthy")
                score=0
        if "order-service" in line:
                    if "info" in line:
                        i+=1
                    elif "warning" in line:
                        w+=1
                    elif "error" in line:
                        e+=1
                    score=(1*0)+(w*1)+(e*2)
                    if score>6:
                        print("order-service status : CRITICAL")
                        score=0
                    elif score>=1:
                        print("order-service : WARNING")
                        score=0
                    else:
                        print("Order-service : Healthy")
                        score=0
        if "inventory-service" in line:
                    if "info" in line:
                        i+=1
                    elif "warning" in line:
                        w+=1
                    elif "error" in line:
                        e+=1
                    score=(1*0)+(w*1)+(e*2)
                    if score>6:
                        print("inventory-service status : CRITICAL")
                        score=0
                    elif score>=1:
                        print("Inventory-service : WARNING")
                        score=0
                    else:
                        print("Inventory-service : Healthy")
                        score=0
        if "notification-service" in line:
                    if "info" in line:
                        i+=1
                    elif "warning" in line:
                        w+=1
                    elif "error" in line:
                        e+=1
                    score=(1*0)+(w*1)+(e*2)
                    if score>6:
                        print("notification-service status : CRITICAL") 
                        score=0
                    elif score>=1:
                        print(" Notification-service : WARNING")
                        score=0
                    else:
                        print("Notification-service : Healthy")
                        score=0       
lo = """
2026-09-10 09:00:01 payment-service INFO Payment request received
2026-09-10 09:00:02 payment-service INFO Payment validated
2026-09-10 09:00:03 payment-service ERROR Payment gateway timeout
2026-09-10 09:00:04 auth-service INFO User authentication successful
2026-09-10 09:00:05 order-service error Order processing delayed
2026-09-10 09:00:06 payment-service ERROR Payment retry failed
2026-09-10 09:00:07 inventory-service INFO Stock updated
2026-09-10 09:00:08 notification-service ERROR Email delivery failed
2026-09-10 09:00:09 order-service error Order completed
""".lower()
print("the basic structure of filling logs is \n",lo)
print("after filling use cltl+z and then press ENTER")
logs = sys.stdin.read().lower()
print('''========================================
     PRODUCTION INCIDENT ANALYZER
========================================

1. Show summary
2. Show service statistics
3. Show error logs
4. Search logs
5. Show service health
6. Show critical incidents
7. Exit''')
choice=int(input("enter your chice"))
while True:
    match choice:
        case 1:
            print(basic_stats(logs))
        case 2:
            print(service_stats(logs))
        case 3:
            print(error_logs(logs))
        case 4:
            print("still in development")
        case 5:
            print(service_health(logs))
        case 6:
            print(critical(logs))
        case 7:
            break
