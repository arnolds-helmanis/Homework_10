count = 0
input = input("Enter file name: ")
fileHandle = open(input)
# I made an empty set so i could extract unique senders and sort all the senders in an alphabetic order
senderSet = set()
# This 'for' cycle iterates through file lines and looks for the lines that starts with 'From', splits this
# line in words and appends the senders to the 'sendersList' list
for line in fileHandle:
    if line.startswith("From"):
        count = count + 1
        contact = line.split(" ")
        senderSet.add(contact[1].rstrip())
senderList = sorted(senderSet)
for sender in senderList:
    print(sender)
senderCount = len(senderList)
print("")
print("In this file were", senderCount, "unique senders, with combined", count, "sent emails.")