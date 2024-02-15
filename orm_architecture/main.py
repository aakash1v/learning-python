import myconnection as ms
import model
import employeeDao as empd

ed = empd.EmployeeDao()

# E1 = model.Employee()

# eid = int(input('Enter employeee id :'))
# ename = input('Enter Emplyee Name :')
# edept= input('Enter department Name :')
# esal = int(input('Enter salary'))

# E1.set_eid(eid)
# E1.set_ename(ename)
# E1.set_edept(edept)
# E1.set_esal(esal)
# ed.insertEmployee(E1)

# Delete code...
# search = int(input('Enter the eid for search :'))
# E = ed.searchEmployee(search)
# if (E==None):
#     print('No record found...')
# else:
#     print("Emp Id :",E.get_eid())
#     print("Emp Name :",E.get_ename())
#     print("Emp Department :",E.get_edept())
#     print("Emp Salary :",E.get_esal())

#     if input('Are u sure wnat to delete (yes/no) ??').lower().startswith('y'):
#         ed.deleteEmployee(search)
#         print('Record Deleted...')
    
# update details...

# E1 = model.Employee()
# eid = int(input('Enter employeee id :'))
# ename = input('Enter Emplyee Name :')
# edept= input('Enter department Name :')
# esal = int(input('Enter salary'))

# E1.set_eid(eid)
# E1.set_ename(ename)
# E1.set_edept(edept)
# E1.set_esal(esal)
# ed.updateEmployee(E1)

# search all 
mylist = ed.searchAll()
print(len(mylist))
for emp in mylist:
    print(emp.get_eid(),end='  ')
    print(emp.get_ename(),end='  ')
    print(emp.get_edept(),end='  ')
    print(emp.get_esal())