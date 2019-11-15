with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string[:52] + "...")
print(len(pi_string))

filename = 'pi_digits_copy.txt'

with open(filename, 'w') as file_obj:
    file_obj.write(pi_string)
    file_obj.write("I also love finding meaning in large datasets.\n")
    file_obj.write("I love creating apps that can run in a browser.\n")

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")