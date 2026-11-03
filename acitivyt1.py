file = open("bucket-list.txt", "w")
file.write("1.Visit the Eiffle Tower\n")
file.write("2.Learn to Code\n")
file.write("3.To become a coder\n")

file.close()
print("Bucket list saved to bucket-list.txt!")

file = open("bucket-list.txt", "r")
content = file.read()
print("\n=== My bucket list ===")
print(content)
file.close()

file = open("bucket-list.txt", "r")
lines = file.readlines()
print(f"You have {len(lines)} items on your bucket list.")
file.close()

file = open("bucket-list.txt", "a")
file.write("4.Go to Arcade\n")
file.write("5.To become susessful in life\n")
file.close()
print("\n2 more items added!")

file = open("bucket-list.txt", "r")
print("\n=== Updated Bucket List ===")
print(file.read())
file.close()

