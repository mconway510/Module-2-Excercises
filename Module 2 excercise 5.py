# module 2 excercise 5

rollNumber  = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict  ={'Mike':47, 'Teri':69, 'Kourtney':76, 'Connor':97} 

print("List -", rollNumber)
print("Dictionary - ", sampleDict)

rollNumber[:] = [item for item in rollNumber if item in sampleDict.values()]
print("after removing unwanted elemnts from list ", rollNumber)