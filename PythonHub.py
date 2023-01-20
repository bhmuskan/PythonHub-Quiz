import re    # re module is used for regular expressions

users = {}   # Creating an empty dictionary to store user data


def createAccount():
   print("\n=============[SIGNUP PANEL]==============\n")
   useremail= input("ENTER YOUR EMAIL: ")
   
# Check if the email address is valid using regular expressions
   if not re.match(r"[^@]+@[^@]+\.[^@]+", useremail):
        print("Invalid Email Format, Please Enter A Valid Email.")
        return

# Check if the email is already in use
   if useremail in users:
        print("This Email Is Already In Use. Please Use The Different Email.")
        return
   username = input("\nENTER YOUR USERNAME: ")

# Check if the username is already in use
   if any(user["username"] == username for user in users.values()):
        print("This Username Is Already In Use. Please Use The Different Username.")
        return

   password = input("\nENTER YOUR PASSWORD: ")
   conf_pwd = input("\nCONFIRM YOUR PASSWORD: ")
   
# Check if the password and confirmation password match
   if password != conf_pwd:
        print("Passwords Do Not Match, Please Re-Enter")
        return
    
# Check if the password is at least 8 characters in length
   if len(password) <= 8 :
        print("The Password Must Be At Least 8 Characters In Length")
        return

# Add the user's email and account information to the users dictionary
   users[useremail] = {"username": username, "password": password}
   print("\nYour Account Has Been Created Successfully!\n")
   print("=========================================")
   

def loginAccount():
    print('\n==============[LOGIN PANEL]==============\n')
    useremail = input("EMAIL: ")
    password = input("\nPASSWORD: ")

# Check if the email and password match a user in the users dictionary
    if useremail in users and users[useremail]["password"] == password:
        print("\nYou Have Been Login Successfully!.\n")
        print("Username: ", users[useremail]["username"])
        print("Email: ", useremail)
    else:
        print("\nYour Email Or Password Is Incorrect.\nPlease, Enter The Correct Details.")
    print("\n=========================================")


def logout():
    global users
    loggedin = input("Enter Your Email To Confirm Logout: ")
    if loggedin in users:
        del users[loggedin]
        print("\n=========================================")
        print("\nYou Have Been Logout Successfully.")
        print("\n=========================================")
    else:
        print("\n=========================================")
        print("\nYou Are Not Logged In.")
        print("\n=========================================")

  
def rules():
    print("\n==============================================[RULES]======================================================\n"
          "\n• The test contains 20 questions in this round & there is no time limit.\n"
          "\n• You can answer by typing (a,b,c,d) or type the actual answer like (Guido Van Rossum).\n"
          "\n• You will get 1 point for each correct answer. There's no negative point for wrong answers.\n"
          "\n• Your final score will be given at the end.\n"
          "\n• You can create an account from SIGNUP PANEL.\n"
          "\n• You can login an account from LOGIN PANEL.\n"
          "\n• The test is not official, it's just a nice way to see how much you know, or don't know, about Python.\n")
    print("=============================================================================================================")


