def open_file_txt(file_path):
    with open(file_path) as file:
        print("Opened file")
        file = file.read()
        print(file)
        #words = file.split(",")
        

    print("Closed file")
    # print(words)

def transcribe(list, test_file):
    with open(test_file, "w") as file:
        print("opening file")
        
        file.write(" ".join(list))
    print("Closing file")
    


def open_file_csv(file_path):
    with open(file_path) as file:
        print("Opened file")
        file = file.read()

        
        

    print("Closed file")
    words = file.split(",")
    return words

def edit_file_csv(file_path):
    with open(file_path) as file:
        print("Opened file")
        file = file.read()
        words = file.split(",")
    print("Closed file")
    
    words.pop(4)    

    with open(file_path, "w") as file:
        file.write(",".join(words))
    return words

open_file_txt("test_file.txt")
open_file_csv("test_file.csv")

    

def transcribe(list, test_file):
    with open(test_file, "w") as file:
        print("opening file")
        
        file.write(" ".join(list))
    print("Closing file")
    

edit_file_csv("test_file.csv")