import pandas # type: ignore

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

PATH = r'D:\PYTHON\PYTHON - Udemy\Game\NATO GAME\nato_phonetic_alphabet.csv'
letter_data = pandas.read_csv(PATH)
#letter_list = letter_data.to_dict()

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter:row.code for (index,row) in letter_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def gen_phonetic():
    word = input("ENter a Word : ").upper()
    try:
        output_list = [phonetic_dict[let] for let in word]
    except KeyError:    
        print("Sorry,only letters in the alphabet please.")
        gen_phonetic()
    else:
        print(output_list)

gen_phonetic()