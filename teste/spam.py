from  pyautogui import spam
from time import  sleep
limite_msg=input('Enter n de msgs: ')
msg=int(input('Coloque a msg: '))
i=0
sleep(2)
while i<int(limite_msg):
    spam.typewrite(msg)
    spam.prees('enter')
i +=1    