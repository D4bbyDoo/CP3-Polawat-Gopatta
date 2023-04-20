userName = input("Username : ")
passWord = input("Password : ")

if userName == "Dabby" and passWord == "front":
    print(" ")
    print(" ")

    pizza = 200
    patkapao = 60
    spaghetti = 150
    beer = 80
    cola = 25
    water = 15

    print ("------------- Welcome to Babui restaurant -------------")
    print("1) Pizza ----------------------------------- 200 ฿")
    print("2) Patkapao -------------------------------- 60  ฿")
    print("3) Spaghetti ------------------------------- 150 ฿")
    print("4) Beer ------------------------------------ 80  ฿")
    print("5) Cola ------------------------------------ 25  ฿")
    print("6) water ----------------------------------- 15  ฿")
    print(" ")
    print("-------------------- Your's Choice --------------------")
    userchoice = int(input(">> "))
    print("------------------------ Bill -------------------------")
    print(" ")
    if userchoice == 1:
        print("Pizza ------------------------------------- ",pizza," ฿")
        print(" ")
        print("Total : ",pizza," ฿")
        print("---------------------- Thank You ----------------------")

    elif userchoice == 2:
        print("Patkapao ---------------------------------- ",patkapao," ฿")
        print(" ")
        print("Total : ",patkapao," ฿")
        print("---------------------- Thank You ----------------------")

    elif userchoice == 3:
        print("Spaghetti --------------------------------- ", spaghetti, " ฿")
        print(" ")
        print("Total : ", spaghetti, " ฿")
        print("---------------------- Thank You ----------------------")
    elif userchoice == 4:
        print("Beer -------------------------------------- ", beer, " ฿")
        print(" ")
        print("Total : ", beer, " ฿")
        print("---------------------- Thank You ----------------------")
    elif userchoice == 5:
        print("Cola -------------------------------------- ", cola, " ฿")
        print(" ")
        print("Total : ", cola, " ฿")
        print("---------------------- Thank You ----------------------")
    elif userchoice == 6:
        print("water ------------------------------------- ", water, " ฿")
        print(" ")
        print("Total : ", water, " ฿")
        print("---------------------- Thank You ----------------------")




