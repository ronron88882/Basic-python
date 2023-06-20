text = "How I want a drink, alcoholic of course, after the heavy chapters involving quantum mechanics. All of thy geometry, Herr Planck, is fairly hard."
words = text.split()
word_length = [len(word) for word in words]

print(word_length)

answer = ''.join(map(str, word_length))

answer
