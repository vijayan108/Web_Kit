# Web_Kit.py
import pywhatkit

class Search():
    def __init__(self,text,value=0,):
        self.text = text
        self.value = value

    def Wiki(self):
       dar = pywhatkit.info(self.text,self.value)
       return dar
     
    def google_search(self):
        pywhatkit.search(self.text)
    
    def youtube_search(self,source):
        # print(source)
        if source == 'yes':
           # print(self.text)
            pywhatkit.playonyt(self.text,True)
        elif source == 'no':
            pywhatkit.playonyt(self.text,False)
        else:
            print("funny right!")

while True:
    try: 
        print("1. You want to search in wikipedia (press '1')\n"
              "2. You want to search in google (press '2')\n"
              "3. You want to serach in youtube (press '3')")
        var = int(input("Enter the number :"))
        break

    except Exception:
        print("invalid input,'Try again\n")

if var == 1:
    word = input("Enter the word to search in wikipedia: ")
    length = input("Enter a number of lines you need from your search :")
    wiki = Search(word,length)
    print(wiki.Wiki())
elif var == 2:
    word = input("Enter the word to search in google: ")
    Search(word).google_search()
elif var == 3:
    word = input("Enter the Word to search in youtube: ")
    account = input("Type ('yes' or 'no') to use your account : ")
    Search(word).youtube_search(account)
else:
    print("You Entered wrong option.Try again!")

