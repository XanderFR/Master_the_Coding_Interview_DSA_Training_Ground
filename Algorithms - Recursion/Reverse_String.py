def recursiveReverse(string):
    if len(string) == 0:
        return string
    else:
        return recursiveReverse(string[1:]) + string[0]  # First letter goes to the back


def recursiveReverseTwo(string):
    if len(string) == 0:
        return string
    else:
        return string[-1] + recursiveReverseTwo(string[:-1])  # Last letter goes to the front

print(recursiveReverse("Alexander Dave Flores Respicio"))
print(recursiveReverseTwo("Alexander Dave Flores Respicio"))
