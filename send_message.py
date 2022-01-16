# from importlib.resources import path
from datetime import datetime
import pywhatkit
import pyautogui 


class Send_Message():
    def __init__(self,text,number=''):
        self.text = text 
        self.number = number
    
    def send_msg(self):
        pywhatkit.sendwhatmsg_instantly(self.number,self.text)
        pyautogui.press('enter',2,2)
    
    def send_group(self,id,hour,min):
        pywhatkit.sendwhatmsg_to_group(id,self.text,hour,min)
        pyautogui.press('enter',2,2)
    
    def send_image(self,path):
        pywhatkit.sendwhats_image(self.number,path,self.text)
        pyautogui.press('enter',2,2)

while True:
    try: 
        print("1. You want to send message for person (press '1')\n"
              "2. You want to send message for group (press '2')\n"
              "3. You want to send image for person (press '3')")
        var = int(input("Enter the number :"))
        break

    except Exception:
        print("invalid input,'Try again\n")

if var == 1:
    word = input("Enter the message to send: ")
    length = input("Enter the phone number to send message like this format(+918898898878): ")
    Send_Message(word,length).send_msg()

elif var == 2:
    word = input("Enter the message to send : ")
    group_id =input("enter the group id :")
    hour= datetime.now().strftime('%H')
    min = int(datetime.now().strftime('%M')) + 1 
    Send_Message(word).send_group(group_id,hour,min)

elif var == 3:
    word = input("Enter the message to tag in image : ")
    path = input("Enter the Path for image like('C:\\Users\\Hacker\\path\\path\\hi.png') : ")
    Send_Message(word).send_image(path)    
else:
    print("You Entered wrong option.Try again!")


