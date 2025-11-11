import random

print("\n------------------------------------")
print(" Rock Paper Scissors Lizzard Spock ")
print("-------------------------------------\n")

print("1) is for ✊ (Rock)")
print("2) is for ✋ (Paper)")
print("3) is for ✌️ (Scissors)")
print("4) is for 🦎 (Lizzard)")
print("5) is for 🖖 (Spock)")


player = int(input("\nChoose between numbers 1-5: "))
computer = random.randint(1, 5)

choose = {1: '✊', 2: '✋', 3: '✌️', 4: "🦎", 5: "🖖"}

print(f"\nYou choose: {choose[player]}")
print(f"Cpu choose: {choose[computer]}")

if computer == player:
    print("Its a Draw!")
elif (player == 3 and computer in [2, 4]) or \
     (player == 2 and computer in [1, 5]) or \
     (player == 1 and computer in [4, 3]) or \
     (player == 4 and computer in [5, 2]) or \
     (player == 5 and computer in [3, 1]):
    print("You win!")
else:
    print("Computer Wins")