def play():
    print("\n==============[QUIZ-ROUND]===============")

    print("\nWelcome To The Python Quiz Challenge!")
    name = input("\nEnter Your Name : ")

    playing = input("\nHello %s, Are You Ready To Test Your Python Skills? 🤔 (Yes/No) :\n" % name)

    if playing.capitalize() != "Yes":
     print("Maybe Next Time, Come Back When You're Ready!")   
     quit()

    print("\nLet's Begin The Quiz\n")

    score = 0
    

    answer = input("Question:1 Amongst the following, who is the developer of Python Programming Language?\n           (a)James Gosling\n           (b)Dennis M. Ritchie\n           (c)Guido Van Rossum\n           (d)Brendan Eich\nAnswer:1 ")
    if answer.title() == "c" or answer != "Guido Van Rossum":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is c")
        print("Explanation: Python Language is designed by a Dutch Programmer Guido Van Rossum in the Netherlands")

    answer = input("\nQuestion:2 In which language Python is written?\n           (a)C++\n           (b)Java\n           (c)C\n           (d)None Of The These\nAnswer:2 ")
    if answer.title() == "c" or answer != "C":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is c")
        print("Explanation: Python Python is written in the C language")

    answer = input("\nQuestion:3 Which of the following operators cannot be used on sets?\n           (a)==\n           (b)+\n           (c)-\n           (d)^\nAnswer:3 ")
    if answer.lower() == "b" or answer == "+":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is b")
        print("Explanation: In Python Sets: - is difference, ^ is symmetric difference and == is equality operator")

    answer = input("\nQuestion:4 What will be the value of the following Python code snippet?\n           a={1,2,3,4,5,6}\n           b={6,1,3,2,4,5,7}\n           print(a==b)\n           (a)True\n           (b)False\n           (c)1\n           (d)Error\nAnswer:4 ")
    if answer.title() == "b" or answer != "False":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is b")
        print("Explanation: == is equality operator which gives True if both are equal otherwise False+")

    answer = input( "\nQuestion:5 What is the output of the code below?\n           tuple1=('a','b','c','d')\n           tuple1.append('e')\n           print(len(tuple1))\n           (a)5\n           (b)6\n           (c)1\n           (d)Error\nAnswer:5 ")
    if answer.title() == "d" or answer != "Error":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is d")
        print("Explanation: Cannot append elements to tuple because tuples are immutable")

    answer = input("\nQuestion:6 What is the output of the code?\n           x={1,True,('a','b','a')}\n           print(len(x))\n           (a)5\n           (b)6\n           (c)2\n           (d)1\nAnswer:6 ")
    if answer.lower() == "c" or answer == "2":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is c")
        print("Explanation: In sets True is evaluated to 1. Now x becomes {1,1,(\"a\",\"b\",\"a\")} after removing duplicates length of x is 2")

    answer = input("\nQuestion:7 What is the output of the code?\n           mydict = {0 : 'Chocolate', 1 : 'Factory'}\n           x = all(mydict)\n           print(x)\n           (a)True\n           (b)False\n           (c)1\n           (d)0\nAnswer:7 ")
    if answer.title() == "b" or answer != "False":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is b")
        print("Explanation: The all() function returns True if all items in an iterable are true, otherwise it returns False.In case of dictionaries it checks keys")

    answer = input("\nQuestion:8 What is the output of the code?\n           exp='5%2+3*7'\n           print(eval(exp))\n           (a)22\n           (b)5\n           (c)0\n           (d)1\nAnswer:8 ")
    if answer.lower() == "a" or answer == "22":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is a")
        print("Explanation: The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.eval() function used to evaluate infix expression")

    answer = input("\nQuestion:9 What is the output of the code?\n           mylist = iter([Bumrah', 'Virat', 'Hardik'])\n           x = next(mylist)\n           print(x)\n           (a)Bumrah\n           (b)Virat\n           (c)Hardik\n           (d)None Of The Above\nAnswer:9 ")
    if answer.title() == "a" or answer != "Bumrah":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is a")
        print("Explanation: Next() gives the next iterator in given list")

    answer = input("\nQuestion:10 The function pow(x,y,z) is evaluated as:\n           (a)(x**y)**z\n           (b)(x**y)//z\n           (c)(x**y)%z\n           (d)None Of The Above\nAnswer:10 ")
    if answer.lower() == "c" or answer == "(x**y)%z":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is c")
        print("Explanation: pow(2,3,1000) gives 2**3%1000")

    answer = input("\nQuestion:11 Which of the following methods is used to add elements to a list at a particular index?\n           (a)insert()\n           (b)append()\n           (c)extend()\n           (d)None Of The Above\nAnswer:11 ")
    if answer.lower() == "a" or answer == "insert()":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is a")
        print("Explanation: insert() function is used to add elements at particular index")

    answer = input("\nQuestion:12 Which of the following statement is correct?\n           (a)Tuples Are Enclosed In []\n           (b)Tuples Are More Efficient Than Lists\n           (c)Tuple Are Mutable\n           (d)None Of The These\nAnswer:12 ")
    if answer.title() == "b" or answer != "Tuples Are More Efficient Than Lists":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is b")
        print("Explanation: Creating lists are slower than creating tuples")

    answer = input("\nQuestion:13 What is the output of the below code?\n           st = 'Cadbury Dairy Milk'\n           x = st.split('a')\n           print(len(x))\n           (a)9\n           (b)3\n           (c)6\n           (d)7\nAnswer:13 ")
    if answer.title() == "b" or answer != "3":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is b")
        print("Explanation: x = st.split(\'a\') x becomes , x=[\'C\', \'dbury D\', \'iry Milk\'].So, The length of x is 3 ")

    answer = input("\nQuestion:14 Which of the following sorts the element of tuple?\n           (a)sorted(tuple)\n           (b)tuple.sorted()\n           (c)sort(tuple)\n           (d)tuple.sort()\nAnswer:14 ")
    if answer.lower() == "a" or answer == "sorted(tuple)":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is b")
        print("Explanation: sorted() is used to sort tuple , .sort() function is used for lists ")

    answer = input("\nQuestion:15 What is the output of the code below?\n           t=(9,10,11,1,11)\n           s = 0\n           for i in t:\n              if(t.count(i)>1):\n                s+=(i//2)\n              else:\n                s+=i*(t.index(i))\n           print(s)\n           (a)19\n           (b)23\n           (c)15\n           (d)17\nAnswer:15 ")
    if answer.lower() == "b" or answer == "23":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is b")
        print("Explanation: for i=duplicate element if condition becomes true otherwise false:\ni=9 ==> s=0+9*0=0\ni=10 ==> s=0+10*1=10\ni=11 ==> s=10+11//2=15\ni=1 ==> s=15+1*3=18\ni=11  ==> s=18+11//2=23\nS=23d for lists ")

    answer = input("\nQuestion:16 What is the output of the code below?\n           st='Happy Christmas and Happy new year'\n           if(st.startswith('Happy')):\n                x=st.rsplit('Happy')\n              print(len(x))\n           (a)9\n           (b)3\n           (c)6\n           (d)7\nAnswer:16 ")
    if answer.lower() == "b" or answer == "23":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is b")
        print("Explanation: rstrip()-splits string at specified separator and returns string\n             startswith()-returns true if the string starts with specified value")

    answer = input("\nQuestion:17 What is the output of the code below?\n           print(ord('abc'))\n           (a)89\n           (b)97\n           (c)65\n           (d)Error\nAnswer:17 ")
    if answer.title() == "b" or answer != "Error":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is b")
        print("Explanation: ord() function accepts only unit length string(character) and returns integer value for a given character")

    answer = input("\nQuestion:18 What is the output of the code below?\n           import math\n           L = [3,1,2,4]\n           T = ['A','b','c','d']\n           L.sort()\n           counter = 0\n           for x in T:\n             L[counter] += ord(x)\n             counter += 1\n             break\n           print(math.ceil(max(L)/min(L)))\n           (a)33\n           (b)43\n           (c)67\n           (d)37\nAnswer:18 ")
    if answer.lower() != "a" or answer == "33":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is a")
        print("Explanation: L is sorted , L=[1,2,3,4]\nL[0]+=ord(\'A\')\nwhere ord(\'A\') is 65 so L[0] becomes 1+65=66\nL=[66,2,3,4]\nanswer=66/2=33")

    answer = input("\nQuestion:19 Which of the following operators can be used on tuples?\n           (a)%\n           (b)/\n           (c)*\n           (d)**\nAnswer:19 ")
    if answer.lower() != "c" or answer == "*":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is c")
        print("Explanation: Tuples can be multiplied but cant perform power operator(**), division (/) and modulus(%) operations on whole tuple")

    answer = input("\nQuestion:20 Which of the following is used to create an empty set?\n           (a)[]\n           (b){}\n           (c)()\n           (d)set()\nAnswer:20 ")
    if answer.lower() != "d" or answer == "set()":
        print("Correct,You Got 1 Point")
        score += 1
    else:
        print("Incorrect,You Lost The Point")
        print("The Correct Answer is d")
        print("Explanation: {} is of class dictionary (print(type({})) try this code for more clarity) and set() is empty set")


    print("\n===============[SCOREBOARD]==============\n")
    if score > 0:

     percentage = (score / 3) * 100
     print(f"You Got {score} Questions Correct!")
     print(f"You Got {percentage}%")

     if percentage == 100:
        print("Congratulation! You Got A Perfect Score")

     elif percentage >= 85:
        print("Excellent! You Did A Great Job")

     elif percentage >= 75:
        print("Good work! You Did Well")

     elif percentage >= 60:
        print("You Did Well But You Can Do Better")

     elif percentage >= 50:
        print("Keep Practicing")

     else:
        print("Try Hard Better Luck Next Time")
        
    else:
        print("Keep Trying, Better Luck Next Time")

    print("\n=========================================")


if __name__ == "__main__":
    choice = 1
    while choice != 6:
        print('\n=========[WELCOME TO PYTHON HUB]=========')
        print('-----------------------------------------')
        print('1: SIGNUP PANEL')
        print('2: LOGIN PANEL')
        print('3: LOGOUT PANEL')
        print('4: RULES')
        print('5: QUIZ ROUND')
        print('6: EXIT')
        print('-----------------------------------------')
        choice = int(input('ENTER YOUR CHOICE: '))
        if choice == 1:
            createAccount()
        elif choice == 2:
            loginAccount()
        elif choice == 3:
            logout()
        elif choice == 4:
            rules()
        elif choice == 5:
            play()
        elif choice == 6:
            break
        else:
            print('Invalid Input, Please Try Again :(')