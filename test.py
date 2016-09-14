
with open("sample.txt") as open_holmes:
    holmes = open_holmes.read()
# working

holmes_scrubbed = holmes.lower()
# working

# holmes_scrubbed = holmes_scrubbed.strip('/n')

loseit = ',.)(:\'#%$@]["!?/*;'
for stupid_thing_in_the_way in loseit:
    holmes_scrubbed = holmes_scrubbed.replace(stupid_thing_in_the_way, '').replace('\n', ' ')

holmes_scrubbed = holmes_scrubbed.split(' ')

# print(holmes_scrubbed)

# not_good = ['a', 'able', 'about', 'across', 'after', 'all', 'the', 'of', 'for']

words_in_holmes = {}

for wordin in holmes_scrubbed:
    if wordin in words_in_holmes.keys():
        words_in_holmes[wordin] += 1
    else:
        words_in_holmes[wordin] = 1


final_list = (sorted(words_in_holmes.items(), key=lambda x: x[1]))

print(final_list)
# final_list = final_list[::-1]

# for item, item_val in final_list():
#    print(item + ": " + str(item_val))
