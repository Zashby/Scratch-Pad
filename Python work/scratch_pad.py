def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    hand_dict = {"A":1, 'K':10, 'Q':10, 'J':10, }
    hand_1_total = 0
    hand_2_total = 0
    for card in hand_1:
        if card.isdigit():
            hand_1_total += int(card)
        elif card in hand_dict.keys():
            hand_1_total+= hand_dict[card]
    if 'A' in hand_1 and hand_1_total <= 11:
        hand_1_total += 10
    for card in hand_2:
        if card.isdigit():
            hand_2_total += int(card)
        elif card in hand_dict.keys():
            hand_2_total+= hand_dict[card]
    if 'A' in hand_2 and hand_2_total <= 11:
        hand_2_total += 10
    print(hand_1_total)
    print(hand_2_total)
    
    
    if hand_2_total >= 21 and hand_1_total >= 21:
        return False
    elif (hand_2_total >= 21) or (hand_1_total > hand_2_total and hand_1_total <=21):
        return True
    else: 
        return False

print(blackjack_hand_greater_than(['A', 'K'], ['10', '2', '8', '5', '7']))