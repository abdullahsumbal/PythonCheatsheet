# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
nums = [1,2,3,4,5]
print(all(x % 2 == 0 for x in nums) )
print(any([x % 2 == 0 for x in nums]) )



s = "a=b=c"
x = s.split("=", 6)
print(x)   # 'a'
