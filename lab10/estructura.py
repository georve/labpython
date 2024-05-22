employee = [{
    "name" : "Georman Calderon",
    "phone" : "663327958" ,
    "age" : 45
},
{
    "name" : "Andry Calderon",
    "phone" : "663327958" ,
    "age" : 40
},
{
    "name" : "Dayana Calderon",
    "phone" : "663327958" ,
    "age" : 38
}]

print(employee)

print("insert a new user")
name = input("What is your name? ")
phone  = input("What is your Phone? ")
age  = input("What is your age? ")

employee.append({"name":name,"phone":phone,"age":age})
for i in range(len(employee)):
   print(employee[i].get('name'))
   
   
for empliy in employee:
   print ( f"{empliy['name']}|{ empliy['phone'] }|{ empliy['age']}") 