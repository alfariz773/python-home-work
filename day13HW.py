n = int(input("How many student names do you want to add? "))

with open("students.txt", "a+") as f:   
    f.seek(0)  
    print("\nExisting Student Names:")
    print(f.read())  
    
    for _ in range(n):
        name = input("Enter student name: ")
        f.write(name + "\n")

print("\nUpdated Student List:")
with open("students.txt", "r") as f:   
    print(f.read())
