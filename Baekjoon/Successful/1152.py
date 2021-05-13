#1152

words = 1
line = input()
for i in line:
    if i == ' ':
        words += 1
if line[0] == ' ':
    words -= 1
if line[-1] == ' ':
    words -= 1
print(words)