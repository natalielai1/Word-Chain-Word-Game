
## Brief Description
A game similar to Word chain, an existing word game in which players come up with words that begin with the letter or letters that the previous word ended with. A category of words is usually chosen: an example chain for food would be soup, peas, sugar, rice. However, my version has no category and instead rules over the number of letters that must be in the word. 

---

## Settings
The player will be able to choose how many rounds they want to play.
The player will enter their action as a string.
If the player answers correctly, they will get a notification and points added to their total score.


---

## Rules of Play

Welcome to CHAIN GROWTH
Rules:
1. You’ll be given a random letter to start.
2. Your first word must start with that letter and be three letters long.
3. Each new word must start with the last letter of the previous word.
4. Each word must be one letter longer than the previous. 
5. You earn points equal to the length of each valid word. The maximum length of a word is 10, then the game will automatically regenerate. A regeneration starts over at Step 1 again, but your previous points are still counted.
6. If you are unable to come up with the next word, you may regenerate. 
7. You may not repeat a word you've already used in the round.
8. You have 3 regenerations (new starting letters) until the round is over.
The goal is to get as many points as possible before the round is over.
---

## Technical Considerations

What information is needed to fully describe the state of the game? 
A list of English words of lengths 3-10.
A list of all previous guesses made by the player.
Number of turns remaining. 
Counter of points that is visible to player. 
A visible notification after each time the player submits a word to showing whether their word is valid.
A visible counter of how many letters the next word has to be.

## TODOs
- Implement word validation logic
- Create scoring system
- Add regeneration functionality
- Test game with various word chains
