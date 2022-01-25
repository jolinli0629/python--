# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

math=input('數學成績')
math_new=int(math)
eng=input('英文成績')
eng_new=int(eng)

if math_new>=90 and eng_new>=90:
    print('有獎品')

if math_new<60 and eng_new<60:
    print('要處罰')


