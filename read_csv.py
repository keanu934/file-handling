import csv
 
             
 
 
#using csv create a list of dictionaries where each dict is a character with the keys being the headers
 
def get_chars():
    lis=[]
    with open("characters.csv","r") as file :
        csv_reader = csv.reader (file)  
        headers=next(csv_reader)
        for row in csv_reader :
            record = {}
            for i in range(len(headers)):
                record [headers[i].lower()] = row[i]
            lis.append(record)
        return lis
   
def print_characters_info(characters, idx):
 
    if 0 <= idx < len(characters):
        # print(characters)
        character = characters[idx]
 
        #print(f"{character['name']}")
        print(f"{character['name']} is a {character['species']} that is {character['age']} and weighs {character['weight']} lbs")
 
def main():
    characters = get_chars()
    # print (characters)
    idx=5
    print_characters_info(characters, idx)
    characters[idx]["weight"] = 15
    print_characters_info(characters, idx)
 
if __name__=='__main__':
    main() 