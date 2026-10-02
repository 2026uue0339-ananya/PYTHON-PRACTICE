#5. Suppose a user enters a sentence/paragraph. Calculate the number of appearance of each 
# word. Hints: • Convert the sentence to lowercase. • Split it into words. • Use a for loop 
# to count occurrences. • Store frequencies in a dictionary. • Allow the user to analyze 
# multiple sentences using a while loop.

#lets make exit by default no

exit = "no"

#make a list to store the words and count the no of words in each sentence

list = []
#store the sentence make a list

sentence_list =[]

#to repeatedly use to write sentence and run the process

while exit !="yes":

#store frequency of words in a dictionary

    paragraph = {
        
        "frequencies": 0
    }

#make the sentence in lowercase

    sentence = input("Enter your thoughts: ").lower()

#split the sentence into words

    words = sentence.split()
   # print(words)

#stor words in list and count it

    for i in words:
        count = words.count(i)
        list.append(count)

    paragraph["frequencies"] = sum(list)    

#after every process ask further

    exit = input("Do you want to exit? (yes/no):")
    #store all sentences from initial into a list

    sentence_list.append(sentence)
    #see what you write

    print(sentence_list)
    #see the no of words you take

    print("No of words in the paragraph:", paragraph["frequencies"])
       

