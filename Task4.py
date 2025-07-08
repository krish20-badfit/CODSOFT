import tkinter as tk
import random

class RPSGame:
    def __init__(self,root):
        self.root=root
        self.root.title("Rock Paper Scissor")
        self.root.geometry("600x650")


        self.choices=["Rock","Paper","Scissors"]

        self.user_score=0
        self.comp_score=0

        #Instruction
        self.label=tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial",15))
        self.label.pack(pady=10)

        #Score display
        self.score_label=tk.Label(root, text="You: 0  | Computer: 0", font=("Arial",15))
        self.score_label.pack(pady=10)

        #Result Display
        self.result=tk.Label(text="",font=("Arial",14))
        self.result.pack(pady=10)




        for choice in self.choices:
            btn = tk.Button(root, text=choice, width=20,command=lambda c=choice: self.play(c))
            btn.pack(pady=5)

        #Reset Btn
        reset_btn = tk.Button(root, text="Reset Score", width=20, bg="red", fg="white", command=self.reset_score)
        reset_btn.pack(pady=20)

    def play(self,user_choice):
        comp_choice= random.choice(self.choices)
        result_text= f"You chose {user_choice}, Computer chose {comp_choice}."

        if user_choice==comp_choice:
            result_text += "It is a tie"

        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
                (user_choice=="Paper" and comp_choice=="Rock") or \
                (user_choice=="Scissors" and comp_choice=="Paper"):
            result_text += "You Win! 🥇💐"
            self.user_score += 1

        else:
            result_text += "Computer Wins! 🥇💻"
            self.comp_score += 1



        self.result.config(text=result_text)
        self.score_label.config(text=f"You: {self.user_score} | Computer: {self.comp_score}")

    def reset_score(self):
        self.user_score = 0
        self.comp_score = 0
        self.score_label.config(text="You: 0  | Computer: 0")
        self.result.config(text="Scores have been reset.")


#Now Run Application
root = tk.Tk()
game = RPSGame(root)
root.mainloop()
