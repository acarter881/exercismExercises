def transform(legacy_data):
    outDict = {}

    for key, value in legacy_data.items():
        for letter in value:
            letter = letter.lower()
            outDict.setdefault(letter, key)

    return outDict