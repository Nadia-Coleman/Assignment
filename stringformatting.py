# This prints out "Hello, Nadia!"
name = "Nadia"
print("Hello, %s!" % name)
# This prints out "Nadia is 15 years old."
name = "Nadia"
age = 15
print("%s is %d years old." % (name, age))
# This prints out: A list: [1, 2, 3]
mylist = [1, 2, 3]
print("A list: %s" % mylist)
data = ("Nadia", "Coleman", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
