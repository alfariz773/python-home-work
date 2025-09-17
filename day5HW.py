frontend={"sam","jhon","kiran","james","shibin"}
backend={"jaison","daniel","sam","kiran","jhon"}

# adding a new student to the backend set 
backend.add("salman")

# Remove a student from the Frontend course
frontend.remove("shibin")

# Displaying the list of students who are enrolled in both courses
bth= backend & frontend
print(f"The student in both list is {bth}")

# Displaying the list of students who are enrolled only in Backend
bckend= backend - frontend
print(f" The student only in backend are {bckend}")

# unique students

uni= backend | frontend
print(f"the count of unique name {len(uni)}")

# Dictionary comprehension to add Fullstack course

dit = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}

# Dictionary comprehension to add Fullstack course

print("the number of each students are:")
for course, count in dit.items():
    print(f"{course}: {count} students")
    
    
#  Dictionary comprehension to add Fullstack course   
fullstack = {**dit, "Fullstack": dit["Frontend"] + dit["Backend"]}
print("\nCourse dictionary with Fullstack included:")
print(fullstack)
    



