import random
import math

names = input("Enter the names of customers (comma-separated): ")
name_list = [name.strip() for name in names.split(",")]
unique_names = list(set(name_list))
random.shuffle(unique_names)
winners = random.sample(unique_names, 2)
reversed_winners = [winner[::-1] for winner in winners]

print("\n🎉 Lucky Draw Results 🎉")
print(f"Winner 1: {reversed_winners[0]}")
print(f"Winner 2: {reversed_winners[1]}")

total = len(unique_names)
print(f"\nTotal unique participants: {total}")
sqrt_participants = round(math.sqrt(total))
print(f"Square root of participants (rounded): {sqrt_participants}")