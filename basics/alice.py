filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except:
    msg = "Can't find file " + filename + "!"
    print(msg)
