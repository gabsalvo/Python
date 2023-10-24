from collections import Counter

def equalFrequency(word):
    count=Counter(word)
    dictionary=dict(count)

    frequence = list(dictionary.values())
    unique_freq = set(frequence)

    if len(unique_freq) == 2:
        min_freq = min(unique_freq)
        max_freq = max(unique_freq)

        if max_freq - min_freq == 1 and frequence.count(max_freq) == 1:
            return True
    return False    

print(equalFrequency('niceeee'))
print(equalFrequency('nicee'))

