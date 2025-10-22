mySentence="how much wood could a would chuck chuck if a wood chuck could chuck wood"

def word_fequency(mySentence):
    words = mySentence.split()

    counter={}

    for word in words:
      
      if word in counter:
        counter[word] += 1
      else:
        counter[word] = 1
    return counter

print(word_fequency(mySentence))