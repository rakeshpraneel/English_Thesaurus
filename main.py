import json
import difflib

Data_Set = json.load(open('data_set/Words_meaning_data_set.json'))

def Search_word(word):
    if word in Data_Set:
        return Data_Set[word]
    elif word.lower() in Data_Set:
        w = word.lower()
        return Data_Set[w]
    elif word.title() in Data_Set:
        w = word.title()
        return Data_Set(w)
    else:
        w = word.lower()
        predicted_word = difflib.get_close_matches(w, Data_Set.keys())[0]
        print("Are you searching for ",predicted_word)
        option = input("Enter y for Yes and n for No:")
        if option == 'y' or option == 'Y':
            return Data_Set[predicted_word]

if __name__ == '__main__':
    User_input = input("Enter the word: ")
    Output = Search_word(User_input)
    #print(Output)
    if type(Output) is list:
        for o in Output:
            print(o)
    else:
        print(Output)
    #print(Data_Set)
    #print(type(Data_Set))