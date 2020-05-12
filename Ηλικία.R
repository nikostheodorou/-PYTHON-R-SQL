name <- readline(prompt="Enter name: ")
age <- readline(prompt="Enter age: ")
age <- as.integer(age)
print(paste("Hi,", name, "next year you will be", age+1, "years old."))
#This code is writen in english ue to the fact that R does not recognize greek letters of any kind.