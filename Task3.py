def digital_root(number):
    total = 0
    number = str(abs(number))
    for x in number:
        total += int(x)
    return total


print(digital_root(23491))
print(digital_root(35424165))
