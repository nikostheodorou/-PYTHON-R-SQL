import sys
import random

ans = True

while ans:
    question = input("Κάνε μία ερώτηση: (πάτα enter για να κλέισει) ")
    
    answers = random.randint(1,8)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print ("Σίγουρα")
    
    elif answers == 2:
        print ("Πιθανό")
    
    elif answers == 3:
        print ("Ίσως")
    
    elif answers == 4:
        print ("Ρώτα μετά")
    
    elif answers == 5:
        print ("Δεν είναι σίγουρο")
    
    elif answers == 6:
        print ("Μπορεί και όχι")
    
    elif answers == 7:
        print ("Μάλλον όχι")
    
    elif answers == 8:
        print ("Σίγουρα όχι")