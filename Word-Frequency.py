
with open("sample.txt") as open_holmes:
    holmes = open_holmes.read()

holmes_scrubbed = holmes.lower()


loseit = ',.)(:\'#%$@]["!?/*;'
for stupid_thing_in_the_way in loseit:
    holmes_scrubbed = holmes_scrubbed.replace(stupid_thing_in_the_way, '').replace('\n', ' ')

holmes_scrubbed = holmes_scrubbed.split(' ')


words_in_holmes = {}

for wordin in holmes_scrubbed:
    if wordin in words_in_holmes.keys():
        words_in_holmes[wordin] += 1
    else:
        words_in_holmes[wordin] = 1

final_list = (sorted(words_in_holmes.items(), key=lambda x: x[1]))

final_list_20 = final_list[-21:-1]
final_list_20 = reversed(final_list_20)


for word, number in final_list_20:
    print(word + ': ' + str(number))
