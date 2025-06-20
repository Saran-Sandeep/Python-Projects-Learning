list_name = [ "Ajay" , "Gokul" , "Ali", "Saran" , "Sandeep" , "Sai" ]

while True :

    print("Hi! My name is Travis")
    name = input( "What is your Name ? :" ).strip().capitalize()

    if ( name in list_name ) :

        print("Hello {}!".format(name))

        #print( "Registerd Name Detected " )

        remove_me = input("Would you like to removed from the system?(y/n) :").strip().lower()

        if remove_me=='y' :

            list_name.remove(name)

        elif remove_me=='n' :

            print("Okay!!!No problem, I don't want you to leave anyway.")

    else :

        #print ( " Unregistered Name Detected " )

        print(f"Hmm! I don't think i have met you yet {name}")

        add_me = input("Would you like to be added to system?(y/n)").strip().lower()

        if add_me=='y' :

            list_name.append(name)

            #print ( " New Username Registered " )

        elif add_me=='n' :

            print("No worries, See you around !")
