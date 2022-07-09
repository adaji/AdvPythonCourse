words = int(input())
dict = []
for i in range(words):
    dict.append(input().split())

sentence = input().split()


out = []
for i in range(len(sentence)):
    for j in range(words):
        if sentence[i] in dict[j]:
            out.append(dict[j][0])
            break
        elif j == words-1:
            out.append(sentence[i])

for x in out:
    print(x, end=' ')
