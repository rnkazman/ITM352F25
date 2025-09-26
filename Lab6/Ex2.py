listOfLists = [[], [1]*3, [2]*7, [3]*12]
print(listOfLists)

listNumber = int(input("Enter a list number (0-3): "))
listLength = len(listOfLists[listNumber])

if listLength < 5:
    print(f"User entered {listNumber}: Short list")
elif 5 <= listLength <= 10:
    print(f"User entered {listNumber}: Medium list")
else:
    print(f"User entered {listNumber}: Long list")
