#字符串拼接的多种方式


#python2.x 使用raw_input() python3.x使用input
#python2.x中也有input，但是输入什么类型就是什么类型，比如zhang，不加引号，则认为zhang是一个变量，如果加了引号则就是"zhang"
name = input('name:')
age = int(input('age:'))
job = input('job:')
salary = input('salary:')
print(type(salary))

#方式一
info1 = '''
---------info of '''+name+'''--------
name:'''+name+'''
age:'''+str(age)+'''
job:'''+job+'''
salary:'''+salary+'''
'''


#方式二
#可以使用%d表示数字，使用%f表示浮点型数字，但是如果使用%d则默认接收的都是字符串，需要int进行强转
info2 = '''
---------info of %s--------
name:%s
age:%d
job:%s
salary:%s
''' % (name,name,age,job,salary)

#方式三
info3 = '''
---------info of {_name}--------
name:{_name}
age:{_age}
job:{_job}
salary:{_salary}
'''.format(_name=name,_age=age,_job=job,_salary=salary)


#方式四
info4 = '''
---------info of {0}--------
name:{0}
age:{1}
job:{2}
salary:{3}
'''.format(name,age,job,salary)

print(info4)