# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

import random

num=random.randint(1,10)
#print(num)
while True:
    ans=input('give me a number(1~10):')
    ans=int(ans)
    if num==ans:
        print('yes')
        break
