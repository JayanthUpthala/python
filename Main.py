from Employee import Employee
#final_pay=['Eid' + '\t' + 'lastname' + '\t' + 'base_pay' + '\t' + 'overtime_rate' + '\t' + 'total_pay' + '\t']
final_pay=[]
with open('Employee_Hours', mode='r') as file:
    emp_pay=file.readlines()
    employee=[]
    for i in emp_pay:
        i=i.strip('\n')
        emp_details=i.split(',')
        print(emp_details)
        cal_emp=Employee(emp_details[0], emp_details[1], emp_details[2], emp_details[3], emp_details[4], emp_details[5], emp_details[6])
        #emp_pay=cal_emp.__str__()
        #emp_list=cal_emp.__repr__(emp_pay)
        base_pay=cal_emp.base_pay()
        overtime_pay=cal_emp.overtime_pay()
        total_pay=cal_emp.total_pay()
        final_pay.append(emp_details[0] + ',' + emp_details[2] + ',' +
        str(base_pay) + ',' + str(overtime_pay) + ',' + str(total_pay) + '\n')
        employee.append(cal_emp)
    employee.sort(key=lambda x: x.lastname)
    print(employee)
with open('Employee_pay_list', mode='w') as file1:
    file1.writelines(final_pay)