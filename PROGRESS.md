# Progress Report
### Due: Monday 1/10 @ 11:59pm Eastern Time

This file will contain your Progress Report. Answer the prompts below to evaluate how well you were able to meet your intermediate goal(s).

### In a numbered list, briefly restate the intermediate goal(s) from your Project Proposal.
- Basic feature of blackjack: hit, stand, surrender

### Which goal(s) were you able to acheieve?
- I can do hit,stand,surrender,double down and analyst(using Matplotlib, NumPy and Scipy)

### Which goal(s) were you not able to acheieve? 
#### Please describe what problem(s) you faced, and indicate if you are still stuck on any particular step.
- I have a bug that i really don't know how to fix is that: for example
+ Player's sum still under 21
+ Housebet's sum however are above 21 and I indicate that the housebet lose
+ And then the next turn is player's turn.
- In another scenerio,
+ Player's sum is above 21 and he loses. So I programmed it to immediately end the turn but The next turn, instead of showing a player's turn, my program showed the housebet's turn.
- I found the bug was in run() with 2 parameters player_turn and housebet_turn and the play()'s parameter: whose_turn
- I don't know how to set the condition statement in the run() so that the program can discriminate between 2 previous situations

### In a few sentences, descibe your next steps.
- Check out more about the Matplotlib library

