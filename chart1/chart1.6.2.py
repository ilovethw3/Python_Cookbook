from collections import defaultdict
emp = {'name':'Tom', 'age':20,  'salary' : 8800.00}
print(emp.items())
d=defaultdict(list)
for key,value in emp.items():
    d[key].append(value)

print(d)