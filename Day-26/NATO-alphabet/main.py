import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass


# {new_key:new_value for (index, row) in df.iterrows()}

phonetic_df = pandas.read_csv("./Day-26/NATO-alphabet/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in phonetic_df.iterrows()}

def generate():
    user_name = input("Enter Your name: ").upper()

    try:
        phonetic_array = [phonetic_dict[letter] for letter in user_name]
    except Exception as e:
        print(f"{e} Sorry only alphabets allowed")
        generate()
    else:
        print(phonetic_array)

generate()