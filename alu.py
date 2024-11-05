# # # mylist=[1,9,12,567,123]
# # # # for x in range(len(mylist)):
# # # #     print(mylist[4])



# # # list=[]
# # # for x in range(len(mylist),0,-1):
# # #     list.append(mylist[x-1])
# # #     # print(mylist[x-1])

# # # print(list)

# # # list=[11,22,33,44,55,66]
# # # mylist=[]
# # # for x in range(len(list),0,-1):
# # #     mylist.append(list[x-1])
# # # print(mylist)
# # # for x in range(20):
# # #     if x%3==0 and x%5==0:
# # #      print(x)
# # # sum=0
# # # for x in range(1,16): 
# # #     sum=sum+x
# # # print(sum)
# list=[1,2,3,4,5]
# sum=[]
# for x in range(len(list),0,-1):
#     sum.append(list[x-1])
# print(sum)


# # mylist=[9,7,12,14,34,15,22,33,77]
# # total_even=0
# # total_odd=0
# # evenlist=[]
# # oddlist=[]

# # for x in mylist:
# #     if x %2==0:
# #         total_even=total_even+1
# #         evenlist.append(x)
# #     if x%2==1:
# #         total_odd=total_odd+1
# #         oddlist.append(x)
# # print("even",evenlist,"\nodd",oddlist)
# # mylist=['apple','orange','banana'] 
# # for x in mylist:
# #    
# # print(x)
# # if 'apple' in mylist:
# #     mylist.remove('apple')

# #     print(mylist)
# # else:
# #     print('nai')


# # 
# # thistuple = ("apple", "banana", "cherry")
# # y = list(thistuple)
# # y.append("orange")
# # thistuple = tuple(y)
# # print(thistuple)
# # thistuple = ("apple", "banana", "cherry")
# # y = ("orange",)
# # thistuple += y

# # print(thistuple)
# # list['a','b','c']
# # a=[]
# # for x in range(len(list),0,-1):
# #     a .append(list[x-1])
# # print(a)

# # fruits = ("apple", "banana", "cherry",'lau')
# # (green, yellow, *red) = fruits

# # print(green)
# # print(yellow)
# # print(red)

# # a=(50,60,70,40)
# # b=list(a)
# # b[0]=80
# # b[3]=90

# # a=tuple(b)
# # for x in a:
# #     print(x)
# t=('a','b','c','d')
# t1=t
# del t
# print(t1)

# t1=(1,2,3,4)
# t2=(5,6)
# t3=t1+t2
# print(t3)

# t=(10,20,30,40,50)
# x=list(t)
# x.remove(10)
# x.remove(20)
# t=tuple(x)
# print(t)

# a=(100,200,300)
# b=list(a)
# b.reverse()
# a=tuple(b)
# print(a)
# a=200
# b=200
# if a<b:
#     print('b a theke boro')
# elif a>b:
#     print('a theke b soto')
# else:
#     print('a and b soman')


# num=[1,2,3,]
# num1=[4,5,6]
# num2=num+num1
# num3=1
# for x in num2:
#     num3=num3*x
#     print(num3)

# a=[1,2,2,3,4,4,5]
# b=0
# c=0
# d=[]
# for x in a:
#     if x==2:
#         b=b-2
#     if x==4:
#         c=c-4
    
# print(x)



# # fruits=['apple','banana','mango','orange']
# # fruits.reverse()
# # print(fruits)

# # a=(1,2,3)
# # b=(4,5,6)
# # c=a+b
# # print(c)

# my_tuple=(10,20,30,10,40,10)
# y=0
# for x in my_tuple:
#     if x==10:
#         y=y+1
# print(y)

# num=(3,5,1,9,6)
# num1=8
# num2=2
# for x in num:
#     if x>num1:
#      print(x)
#     else:
#        x<num2
# print(x)


# my_tupel=(10,20,30)
# mylist=list(my_tupel)
# print(mylist)

# set2={1,2,3,}
# set1=list(set2)
# set1.remove(2)
# set2=set(set1)
# set2.add(4)
# print(set2)

# num={10,20,30,40}
# sums=0
# for x in num:
#     sum =sum+x
# print(sum)
# 

# set={1,2,3,4}
# set1={3,4,5,6}
# comon=set.intersection(set1)
# uncomon=set.symmetric_difference(set1)
# print(comon)
# print(uncomon)


# a={1,2,3,4,5}
# b={2,3,4,6}
# c=a&b
# print(c)


# a=[1,2,3,4,2,3]
# b=[]
# for x in a:
#     if x not in b:
#         b.append(x)
# print(b)

# a=[10,20,30,40,50]
# sum=0
# c=(len(a))
# for x in a:
#     sum=sum+x
    
# print(sum/c)

# a=['banana','mango','orange']
# b=[]
# for x in a: 
#     if x=='mango' :
#         continue
#     b.append(x)
    
# print(b)


# a=500
# if a<700:
#     print('b theke a soto')
# elif a==500:
#     print('a and b equal1')
# else:
#     print('a and b soman')
# a=120
# b=290
# print('boro') if a>b else('b soto')plm ta sulve korte hobe
# a=10
# b=10
# print('a soto')if a<b else print('soman') if a==b else print ('na')


# a=110
# b=25
# c=40
# if a<b and c>b:

#     print('yes true')
# else:
#     print('no false')
# a=23
# b=250
# c=30
# if a>b or b<c:
#     print('yes condition is true')
# else:
#     print('no conditoin is false')
# a=130
# b=1300
# if not a<b:
#     print(' a is greater than b')
# elif  not a==b:
#     print('yes equal')


# a=41
# if a>220:
#     print('yes a boro')
# elif a<6:
#     print('yes a soto')
# else:
#     print('no')
