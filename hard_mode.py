
with open("sample.txt") as open_holmes:
    holmes = open_holmes.read()

holmes_scrubbed = holmes.lower()


loseit = ',.)(:\'#%$@]["!?/*;'
for stupid_thing_in_the_way in loseit:
    holmes_scrubbed = holmes_scrubbed.replace(stupid_thing_in_the_way, '').replace('\n', ' ')

holmes_scrubbed = holmes_scrubbed.split(' ')


words_in_holmes = {}

bad_word = """a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,
because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,
for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,
it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,
not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,
since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,
twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,
would,yet,you,your"""

bad_word = bad_word.replace('\n', ',')
bad_word = bad_word.split(',')


for wordin in holmes_scrubbed:
    if wordin in bad_word:
        pass
    elif wordin in words_in_holmes.keys():
        words_in_holmes[wordin] += 1
    else:
        words_in_holmes[wordin] = 1


final_list = (sorted(words_in_holmes.items(), key=lambda x: x[1]))

final_list_20 = final_list[-21:-1]
final_list_20 = reversed(final_list_20)

count = 0

# for word, number in final_list_20:
#     new_num = (number/50)
#     print(word + ': ' + '#' * new_num)

for word, number in final_list_20:
    print(word)
    print(number)
