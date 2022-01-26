# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

import random
num=random.randint(1,20)

i=1
while i<6:
    ans=input('輸入1~20的數字:')
    ans=int(ans)
    if num==ans:
        print('yes')
        anser = input('是否繼續遊玩?:')
        break
    elif num<ans:
        print('太大')
    else:
        print('太小')
    i=i+1
    if i==6 and num!=ans:
        print('你輸了')
        anser=input('是否繼續遊玩?:')
        if True:
            print('你玩了5次')

