#WAP to enter marks of three subjects from the user and store them in a 
#dictionary.Start with an empty dictionary and add one by one.
#Use subject name as key and marks as value.
marks={}
x=int(input("Enter physics marks:"))
marks.update({"physics":x})

x=int(input("Enter chemistry marks:"))
marks.update({"chemistry":x})

x=int(input("Enter maths marks:"))
marks.update({"maths":x})

print(marks)