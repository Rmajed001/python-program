#Input() statement in Python is used to take input from the user. it used to accept values (using keyboard) from the user at runtime.
#সহজ বাংলায় ইনপুট() স্টেটমেন্ট ব্যবহার করে ইউজার থেকে ইনপুট নেয়া হয়।
#পাইথনে ইনপুট() স্টেটমেন্ট সবসময় স্ট্রিং টাইপের ডাটা রিটার্ন করে। অর্থাৎ, ইউজার ইনপুট হিসেবে যে ডাটা দিবে তা স্ট্রিং টাইপে রিটার্ন হবে।
#আলাদা করে টাইপ কনভার্সন করতে হবে। যেমনঃ int করে নিতে চাইলে int(input()) ফাংশন ব্যবহার করতে হবে। ঠিক তেমনি float করতে চাইলে float(input()) ফাংশন ব্যবহার করতে হবে।

name=input("Enter your name: ")  
print( " Welcome", name,type(name))  

val=int(input("Enter a number: "))  # Taking integer input from the user
print("You entered:", val," type of value is:", type(val))
val_float=float(input("Enter a float number: "))  # Taking float input from the user
print("You entered float number:", val_float," type of value is:", type(val_float))


name=input("Enter name: ")
age=int(input("Enter age: "))  # Taking integer input for age
marks=float(input("Enter marks: "))

print("welcome", name)
print("Age: ", age)
print("Marks: ", marks)
print("Type of name is:", type(name))
print("Type of age is:", type(age))
print("Type of marks is:", type(marks))
