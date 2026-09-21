import sys

def clasify(a):
    if a==0:
        return "HEALTHY"
    elif a >= 1 and a<=4:
        return "WARNING"
    elif a>=5:
        return "CRITICAL" 

def basic_stats(logs):    
    errorline=warningline=infoline=count=0
    print("the basic format ")
    words=logs.split()
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
      The total character in the ord are : {len(logs)}
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
    notification+payment+auth+order+inventory
    print(f'''
     total words           :  {len(words)}
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
    p=[]
    a=[]
    o=[]
    i=[]
    n=[]
    isc=esc=wsc=pscore=ascore=oscore=iscore=nscore=0
    lines=logs.splitlines()
    for line in lines:
        if "payment-service" in line:
            p.append(line) 
        elif 'auth-service' in line:
            a.append(line)
        elif 'order-service' in line:
            o.append(line) 
        elif 'inventory-service' in line:
            i.append(line)
        elif 'notification-service' in line:
            n.append(line)
    for p1 in p:
        if 'info' in p1:
            isc+=1
        elif 'error' in p1:
            esc+=1
        elif 'warning' in p1:
            wsc+=1
    pscore=(isc*0)+(esc*2)+(wsc*1)
    print(f"payment-service :  {clasify(pscore)}")
    isc=esc=wsc=0
    for a1 in a:
        if 'info' in a1:
            isc+=1
        elif 'error' in a1:
            esc+=1
        elif 'warning' in a1:
            wsc+=1
    ascore=(isc*0)+(esc*2)+(wsc*1)
    print(f"auth-service :  {clasify(ascore)}")
    isc=esc=wsc=0
    for o1 in o:
        if 'info' in o1:
            isc+=1
        elif 'error' in o1:
            esc+=1
        elif 'warning' in o1:
            wsc+=1
    oscore=(isc*0)+(esc*2)+(wsc*1)
    print(f'order-service :  {clasify(oscore)}')
    isc=esc=wsc=0
    for i1 in i:
        if 'info' in i1:
            isc+=1
        elif 'error' in i1:
            esc+=1
        elif 'warning' in i1:
            wsc+=1
    iscore=(isc*0)+(esc*2)+(wsc*1)
    print(f'inventory-service : {clasify(iscore)}')
    isc=esc=wsc=0
    for n1 in n:
        if 'info' in n1:
            isc+=1
        elif 'error' in n1:
            esc+=1
        elif 'warning' in n1:
            wsc+=1
    nscore=(isc*0)+(esc*2)+(wsc*1)
    print(f' notification-service : {clasify(nscore)}')
    isc=esc=wsc=0   

print("after filling use cltl+z and then press ENTER")
logs = logs = """
2026-09-10 09:00:01 payment-service INFO Payment request received
2026-09-10 09:00:02 payment-service INFO Payment validated
2026-09-10 09:00:03 payment-service ERROR Payment gateway timeout
2026-09-10 09:00:04 auth-service INFO User authentication successful
2026-09-10 09:00:05 order-service WARNING Order processing delayed
2026-09-10 09:00:06 payment-service ERROR Payment retry failed
2026-09-10 09:00:07 inventory-service INFO Stock updated
2026-09-10 09:00:08 notification-service ERROR Email delivery failed
2026-09-10 09:00:09 order-service INFO Order completed
""".lower()
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
while True:
    choice=input("enter your chice ")
    match choice:
        case 1:
            basic_stats(logs)
        case 2:
            service_stats(logs)
        case 3:
            error_logs(logs)
        case 4:
            print("still in development")
        case 5:
            service_health(logs)
        case 6:
            critical(logs)
        case 7:
            break
        case _:  # Default case if no other patterns match
            print("wrong input")

