import pickle

a = {" name ": "Tom", "age": "40"}

with open('text.txt', 'wb') as file:
    pickle.dump(a, file)

with open('text.txt', 'rb') as file2:
    b = pickle.load(file2)

with open(r'F:\make_python3\moudle\applications\challenges\banner.p', 'rb') as file3:
    data = pickle.load(file3)
print(type(b))
print(b)
print(data)