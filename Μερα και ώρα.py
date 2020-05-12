x = input("Μπορείς να μου δώσεις ημερομηνία και ώρα; ΝΑΙ ή ΟΧΙ;")
if x == "ΝΑΙ":
	from datetime import datetime

	Τώρα = datetime.now()

	Μέρα = str(Τώρα.day)

	Μήνας = str(Τώρα.month)

	Χρόνος = str(Τώρα.year)

	Ωρα = str(Τώρα.hour)

	Λεπτό = str(Τώρα.minute)

	print ("Είναι " + Μέρα + "/" + Μήνας + "/" + Χρόνος + " και " + Ωρα + ":" + Λεπτό)
elif x == "ΟΧΙ":
    print("Οκ, δεν πειράζει.")
else:
    print("Μπορείς να μου πεις; ΝΑΙ ή ΟΧΙ;")
