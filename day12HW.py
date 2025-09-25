name= input("enter your name:")
if name.strip():
    
    feedback= input("enter your feedback:")
    if feedback.strip():
        
        print(f"\n thankyou, {name}, for your feedback")
        print(f"your feedback: {feedback}")
        
    else:
        print("error: feedback cannot be empty")
else:
    print("error: name cannot be empty")
    
print("\nFeedback process finished (with or without error).")
        