## customer management system:
# 1=Add Customer
# 2=Search Customer
# 3=Delete Customer
# 4=Modify Customer
# 5=Display All Customers

id_list=[]
name_list=[]
age_list=[]
mo_no_list=[]
state_list=[]
pin_code_list=[]
print("CUSTOMER MANAGEMENT SYSTEM")
choice=input("1.add cutomer\n2.search customer\n3.delete cutomer\n4.update cutomer\n5.display all customer\nenter your choice:")
#add customer
if(choice=="1"):
    cust_id=input("enter customer id:")
    cust_name=input("enter customer name:")
    cust_age=int(input("enter customer age:"))
    cust_mobile=input("enter customer mobile no:")
    cust_state=input("enter cutomer state:")
    cust_pin_code=int(input("enter your area pin code:"))
    id_list.append(cust_id)
    name_list.append(cust_name)
    age_list.append(cust_age)
    mo_no_list.append(cust_mobile)
    state_list.append(cust_state)
    pin_code_list.append(cust_pin_code)
    print("cust_id:",id_list)
    print("cust_name:", name_list)
    print("cust_age:", age_list)
    print("cust_mobile:", mo_no_list)
    print("cust_state:", state_list)
    print("cust_pin_code:", pin_code_list)

#saerch customer
if(choice=="2"):
    id=int(input("enter customer id which you want to search:"))
    i=id_list.index(id)         #let id:10,i=1
    if(id in id_list):
        print("cust id:",id_list[i])
        print("cust name:",name_list[i])
        print("cust name:", age_list[i])
        print("cust name:", mo_no_list[i])
        print("cust name:",state_list[i])
        print("cust name:", pin_code_list[i])
    else:
        print("id not found in list")


#delete customer
if(choice=="3"):
    id=int(input("enter customer id which you want to delete:"))
    i=id_list.index(id)
    if(id in id_list):
        id_list.pop(i)
        name_list.pop(i)
        age_list.pop(i)
        mo_no_list.pop(i)
        state_list.pop(i)
        pin_code_list.pop(i)
        print("cust id:", id_list[i])
        print("cust name:", name_list[i])
        print("cust age:", age_list[i])
        print("cust mobile:", mo_no_list[i])
        print("cust state:", state_list[i])
        print("cust pin code:", pin_code_list[i])

#update customer
if(choice=="4"):
    id=int(input("enter customer id which you want to modify:"))
    i = id_list.index(id)
    if(id in id_list):
        upadate_name=input("enter updated name:")
        upadate_age = input("enter updated age:")
        upadate_mobile = input("enter updated mobile no:")
        upadate_state = input("enter updated state:")
        upadate_pin = input("enter updated pin code:")
        name_list[i]=upadate_name
        age_list[i]=upadate_age
        mo_no_list[i]=upadate_mobile
        state_list[i]=upadate_state
        pin_code_list[i]=upadate_pin
        print(id_list,name_list,age_list,mo_no_list,state_list,pin_code_list)

#display all customer

if(choice=="5"):
    print("cust id:", id_list)
    print("cust name:", name_list)
    print("cust name:", age_list)
    print("cust name:", mo_no_list)
    print("cust name:", state_list)
    print("cust name:", pin_code_list)









