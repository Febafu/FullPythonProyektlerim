import random
oynamaq=True
while (oynamaq):
    def play_game():
        options = ["rock", "paper", "scissors"]
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
    
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")
        a=input("Devam etmek isteyirsiniz? 1=YES 0=NO : ")
        if (a):
            oynamaq=True
        elif(a):
            break

    def main():
        play_game()


    if __name__ == "__main__":
        main()
    

