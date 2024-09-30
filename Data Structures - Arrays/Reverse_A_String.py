def reverse(string):
    if type(string) == str:  # Check for string input
        charList = list(string)  # Turn string to array
        # print(charList)
        charList.reverse()  # Reverse array
        # print(charList)
        newSting = "".join([word for word in charList])  # Bring all characters together
        return newSting
    else:
        return "Not a string"

print(reverse(4567))
print(reverse("Video games and consoles"))
