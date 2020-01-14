import os

def nice_count2():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day5.txt") as f:
        data = f.read().splitlines()     
    
    total_count = 0

    for word in data:       
        repeat_found = False

        for index in range(len(word)):                     
            if index > 1:
                if word[index - 2] == word[index]:
                    repeat_found = True
                    break

        if repeat_found:
            for index in range(len(word)):
                if index > 0:
                    search_text = word[index - 1] + word[index]
                    temp_word = word[index + 1:]               
                    if search_text in temp_word:                        
                        total_count = total_count + 1
                        break       

    print(total_count)

if __name__ == "__main__":
    nice_count2()