# class phone:
#     brand='vivo'
#     model='s28'
#     color='black'
#     price=28000
#     feater=['camara','phone book','email']
#     def vedio_call(self,x,y):
#         print(x+y)
        
# mylist=phone()
# mylist.vedio_call(12,12)
# print(mylist)

# class celculetor:
#     name='cesio'
#     def puls(s,x,y):
#         print(x+y)
#     def minas(s,x,y):
#         print(x-y)
#     def multpul(s,x,y):
#         print(x*y)
#     def mudulas(s,x,y):
#         print(x/y)
# a=celculetor()
# a.puls(12,2)
# a.minas(23,1)
# a.mudulas(13,5)
# a.mudulas(33,11)

class phone:
    def __init__(self,barnd,model,price):
        self.barnd=barnd
        self.model=model
        self.price=price
myphone=phone('vivo','s28',20000)

print('brand'':',myphone.barnd,'\nmodel'':',myphone.model,'\nprice'':',myphone.price)

yourphone=phone('oppo','x11',24000)
print('barnd'':',yourphone.barnd,'\nmodel'':',yourphone.model,'\nprice'':',yourphone.price)
    


