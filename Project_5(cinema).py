#list the films, the age restriction and the no. of seats available using a data structure

films = {
    "Finding Dory" : [5,3],
    "Tarzan" : [10,5],
    "Bourne Ultimatum" : [18,12],
    "Ghost Busters" : [18,15]
    }

while True :

#asking users choice of the film
    
    choice = input("Which film would you like to watch ? :").strip().title()

    if choice in films :

#asking the user's age
        
        age = int(input("What is your age ? :"))

#check age 
        
        if age >= films[choice][0] :

#check availability of seats

            if films[choice][1]==0 :

                print("Sorry...Housefull")

            else :

                films[choice][1]-=1
                
                print("You are good to go....Enjoy the film  :-)")

        else :

            print("You are too young to see that film")
            
    else :

        print("Sorry ! We dont have that film")

    
    
