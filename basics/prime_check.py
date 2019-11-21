def check_val(value):
    for i in range(2, value // 2):
        if value % 2 == 0:
            return False
        else:
            return True
    return True


for n in range(2, 10):
    print(str(n) + ":" + str(check_val(n)))
