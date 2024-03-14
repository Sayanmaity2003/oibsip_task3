import string
import random
if __name__ == "__main__":
    s1 = string.ascii_letters
    s3 = string.digits
    s4 = string.punctuation
    s = []
    print("------------Simple Password Generator-----------")
    pl = int(input("Enter the password length: "))
    print("----------Password character types are---------")
    print("1.Letters\n2.Numbers\n3.Symbols")
    typ = int(input("Choose password character type: "))
    if(typ==1):
        s.extend(list(s1))
    elif(typ==2):
        s.extend(list(s3))
    elif(typ==3):
        s.extend(list(s4))
    else:
        print("Choose valid character!!!")
    print("Your Password is: ")
    print("".join(random.sample(s,pl)))