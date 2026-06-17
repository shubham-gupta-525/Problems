distinct_words = {}
times = []

num = int(input())
for i in range(num):
    word = input()
    if word in distinct_words:
        distinct_words[word] += 1
    else:
        distinct_words[word] = 1
        times.append(word)

print(len(times))
no_of_times = [value for key, value in distinct_words.items()]
print(*no_of_times)



