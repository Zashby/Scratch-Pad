def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    index_list = []
    for i, doc in enumerate(doc_list):
        check = doc.lower().split(' ')
        for word in check:
            test = word.replace(',',"")
            test = test.replace('.',"")
            if keyword.lower() == test:
                index_list.append(i)
    return index_list
    pass
    


print(word_search(['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?'], 'car'))
