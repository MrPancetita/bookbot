def word_counter(string):
    word_count = len(string.split())
    return word_count  
    
def word_dictionary(string):
    word_dict = {}
    words = string.split()
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def character_dictionary(string):
    char_dict = {}
    for char in string:
        char_lower = char.lower()
        if char_lower in char_dict:
            char_dict[char_lower] += 1
        else:
            char_dict[char_lower] = 1
    return char_dict

def report_generator(path_to_file, file_contents):
    word_count = word_counter(file_contents)
    char_dict = character_dictionary(file_contents)
    
    report = f"--- Begin report of {path_to_file} ---\n"
    report += f"Word count: {word_count}\n\n"
    report += "Character count by character:\n"

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char, count in char_dict.items():
        if char in alphabet:
            report += f"The character '{char}' was found {count} times\n"
    return report



def main(): 

    path_to_file = "./books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read() 
        print (report_generator(path_to_file, file_contents))
 
main()


