def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)
    return same_words


result1 = single_root_words('Rich', 'riChiest', 'orIchalcum', 'cheers', 'ricHies')
result2 = single_root_words('DiSabLement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)