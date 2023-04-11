"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open('green-eggs.txt').read()
    # print(contents)
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    ['Would', 'you', 'could', 'you', 'in', 'a', 'house?', 'Would', 'you', 'could', 
     'you', 'with', 'a', 'mouse?', 'Would', 'you', 'could', 'you', 'in', 'a', 'box?', 
     'Would', 'you', 'could', 'you', 'with', 'a', 'fox?', 'Would', 'you', 'like', 'green', 
     'eggs', 'and', 'ham?', 'Would', 'you', 'like', 'them,', 'Sam', 'I', 'am?']


    chains = {}
    
    # your code goes here

    contents_list = text_string.split()
    # print(contents_list)
    #contents_list = [words]

    # Would you could you in a house?
    for i in range(0, len(contents_list)- 1):
       chains[(contents_list[i],contents_list[i+1])] = []
        

    # Loop over the text_string
    for i in range(0, len(contents_list)-2):
        # if (word1, word2) are key in our dictionary we will add as a value word3 
        if ((contents_list[i], contents_list[i+1]) in chains):
            chains.get((contents_list[i], contents_list[i+1])).append(contents_list[i+2])

    # print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    #choice(chains.keys())
    # rand_key = chains.keys().choice

    
    rand_key = choice(list(chains))    
    rand_value = choice(chains.get(rand_key))
    
    words.extend(list(rand_key))
    words.append(rand_value)

    # get new key
    # rand_key[0], rand_value

    
    print(rand_key, rand_value)
    #print(words)
    while(True):
        rand_key = (words[-2], words[-1]) #(I, am)
        
        print("loop: ", rand_key)
        if(rand_key not in chains or rand_value == []):
            print(f"{rand_key} is not in chains, or {rand_value} is empty)")
            break
        
        
        rand_value = choice(chains.get(rand_key))
        
        words.append(rand_value)
        #print(f"{rand_key} exists. random value: {rand_value}")

        print(words)

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
