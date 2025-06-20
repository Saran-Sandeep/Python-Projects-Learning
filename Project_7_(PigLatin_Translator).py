#ask the user for a sentence

sentence=input("Enter a Sentence : ").strip().lower()

#split the sentence into words

words=sentence.split()

#loop through each word and make the words into piglatin

new_words=[]

for word in words :

    if word[0] in "aeiou" :

        new_word=word + "yay"
    
        new_words.append(new_word)

    else :
        v_pos=0
        
        for letter in word :

            if letter not in "aeiou" :

                v_pos=v_pos+1

            else :

                break
            
        cons=word[0:v_pos]
        
        the_rest=word[v_pos:]

        new_word=the_rest+cons+"ay"

        new_words.append(new_word)

#Sticking all words again into sentence

output=" ".join(new_words)

#print output

print(output)

        
