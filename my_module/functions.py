"""A collection of functions for doing my project."""

import random

def format_answers(answers):
    """ This function formats the user's response to the quiz
    
    Parameters
    ----------
    answers: list
        a list of the user's answers
    
    Returns
    -------
    formatted_answers: list
        a list of user's answers formatted to be fed into other functions
    """
    
    formatted_answers = []
    
    for answer in answers:
        
        answer = answer.upper()
                                         
        if len(answer) != 1: # if someone responds more than one character. i.e. AA or A.
            return print('Please submit a single character answer for your multiple choice response (A, B, C, or D)')
        elif answer not in ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']:
            return print('Please submit a single character answer for your multiple choice response (A, B, C, or D)')
        else:
            formatted_answers.append(answer) #if they submit a single character, it gets appended.
    
    return formatted_answers

def test(): 
    """
    This function prompts the user to answer ten questions related to the television show *Friends*, 
    and stores their answers in a variable.
    
    
    Parameters
    ----------
    Takes no arguments for input, the user will be prompted to input answers once the function is run
    
    Returns
    -------
    user_answers: list
        a list containing the user's test answers
    """
    
    question_list = [
                 "\nWhose babies did Phoebe give birth to?\n\n" + 
                    "A. Joey's\n" + 
                    "B. Mike's\n" + 
                    "C. David's\n" + 
                    "D. Her brother's\n\n" + 
                    "Answer: ", 
                 "\nHow many Friends are there?\n\n" + 
                    "A. 3\n" + 
                    "B. 5\n" + 
                    "C. 6\n" + 
                    "D. 4\n\n" + 
                    "Answer: ",
                 "\nWhere did Mike intially propose to Phoebe?\n\n" + 
                    "A. Barbados\n" + 
                    "B. Costa Rica\n" + 
                    "C. The coffee shop\n" + 
                    "D. A restaurant\n\n" + 
                    "Answer: ",
                 "\nWhat did Ross and Rachel name their baby?\n\n" + 
                    "A. Molly\n" + 
                    "B. Grace\n" + 
                    "C. Emma\n" + 
                    "D. Elizabeth\n\n" + 
                    "Answer: ",
                 "\nWhich relationship made Ross so drunk that he held a dish out of the oven with no mits?\n\n" + 
                    "A. Charlie back with her ex Benjy\n" + 
                    "B. Chandler & Monica\n" + 
                    "C. Rachel & Elizabeth's dad\n" + 
                    "D. Rachel & Joey\n\n" + 
                    "Answer: ",
                 "\nWhat color dress did Rachel decide on in *The One Where No One Was Ready*?\n\n" + 
                    "A. Yellow\n" + 
                    "B. Beige\n" + 
                    "C. Lavender\n" + 
                    "D. Green\n\n" + 
                    "Answer: ",
                 "\nWhich trivia question made Monica & Rachel loose their apartment over to Chandler & Joey?\n\n" + 
                    "A. How many sisters does Joey have?\n" + 
                    "B. How many women has Chandler slept with?\n" + 
                    "C. What's Chandler's job?\n" + 
                    "D. What's Joey's favorite kind of sandwich?\n\n" + 
                    "Answer:  ",
                 "\nIn regards to Phoebe: which of the following is not true?\n\n" + 
                    "A. She believed her mom was reincarnated as a cat\n" + 
                    "B. She stalked her twin's stalker\n" + 
                    "C. She robbed Chandler on the street\n" + 
                    "D. She was offered to be made into a popstar from her song, *Smelly Cat*\n\n" + 
                    "Answer: ",
                 "\nHow would you describe Joey?\n\n" + 
                    "A. A *player*\n" + 
                    "B. An intellectual\n" + 
                    "C. A socialite\n" + 
                    "D. A hermit\n\n" + 
                    "Answer: ",
                 "\nFrom what does Chandler's humor stem from?\n\n" + 
                    "A. His innate tendencies to people-please\n" + 
                    "B. A defense mechanism from his parent's divorce\n" + 
                    "C. An attempt to maintain his friends as he didn't have many growing up\n" + 
                    "D. Tribute to his favorite comedians\n\n" + 
                    "Answer: "
    ]
    
    answer_key = [
                  'D',
                  'C',
                  'A', 
                  'C',
                  'D',
                  'D',
                  'C',
                  'C',
                  'A',
                  'B'
    ]
    
    user_answers = [] # empty list to append the user's answers to
    
    for q in question_list:
        
        answer = input(q) # input function to prompt the user to answer questions from the question_list
        user_answers.append(answer)
    
    user_answers = format_answers(user_answers)
    
    return user_answers

