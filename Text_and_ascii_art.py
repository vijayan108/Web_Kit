import pywhatkit


while True:
    try: 
        print("1. You want to change Image to ascii art (press '1')\n"
              "2. You want to change text to handwritten image (press '2')\n"
              "3. You want to shutdown the system (press '3')")
        var = int(input("Enter the number :"))
        break

    except Exception:
        print("invalid input,'Try again\n")
if var == 1:
    path = input("Enter the Path for image like('C:\\Users\\Hacker\\path\\path\\hi.png') :")
    output = input("Enter a filename to save for output file like('hello') : ")
    pywhatkit.image_to_ascii_art(path,output)
elif var == 2:
    path = input("enter the text that change to handwritten: ")
    output = input("Enter a filename to save for output file like('hello.png') : ")
    pywhatkit.text_to_handwriting(path,output,(0,0,136))
elif var == 3:
    time = input("Enter the number of seconds to shutdown: ")
    pywhatkit.shutdown(time)