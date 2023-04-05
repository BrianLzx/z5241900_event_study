def process_string(s):
    L = s.split()
    for i, word in enumerate(L):
        if i % 2 == 0:
            L[i] = word.lower()
        else:
            L[i] = word.upper()
    return L