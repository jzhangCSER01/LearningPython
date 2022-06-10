'''
列表实现队列功能
'''

# example
itname = []
import time
# add the interview name
while(1):
    newname = input('Enter the name of waiting for the Interview(if end, enter end):')
    if(newname == 'end'):
        break
    else:
        itname.append(newname)
# In front of the row of people to interview first
while(len(itname) > 0):
    name = itname.pop(0)
    print('%s take the interview' %name)
    time.sleep(5)   # wait for 5 seconds