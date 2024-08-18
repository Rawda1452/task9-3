def remove(list1, remove_num):
    return [num for num in list1 if num != remove_num]

def main():
    user= input("Enter: ")
    numbers = list(map(int, user.split()))
    remove_num = int(input("what is th number you want to remove?? "))
    x= remove(numbers, remove_num)
    print("remaining :",x)
main()