def calculate_score(answers_list):
    
    """ Running this function reviews the user's answers to the quiz from the test() function 
        
        Parameters
        ----------
        answers_list: list 
            10 single-charater str answers that are multiple choice. 
        
        Returns
        -------
        User's score: str 
            how many they got correct out of how many total questions. 
        If the user submits an answer that is not acceptable, the function print's instruction to retake the quiz.
        
    """
    
    question_list = [
                 "\nWhose babies did Phoebe give birth to?\n\n" + 
                    "A. Joey's\n" + 
                    "B. Mike's\n" + 
                    "C. David's\n" + 
                    "D. Her brother's\n\n" + 
                    "Answer: ", 
                 "\nHow many Friends are there?\n\n" + 
                    "A. 3\n" + 
                    "B. 5\n" + 
                    "C. 6\n" + 
                    "D. 4\n\n" + 
                    "Answer: ",
                 "\nWhere did Mike intially propose to Phoebe?\n\n" + 
                    "A. Barbados\n" + 
                    "B. Costa Rica\n" + 
                    "C. The coffee shop\n" + 
                    "D. A restaurant\n\n" + 
                    "Answer: ",
                 "\nWhat did Ross and Rachel name their baby?\n\n" + 
                    "A. Molly\n" + 
                    "B. Grace\n" + 
                    "C. Emma\n" + 
                    "D. Elizabeth\n\n" + 
                    "Answer: ",
                 "\nWhich relationship made Ross so drunk that he held a dish out of the oven with no mits?\n\n" + 
                    "A. Charlie back with her ex Benjy\n" + 
                    "B. Chandler & Monica\n" + 
                    "C. Rachel & Elizabeth's dad\n" + 
                    "D. Rachel & Joey\n\n" + 
                    "Answer: ",
                 "\nWhat color dress did Rachel decide on in *The One Where No One Was Ready*?\n\n" + 
                    "A. Yellow\n" + 
                    "B. Beige\n" + 
                    "C. Lavender\n" + 
                    "D. Green\n\n" + 
                    "Answer: ",
                 "\nWhich trivia question made Monica & Rachel loose their apartment over to Chandler & Joey?\n\n" + 
                    "A. How many sisters does Joey have?\n" + 
                    "B. How many women has Chandler slept with?\n" + 
                    "C. What's Chandler's job?\n" + 
                    "D. What's Joey's favorite kind of sandwich?\n\n" + 
                    "Answer:  ",
                 "\nIn regards to Phoebe: which of the following is not true?\n\n" + 
                    "A. She believed her mom was reincarnated as a cat\n" + 
                    "B. She stalked her twin's stalker\n" + 
                    "C. She robbed Chandler on the street\n" + 
                    "D. She was offered to be made into a popstar from her song, *Smelly Cat*\n\n" + 
                    "Answer: ",
                 "\nHow would you describe Joey?\n\n" + 
                    "A. A *player*\n" + 
                    "B. An intellectual\n" + 
                    "C. A socialite\n" + 
                    "D. A hermit\n\n" + 
                    "Answer: ",
                 "\nFrom what does Chandler's humor stem from?\n\n" + 
                    "A. His innate tendencies to people-please\n" + 
                    "B. A defense mechanism from his parent's divorce\n" + 
                    "C. An attempt to maintain his friends as he didn't have many growing up\n" + 
                    "D. Tribute to his favorite comedians\n\n" + 
                    "Answer: "
    ]

    
    answer_key = [
                  'D', 
                  'C',
                  'A', 
                  'C',
                  'D',
                  'D',
                  'C',
                  'C',
                  'A',
                  'B'
    ]
    
    score = 0
    
   
    # Mikey suggested the Try/ Except method to silence my error message — https://github.com/mike-flanagan
    try: 
        
        for key, answer in zip(answer_key, answers_list): # for these items in these lists, we iterate through and 
                                                          # compare the user_answers to the answer_key index to index
            if key == answer:
                score += 1 # if the user answers correctly match the answer key, we increase the user's score by 1
            else:
                pass # if the user's answer does not match, we move on to the next answer
    
        return "Your score: " + str(score) + " / " + str(len(question_list)) # I attribute Servin for this specific line
    
    except:
        
        print("YOU MADE A TYPO! \n\nPlease retake the quiz and submit ONLY A, B, C, or D for answers.")

def phoebe_song():
    
    """ This function generates a random song (with lyrics) that Phoebe will perform.
    
    Parameters
    ----------
    No arguments
    
    Returns
    -------
    song: str 
        the title of the song generated with the chorus of the song's lyrics
    
    """
    
    song_choices = ['Smelly Cat', 'Stinky Shoes', 'Jingle Bitch', 'Crusty Old Man', 'First Time I met Chandler']
    
    song = random.choice(song_choices) #generates a random song from song_choices
    ('Song: ', song)
    
    # for formatting, I had to use many unflattering spaces within the string of the song
    if song == 'Smelly Cat':
        return f"Song: {song}                                                                                                    "+\
    "Chorus: Smelly Cat, Smelly Cat, What are they feeding you? Smelly Cat, Smelly Cat, It's not your fault"
    
    elif song == 'Stinky Shoes':
        return f"Song: {song}                                                                                                  "+\
    "Chorus: Sticky shoes, sticky shoes. Always makes me smile. Sticky shoes, sticky shoes- Next time I'll avoid the pile"
    
    elif song == 'Jingle Bitch':
        return f"Song: {song}                                                                                                  "+\
    "Chorus: Jingle Bitch screwed me over! Go to hell Jingle Whore! Go to hell, go to hell, go to hell-hell-hell"
    
    elif song == 'Crusty Old Man':
        return f"Song: {song}                                                                                                  "+\
    "Chorus: And a crusty old man said, 'I'll do what I can,' and the rest of the rats played moroccas."
    
    elif song == 'First Time I met Chandler':
        return f"Song: {song}                                                                                                  "+\
    "Chorus: First time I met Chandler I thought he was gay, but here I am singing on his wedding daaaay"
  