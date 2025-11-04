# key and value unordered seq  and mutable
human1 = {'height':120 , 'weight' : 80 , 'age':21 , 'eye-color': 'blue'}

print(human1.items())
print(human1.keys())
print(human1.values())
print(human1.__len__())


human1['age']  = 22 
print(human1['age'])


s = set(human1)
print(s)

s = set(human1.values())
print(s)

human1 = {'height':120 , 'weight' : 80 , 'age':21 , 'eye-color': 'blue' , 'lang':['arabic' , 'english']}
print(human1['lang'][0])


humans = {1:human1 ,
           2: {'height':120 ,'weight' : 80 , 'age':21 , 'eye-color': 'blue' , 'lang':['arabic' , 'english']} ,
           3: {'height':142 ,'weight' : 90 , 'age':2 , 'eye-color': 'red' , 'lang':['arabic' , 'english']} ,
           4: {'height':34 ,'weight' : 190 , 'age':109 , 'eye-color': 'white' , 'lang':[]} ,
           5: {'height':78 ,'weight' : 39 , 'age':24 , 'eye-color': 'green' , 'lang':['arabic' , 'english']} ,
                            }

print(humans[1])
print(humans[4])