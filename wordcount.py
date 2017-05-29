word_count = {}

f = open("twain.txt")
for line in f:
    line = line.strip()
    line = line.strip(',')
    line = line.split(' ')
    
    for word in line:
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1
        # if word in word_count:
        #     word_count[word] += 1
        # else:
        #     word_count[word] = 1

for word, count in word_count.iteritems():
    print "{} {}".format(word, count)
# print word_count
