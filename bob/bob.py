
def response(hey_bob):
    if hey_bob.strip() == "": return 'Fine. Be that way!'
    if hey_bob == hey_bob.upper() and len([char for char in hey_bob if char.isalpha()]) > 0 and hey_bob.strip()[-1] == '?': return 'Calm down, I know what I\'m doing!'
    if hey_bob == hey_bob.upper() and len([char for char in hey_bob if char.isalpha()]) > 0: return 'Whoa, chill out!'
    if hey_bob.strip()[-1] == '?': return 'Sure.'
    else: return 'Whatever.'
    
print(response("1, 2, 3"))