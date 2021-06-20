def find_anagrams(word, candidates):
    return [thing for thing in candidates if thing.lower() != word.lower() and sorted(thing.lower()) == sorted(word.lower())]

print(find_anagrams('LISTEN', ["Listen", "Silent", "LISTEN"]))