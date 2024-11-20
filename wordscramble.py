import random

def word_scramble():
    print("Welcome to Word Scramble!")

    # A large list of words (1000+ words)
    word_list = [
        'abacus', 'absolute', 'academy', 'accident', 'accommodate', 'accordion', 'achievement', 'acquaintance',
        'adventure', 'allegory', 'ambition', 'amplify', 'analysis', 'ancient', 'applause', 'approach', 'argument',
        'articulate', 'aspiration', 'attempt', 'attractive', 'audible', 'balance', 'barrier', 'beautiful',
        'benefit', 'bicycle', 'blossom', 'borrowing', 'calendar', 'capture', 'category', 'champion', 'charity',
        'chemistry', 'circular', 'clarify', 'classic', 'collection', 'companion', 'computer', 'courageous', 'courage',
        'creativity', 'debate', 'defend', 'delight', 'difficult', 'discovery', 'eliminate', 'enlighten', 'episode',
        'equality', 'eventful', 'exercise', 'explanation', 'extraordinary', 'fantastic', 'festival', 'fiction',
        'freedom', 'generous', 'genuine', 'glorious', 'harmony', 'happiness', 'highlight', 'imagine', 'incredible',
        'inspiration', 'intellect', 'interest', 'invention', 'journey', 'justice', 'knowledge', 'landscape', 'learning',
        'magnetic', 'magnitude', 'mature', 'meaningful', 'mystery', 'national', 'optimism', 'outstanding', 'paradise',
        'particular', 'patience', 'perfect', 'photograph', 'reliable', 'reputation', 'responsible', 'revolution', 'scenery',
        'sensation', 'sincere', 'solution', 'strengthen', 'success', 'sufficient', 'symbolic', 'teacher', 'tournament',
        'universe', 'victorious', 'wholesome', 'wonderful', 'zoology', 'acknowledge', 'adopt', 'advantage', 'analysis',
        'anxiety', 'artificial', 'audible', 'automobile', 'beautiful', 'beginning', 'beverage', 'blessing', 'bother',
        'calculate', 'celebration', 'chamber', 'charismatic', 'climate', 'clutter', 'collaborate', 'creativity', 'difficult',
        'education', 'electronic', 'endurance', 'enlighten', 'estimate', 'fashionable', 'fictional', 'freedom', 'genuine',
        'gesture', 'gossips', 'imagination', 'importance', 'intelligent', 'innocent', 'insightful', 'invincible', 'justice',
        'keystone', 'language', 'laughter', 'magnitude', 'metaphor', 'negotiate', 'observant', 'optimal', 'opinion',
        'persistence', 'powerful', 'radiant', 'rejuvenate', 'resilient', 'respectful', 'responsible', 'spiritual', 'tendency',
        'transparent', 'understand', 'victorious', 'wonderful', 'zodiac'
        # Add more words here, you can add up to 1000+ words.
    ]
    
    # Select a random word from the list
    word_to_guess = random.choice(word_list)
    
    # Scramble the word
    scrambled_word = ''.join(random.sample(word_to_guess, len(word_to_guess)))
    
    print(f"The scrambled word is: {scrambled_word}")
    
    # Ask the player to guess the unscrambled word
    attempts = 0
    while True:
        guess = input("Unscramble the word: ").lower()
        attempts += 1
        
        if guess == word_to_guess:
            print(f"Congratulations! You've unscrambled the word in {attempts} attempts.")
            break
        else:
            print("Incorrect guess. Try again!")

if __name__ == "__main__":
    word_scramble()
