# import datetime
# parson_banckar={
#     'Name':'rakiba yesmin',
#     'education':'BA',
#     'CGPA':'second class',
#     'experians':'one year',
#     'marrid':'marrid',
#     'selary':25000,
#     'joinig date':datetime.datetime.now()

# }
# parson_banckar['tmie']='10am and 4pm'
# parson_banckar['address']='bogura'
# parson_banckar['selary']=24000
# if 'selary' in parson_banckar:
#     print('selary ase')
# elif 'addrss' in parson_banckar:
#     print('address ase')
# else:
#     print('nai')

# teacher={
#     'name':'fahima akter',
#     'education':'BBA',
#     'subject':'bangla',
#     'joinig':'1-2-2015',
#     'selary':11000,
#     'year':2023
# } 
# teacher1=dict(teacher)
# print(teacher1)
    
# list1={
#     'name':'fahima akter',
#     'education':'BBA',
#     'joing':'1-2-15'
# }
# list2={
#     'name':'jafrin sultana',
#     'education':'MMC',
#     'joing':'2-4-13'
# }
# list3={
#      'name':'rebeka sultana',
#      'education':'BSC',
#      'joing':'5-3-17'
# }
# teacher={
#     'list1':list1,
#     'list2':list2,
#     'list3':list3
# }
# print(teacher)
# # for x,obj in teacher.items():
#     print(x)
#     for y in obj:
#         print(y+':',obj[y])
# a=[12,20,33,40,45]
# b=0
# for x in a:
#     if x >20:
#         b+=x
# print(b)
# def perason (**name):
#     print('he is honest man ' + name['name1'] )
# perason(name1='rakiba',name2='jannati',name3='rakibul')

# def name (list):
#     for x in list:
#         print(x)
# list=['alu','piyaj','lau']
# name(list)

# list={
#     'name':'rakiba yesmin',
#     'eduction':'HSC',
#     'CGPA':'4.35'

   
# }
# list['date of brith']='20-08-2000'
# for x,y in list.items():
#     print(x,':', y)

# def name(name1,name2,name3):
#     return f'he is honest {name3}'
# a=name(name1='morshed',name2='jannati',name3='rakiba')
# print(a)

# thisdict= dict(name='rakiba yesmin',age=25,cunntry='bangladesh')
# print(type(thisdict))
student={
    'list':{
    'name':'jemi akter',
    'roll':3,
    'class':'ten'
    },
    'list1':{
        'name':'rakiba yesmin',
        'roll':7,
        'class':'nine'

    }
}
print(student)