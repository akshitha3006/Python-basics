basket1={"Banana","Mango","Kiwi","Apple","Orange","Kiwi","Banana","Mango","Grapes"}
basket2={"Strawberry","Mango","Grapes","Kiwi","Banana","Strawberry","Lichi","Apple","Mango"}
basket1.add("Pineapple")
basket=basket1.intersection(basket2)
print(basket)

import array as arr
basket3=arr.array("i",[2,3,1,7,3,2,7,6,4,5,6,8,6,9,3,5,4,8,5,6])
basket3.append(7)
basket3.insert(1,1)
print(basket3)

print(basket3.count(6))
basket3.reverse()
print(basket3)
