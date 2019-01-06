
import random

def welcomeMessage():
    print("Welcome to my very basic rock, paper, scissors game!")
    print('You can play as long as you want.')
    print('Whenever you want to quit, just enter -1 and the game will end immediately.')


#Implementing the rules of rock paper scissors with if-else blocks
def decider(player_action, ai_action):
    
    #Rock beats scissors
    if player_action == '1' and ai_action == '3':
        #player_score = player_score + 1
        return True
    elif ai_action == '1' and player_action == '3':
        #ai_score = ai_score + 1
        return False
    
    #Paper beats Rock
    elif player_action == '2' and ai_action == '1':
        #player_score = player_score + 1
        return True
    elif ai_action == '2' and player_action == '1':
        #ai_score = ai_score + 1
        return False
        
    #scissors beats paper
    elif player_action == '3' and ai_action == '2':
        #player_score = player_score + 1
        return True
    elif ai_action == '3' and player_action == '2':
        #ai_score = ai_score + 1
        return False


#Display the welcome messages
welcomeMessage()

#Possible actions
actions = {'1': 'Rock', '2': 'Paper', '3': 'Scissors'}
player_action = input('Enter a number | Rock(1), Paper(2), or Scissors(3): ')

#Scores of player an AI
player_score = 0
ai_score = 0

#Action of AI will be defined in the while loop
ai_action = None

#Game will continue until the user enters '-1' as their choice.
while player_action != '-1':
    ai_action = str(random.randint(1, 3))
    
    #Actions performed when the player wins
    if decider(player_action, ai_action) == True:
        player_score += 1
        print('You won!')
        print('Your move:', actions[player_action], "| AI's move:", actions[ai_action])
    
    #Actions performed when the AI wins    
    elif decider(player_action, ai_action) == False:
        ai_score += 1
        print('AI won :(')
        print('Your move:', actions[player_action], "AI's move:", actions[ai_action])
    
    #Actions performed when it's a tie    
    else:
        print("It's a tie!")
        print('Your move:', actions[player_action], "AI's move:", actions[ai_action])
        
    print("Your score:", player_score, "\nAI's score:", ai_score, "\n")
    player_action = input('Enter a number | Rock(1), Paper(2), or Scissors(3): ')


#Ending the game
print("Game stopped.")
print("Your final score:", player_score, "\nAI's final score:", ai_score)

#End game messages
if player_score > ai_score:
    print("You won the game! Thanks for playing! I hope you had a fun time.")
elif player_score == ai_score:
    print("You tied! Feel free to try your luck later.")
else:
    print("Thanks for playing! I hope you had a fun time... Even though you lost(hehehe)")
