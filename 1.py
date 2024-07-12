# try:
#     a = input("Enter your number")
#     if a<0:
#         raise ValueError("cant be negative")
#     fact = 1
#     for i in range:
#         fact *=  i 
#         print(f"Fact {a} is {fact}")    
# except ValueError:
#     print(f"Incorecct input ")


def factNum(num):
    fact = 1
    for i in range(1,num,+1):
        fact *= i
    return fact
try:
    num = input("Enter your number")
    if num < 0:
        raise ValueError("Number cant be negative")
    result = factNum(num)
    print(f"Fact {num} is {result}")
except ValueError :
    print(f"Incorrect input ")


list = [] 
print("Enter a number "b"")
try:

    user = input()
    if user.lower() == "b":
      
     num = int(user)
    list.append(num)
except ValueError:
    print("Enter a num finish")





