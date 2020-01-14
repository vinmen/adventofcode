import os

def nice_count():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day5.txt") as f:
        data = f.read().splitlines()     

    vowels = ['a','e','i','o','u']
    bad_group = ['ab','cd','pq','xy']
    total_count = 0

    for word in data:        
        vowel_count  = 0
        double_found = False
        bad_group_found = False        

        for index in range(len(word)):
            if word[index] in vowels:
                vowel_count = vowel_count + 1            
            if index > 0:
                if word[index - 1] + word[index] in bad_group:
                    bad_group_found = True
                    break
                if double_found == False and word[index] == word[index - 1]:
                    double_found = True                
        
        if bad_group_found == False and double_found == True and vowel_count >= 3:
            total_count = total_count + 1           

    print(total_count)

if __name__ == "__main__":
    nice_count()