def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)

def factorial_recursive(n):
    my_name = 'marcelo'

def another_function():
    pass

print(factorial_recursive(2))

from sys import argv

script, filename = argv

txt = open(filename)
print(f"here is your file {filename}:")
print(txt.read())

print("type the filename again:")
file_again = input("> ")

txt_again = open(file_again)


print(txt_again.read())

d = {}

def setdefault(k,v):
    if k not in d:
        d[k] = v
        return v

#dict.setdefault(key, default=None)  # key is key to be searched...default is return in case key is not found
dict = {"Name": "Zara", 'age': 7}
print("value : %s " % dict.setdefault("age", None))
print("value : %s " % dict.setdefault("sex", None))

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

dict = {'Name': 'Zara', 'Sex': 'M', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Sex']: ", dict.setdefault('Class', 'default'))

def twoSum(nums, target):
        dict = {}
        for i in range(len(nums)):
            if target-nums[i] not in dict:
                print(target-nums[i])
                #dict[nums[i]] = i
                dict.setdefault(nums[i], []).append(i)
            else:
                return [dict[target-nums[i]], i]
                
nums = [2,7,5,8]
print(twoSum(nums, 10))
