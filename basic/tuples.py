# tuple is Immutable list  (can't change)
dimensions = (200 , 50 , 100)
print(dimensions[1])
print(dimensions.count(200))
print(dimensions.index(200))


misc_d = (14 ,'ab' , (9,2) , [1,2,3] , {'def':12})
for index , value in enumerate(misc_d):
    print(index , value)