#Module 2 Excercise 3
#Module 2 Excercise 3
ListOne = [3, 6, 9, 12, 15, 18, 21] #first provided list
listTwo = [4, 8, 12, 16, 20, 24, 28] #second provided list
listThree = list() #my new list

#Define Odd Index 
oddElements = listOne[1::2]

#Define even Index
EvenElement = listTwo[0::2]

#Print new list
print("List 3")
listThree.extend(oddElements)
listThree.extend(EvenElement)
print(listThree)