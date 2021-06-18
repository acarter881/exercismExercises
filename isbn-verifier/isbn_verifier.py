def is_valid(isbn):
    if '-' in isbn:
        isbn = ''.join(isbn.split('-'))

    if len(isbn) != 10: return False
  
    total = 0

    for i in range(len(isbn)):
        try:
            if isbn[i] == 'X':
                total += 10
            else:
                total += int(isbn[i]) * (10-i)
        except ValueError:
            return False 
    
    if total % 11 == 0: return True
    return False