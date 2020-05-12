x=input("Θες να παίξεις ζάρια; ΝΑΙ ή ΟΧΙ;")
if x=="ΝΑΙ":
	import random
	min = 1
	max = 6

	roll_again = "ΝΑΙ"

	while roll_again == "ΝΑΙ":
		print ("Ρίξε τα ζάρια...")
		print ("Έριξες....")
		print (random.randint(min, max))
		print (random.randint(min, max))

		roll_again = input("Πάμε πάλι;")
elif x == "ΟΧΙ":
    print("Οκ, δεν πειράζει.")
else:
    print("Μπορείς να μου πεις; ΝΑΙ ή ΟΧΙ;")