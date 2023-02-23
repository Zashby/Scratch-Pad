import string

def striplist(texts):
    from string import punctuation
    punc = list(punctuation) + [" ", "\n", "\r"]
    for x in punc:
        texts = texts.replace(x, "")
    return texts

def rot_cipher_lite(plain_text, rot):
    alphabet = []
    for x, y in zip(string.ascii_lowercase, string.ascii_uppercase):
        alphabet.append(x)
        alphabet.append(y)
    punc_list = list(string.punctuation)
    num_list = list(string.digits)
    plain_list = list(plain_text)
    for l in range(len(plain_list)):
        if plain_list[l] in alphabet:
            plain_list[l] = alphabet[(alphabet.index(plain_list[l])+(rot*2))%len(alphabet)]
        if plain_list[l] in punc_list:
            plain_list[l] = punc_list[(punc_list.index(plain_list[l])+rot)%len(punc_list)]
        if plain_list[l] in num_list:
            plain_list[l] = num_list[(num_list.index(plain_list[l])+rot)%len(num_list)]

def snail(snail_map):
    array = []
    while snail_map!= []:
        array += snail_map.pop(0)
        if snail_map!= []:
            last_array = snail_map.pop(len(snail_map)-1)
            last_array.reverse()
            for x in snail_map:
                array.append(x.pop(len(x)-1)) 
            array += last_array
            for x in range((len(snail_map))-1,-1,-1):
                array.append(snail_map[x].pop(0))
        
    return array


def dataSetEdit(file_path, *args):
    with open(file_path) as file:
        read=file.read()
        words = read.split(",")
        for i ,word in enumerate(words):
            for arg in args:
                if arg in word:
                    words[i]=word.replace(arg, "")
        read = ",".join(words)

    with open(file_path,'w') as file:
        file.write(read)



            # if arg in word:
            #     words[i]=word[:word.index(arg)]

def pangramCheck(str):
    str=str.lower()
    check = list(string.ascii_lowercase)
    for x in str:
        if x in check:
            check.pop(check.index(x))
    if not check:
        return 'pangram'
    else:
        return 'not pangram'
    
    