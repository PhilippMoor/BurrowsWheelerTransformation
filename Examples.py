from BWT_ALL_INCLUSIVE import *
import re
import textwrap
import matplotlib.pyplot as plt
random.seed(1)


diagram_1 = [['B','A'],['A','BA'],['A','B']]
diagram_2 = [['B','A'],['A','A'],['A','BB']]
diagram_3 = [['B','BA'],['A','A'],['A','B']]
diagram_4 = [['B','A'],['A','A'],['A','AB']]
diagram_5 = [['B','AA'],['A','A'],['A','B']]
diagram_6 = [['B','A'],['A','BA'],['A','BB']]
diagram_7 = [['B','BA'],['A','BA'],['A','B']]
diagram_8 = [['B','BA'],['A','A'],['A','BB']]


# helper_word = helper_function_diagrams(diagram=diagram_2)
# print(helper_word)
# print(helper_function_derivate(helper_word))

#################################  EXAMPLES  ##################################
fibonacci_word = CreateWord.morphismword(['a','b'],['ab','a'],'a',21,name='Fibonacci word')
thue_morse_word = CreateWord.morphismword(['a','b'],['ab','ba'],'a',5,name='Thue Morse Word')
tribonacci_word = CreateWord.morphismword(['a','b','c'],['ab','ac','a'],'a',5,name='Tribonacci word')
tetranacci_word = CreateWord.morphismword(['a','b','c','d'],['ab','ac','ad','a'],'a',5,name='Tetranacci word')
order_reversing_morphism = CreateWord.morphismword(['a','b','c'],['abacaba','abacab','abac'],'a',5,name='Order reversing word')
composition_thue_sturmian = CreateWord.morphismword(['a','b'],['abba','ab'],'a',5,name='Composition Thue Sturmian')
composition_sturmian_thue = CreateWord.morphismword(['a','b'],['aba','aab'],'a',5,name='Composition Sturmian Thue')
last_example_conclusion = CreateWord.morphismword(['a','b'],['ababba','abba'],'a',5,name='last_example_conclusion')

example_list = [fibonacci_word,thue_morse_word,tribonacci_word,tetranacci_word,order_reversing_morphism,composition_thue_sturmian,composition_sturmian_thue,last_example_conclusion]
#for word in example_list:
    #print(word.analysis(word,analyzefactors=0))

#################################  INPUT EXAMPLE  ##################################
example_word = Word('barbara','barbara')
#print(example_word.bwt(example_word)[0].analysis(example_word))
#print(example_word.bwt(example_word)[0].string)
###################################################################################
t_1 = time.time()
#octagon_example_1 = CreateWord.octagonword([3,5,3,5,3,5],input_string="BA",name="octagon word 1 on s_i = 3,5,3,5,3,5 with init_string = BA") #initial example
#print(octagon_example_1.analysis(octagon_example_1,analyzefactors=0))
delta_1 = time.time()-t_1
#print("it has taken :",round(delta_1,2)," seconds to compute")
#octagon_example_2 = CreateWord.octagonword([3,5,5,1,7,2],input_string="BA",name="octagon word 2 on s_i = 3,5,5,1,7,2 with init_string = BA")
#print(octagon_example_2.analysis(octagon_example_2,analyzefactors=0))
#octagon_example_3 = CreateWord.octagonword([2,3,4,5,6,7],input_string="BA",name="octagon word 3 on s_i = 2,3,4,5,6,7 with init_string = BA")
#print(octagon_example_3.analysis(octagon_example_3,analyzefactors=0))

#octagon_example_4 = CreateWord.octagonword([3,5,4],input_string="BA",name="octagon word 4 on s_i = 3,5,4 with init_string = BA")
#print(octagon_example_4.analysis(octagon_example_4,analyzefactors=0))
#print(octagon_example_4.string)
#print(octagon_example_4.bwt(octagon_example_4)[0].string)

# octagon_half_word = CreateWord.octagonword([5,2,3,4],input_string="AD",name="half octagon word on s_i = 5,2,3,4 with init_string = AD")
# octagon_half_word = CreateWord.octagonword([1,1,1,1,1,1,1,],input_string="AC",name="half octagon word on s_i = 1,1,1,1,1,1,1 with init_string = AC")
# n = len(octagon_half_word.string)
# print(octagon_half_word.analysis(octagon_half_word))
# print("%%%%%%%%%%%%%% SUB WORDS %%%%%%%%%%%%%%%")
# #print(octagon_half_word.find_unique_consecutive_appearances())
# name = 1
# for double_word in octagon_half_word.find_unique_consecutive_appearances():
#     half_word = double_word[:int(len(double_word)/2)]
#     namestring = "halfword " + str(name)
#     half = Word(half_word,name=namestring)
#     name += 1
#     print(half.analysis(half))

#print(octagon_example.string)

####################################### BINARY WORDS ############################################

#binary_example_1 = CreateWord.binary_word([2,1,3,1,3,2,3,2,3,2,2,2,2,2],input_string="ABABABBA",name="binary_word_1 on s_i = 2,1,3,1 with init_string = BA") #initial example
#print(binary_example_1.analysis(binary_example_1,analyzefactors=0))
#print(binary_example_1.string)
#print(binary_example_1.bwt(binary_example_1)[0].string)

#random_binary_1 = CreateWord.randomword(['a','b'],100,name="random binary 100 word")
#print(random_binary_1.analysis(random_binary_1,analyzefactors=0))

#################################################################################################

####################################### REPEATED WORDS ############################################

#repeat_word_1 = CreateWord.repetitionword(input_word="BBABBBAB",number_of_rep=1000,name="repeat word 1")
#print(repeat_word_1.analysis(repeat_word_1,analyzefactors=0))


# ####################################### FOR GRAPHIC USE ############################################
# plot_word = CreateWord.octagonword([2],input_string="AC",name="plot word 1 on s_i = 2 with init_string = AC")
# print(plot_word.number_of_runs)
# print(plot_word.bwt(plot_word)[0].number_of_runs)
# print(plot_word.bwt(plot_word)[0].number_of_runs/plot_word.number_of_runs)
# plot_word = CreateWord.octagonword([2,3],input_string="AC",name="plot word 1 on s_i = 2,3 with init_string = AC")
# print(plot_word.number_of_runs)
# print(plot_word.bwt(plot_word)[0].number_of_runs)
# print(plot_word.bwt(plot_word)[0].number_of_runs/plot_word.number_of_runs)
# plot_word = CreateWord.octagonword([2,3,4],input_string="AC",name="plot word 1 on s_i = 2,3,4 with init_string = AC")
# print(plot_word.number_of_runs)
# print(plot_word.bwt(plot_word)[0].number_of_runs)
# print(plot_word.bwt(plot_word)[0].number_of_runs/plot_word.number_of_runs)
# plot_word = CreateWord.octagonword([2,3,4,5],input_string="AC",name="plot word 1 on s_i = 2,3,4,5 with init_string = AC")
# print(plot_word.number_of_runs)
# print(plot_word.bwt(plot_word)[0].number_of_runs)
# print(plot_word.bwt(plot_word)[0].number_of_runs/plot_word.number_of_runs)
# plot_word = CreateWord.octagonword([2,3,4,5,6],input_string="AC",name="plot word 1 on s_i = 2,3,4,5,6 with init_string = AC")
# print(plot_word.number_of_runs)
# print(plot_word.bwt(plot_word)[0].number_of_runs)
# print(plot_word.bwt(plot_word)[0].number_of_runs/plot_word.number_of_runs)
# plot_word = CreateWord.octagonword([2,3,4,5,6,7],input_string="AC",name="plot word 1 on s_i = 2,3,4,5,6 with init_string = AC")
# print(plot_word.number_of_runs)
# print(plot_word.bwt(plot_word)[0].number_of_runs)
# print(plot_word.bwt(plot_word)[0].number_of_runs/plot_word.number_of_runs)
# plot_word = CreateWord.octagonword([2,3,4,5,6,7,2],input_string="AC",name="plot word 1 on s_i = 2,3,4,5,6 with init_string = AC")
# print(plot_word.number_of_runs)
# print(plot_word.bwt(plot_word)[0].number_of_runs)
# print(plot_word.bwt(plot_word)[0].number_of_runs/plot_word.number_of_runs)
#
#
# print("XXXXXXXXXXXXXXXXXXX")
# ####################################### FOR GRAPHIC USE 2 ############################################
# plot_word = CreateWord.octagonword([1],input_string="BB",name="plot word 2 on s_i = 1 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([1,1],input_string="BB",name="plot word 2 on s_i = 1,1 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([1,1,1],input_string="BB",name="plot word 2 on s_i = 1,1,1 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([1,1,1,1],input_string="BB",name="plot word 2 on s_i = 1,1,1,1 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([1,1,1,1,1],input_string="BB",name="plot word 2 on s_i = 1,1,1,1,1 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([1,1,1,1,1,1],input_string="BB",name="plot word 2 on s_i = 1,1,1,1,1,1 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([1,1,1,1,1,1,1],input_string="BB",name="plot word 2 on s_i = 1,1,1,1,1,1,1 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([1,1,1,1,1,1,1,1],input_string="BB",name="plot word 2 on s_i = 1,1,1,1,1,1,1 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([1,1,1,1,1,1,1,1,1],input_string="BB",name="plot word 2 on s_i = 1,1,1,1,1,1,1 with init_string = AC")
# print(plot_word.analysis(plot_word))
#
# ####################################### FOR GRAPHIC USE 3 ############################################
# plot_word = CreateWord.octagonword([7],input_string="DC",name="plot word 3 on s_i = 7 with init_string = DC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([7,7],input_string="DC",name="plot word 3 on s_i = 7,7 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([7,7,7],input_string="DC",name="plot word 2 on s_i = 7,7,7 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([7,7,7,7],input_string="DC",name="plot word 2 on s_i = 7,7,7,7 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([7,7,7,7,7],input_string="DC",name="plot word 2 on s_i = 7,7,7,7,7 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([7,7,7,7,7,7],input_string="DC",name="plot word 2 on s_i = 7,7,7,7,7,7 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([7,7,7,7,7,7,7],input_string="DC",name="plot word 2 on s_i = 7,7,7,7,7,7,7 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([7,7,7,7,7,7,7,7],input_string="DC",name="plot word 2 on s_i = 7,7,7,7,7,7,7,7 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([7,7,7,7,7,7,7,7,7],input_string="DC",name="plot word 2 on s_i = 7,7,7,7,7,7,7,7 with init_string = AC")
# print(plot_word.analysis(plot_word))
#
# ####################################### FOR GRAPHIC USE 4 ############################################
# # 2563346
# plot_word = CreateWord.octagonword([2],input_string="DC",name="plot word 4 on s_i = 2 with init_string = DC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([2,5],input_string="DC",name="plot word 4 on s_i = 2,5 with init_string = DC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([2,5,6],input_string="DC",name="plot word 4 on s_i = 2,5,6 with init_string = DC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([2,5,6,3],input_string="DC",name="plot word 4 on s_i = 2,5,6,3 with init_string = DC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([2,5,6,3,3],input_string="DC",name="plot word 4 on s_i = 2,5,6,3,3 with init_string = DC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([2,5,6,3,3,4],input_string="DC",name="plot word 4 on s_i = 2,5,6,3,3,4 with init_string = DC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([2,5,6,3,3,4,6],input_string="DC",name="plot word 4 on s_i = 2,5,6,3,3,4,6 with init_string = DC")
# print(plot_word.analysis(plot_word))
#
# ####################################### FOR GRAPHIC USE 5 ############################################
# # 1711771
# plot_word = CreateWord.octagonword([1],input_string="CA",name="plot word 5 on s_i = 1 with init_string = CA")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([1,7],input_string="CA",name="plot word 5 on s_i = 1,7 with init_string = CA")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([1,7,1],input_string="CA",name="plot word 5 on s_i = 1,7,1 with init_string = CA")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([1,7,1,1],input_string="CA",name="plot word 5 on s_i = 1,7,1,1 with init_string = CA")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([1,7,1,1,7],input_string="CA",name="plot word 5 on s_i = 1,7,1,1,7 with init_string = CA")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([1,7,1,1,7,7],input_string="CA",name="plot word 5 on s_i = 1,7,1,1,7,7 with init_string = CA")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([1,7,1,1,7,7,1],input_string="CA",name="plot word 5 on s_i = 1,7,1,1,7,7,1 with init_string = CA")
# print(plot_word.analysis(plot_word))
#
# ####################################### FOR GRAPHIC USE 6 ############################################
# # 2,3,4,1,1,1,1
# plot_word = CreateWord.octagonword([2],input_string="AC",name="plot word 6 on s_i = 2 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([2,3],input_string="AC",name="plot word 6 on s_i = 2,3 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([2,3,4],input_string="AC",name="plot word 6 on s_i = 2,3,4 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([2,3,4,1],input_string="AC",name="plot word 6 on s_i = 2,3,4,1 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([2,3,4,1,1],input_string="AC",name="plot word 6 on s_i = 2,3,4,1,1 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([2,3,4,1,1,1],input_string="AC",name="plot word 6 on s_i = 2,3,4,1,1,1 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([2,3,4,1,1,1,1],input_string="AC",name="plot word 6 on s_i = 2,3,4,1,1,1,1 with init_string = AC")
# print(plot_word.analysis(plot_word))
#
# ####################################### FOR GRAPHIC USE 7 ############################################
# # 2,3,4,1,1,1,1
# plot_word = CreateWord.octagonword([4],input_string="CB",name="plot word 7 on s_i = 2 with init_string = AC")
# print(plot_word.analysis(plot_word))
# plot_word = CreateWord.octagonword([4,4],input_string="CB",name="plot word 7 on s_i = 2 with init_string = AC")
# print(plot_word.analysis(plot_word))
#
# plot_word = CreateWord.octagonword([7,1,7,1,7,1],input_string="CC",name="plot word Graph on s_i = 2 with init_string = CC")
# print(plot_word.analysis(plot_word))


# ratio_list = []
# for double_word in plot_word.find_unique_consecutive_appearances():
#     half_word = double_word[:int(len(double_word)/2)]
#     namestring = "halfword " + str(name)
#     half = Word(half_word,name=namestring)
#     name += 1
#     print(half.analysis(half))
#     ratio_list.append(half.compression_ratio())
#
# print(ratio_list)
# x = [x for x in range(len(ratio_list))]
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.bar(x,ratio_list)
# plt.show()
fib = CreateWord.morphismword(alphabetlist=['A','B'],morphismlist=['AB','A'],start="A",number_of_iterations=5,name="Fibonacci word with 5 iterations")
print(fib.analysis(fib))
random_word = CreateWord.randomword(alphabetlist=['A','B'],wordlength=10,name="binary random word on 10 letters ")
print(random_word.analysis(random_word))
random_word = CreateWord.randomword(alphabetlist=['A','B'],wordlength=20,name="binary random word on 20 letters ")
print(random_word.analysis(random_word))
random_word = CreateWord.randomword(alphabetlist=['A','B'],wordlength=20,name="binary random word on 20 letters ")
print(random_word.analysis(random_word))
random_word = CreateWord.randomword(alphabetlist=['A','B'],wordlength=20,name="binary random word on 20 letters ")
print(random_word.analysis(random_word))




directive_seq = ['A','B','A','A','B','A']
current = "A"
for i in directive_seq:
    if i == 'A':
        word = CreateWord.morphismword(['A','B'],['A','AB'],start=current,number_of_iterations=1)
    else:
        word = CreateWord.morphismword(['A', 'B'],['BA', 'B'], start=current,number_of_iterations=1)
    current = word.string
    print(word.analysis(word))

sequence = "ABABAB"
directive_seq = list(sequence)
current = "A"
for i in directive_seq:
    if i == 'A':
        word = CreateWord.morphismword(['A','B'],['A','AB'],start=current,number_of_iterations=1,name="Directive word")
    else:
        word = CreateWord.morphismword(['A', 'B'],['BA', 'B'], start=current,number_of_iterations=1,name="Directive word")
    current = word.string
    print(word.analysis(word))

example_rep = CreateWord.repetitionword("ABABAABAA",100,name="Abba 10")
print(example_rep.analysis(example_rep))


word_1 = CreateWord.octagonword([3,5,4],"BA",name="word_1")
subwords = word_1.find_unique_consecutive_appearances()
print(subwords)
print(len(subwords))
print(word_1.string)
count = 1
for item in subwords:
    word = Word(item,name=str(count))
    print(word.analysis(word))
    count += 1

benchmark_1 = CreateWord.randomword(["A","B","C","D"],wordlength=10,name="random word 10")
print(benchmark_1.analysis(benchmark_1))
benchmark_1 = CreateWord.randomword(["A","B","C","D"],wordlength=10,name="random word 10")
print(benchmark_1.analysis(benchmark_1))
benchmark_1 = CreateWord.randomword(["A","B","C","D"],wordlength=15,name="random word 15")
print(benchmark_1.analysis(benchmark_1))
benchmark_1 = CreateWord.randomword(["A","B","C","D"],wordlength=15,name="random word 15")
print(benchmark_1.analysis(benchmark_1))


benchmark_2 = CreateWord.repetitionword("BBBABBDCCD",1,name="repetitionword")
print(benchmark_2.analysis(benchmark_2))
benchmark_3 = CreateWord.repetitionword("BBBABBDCCD",100,name="repetitionword 100")
print(benchmark_3.analysis(benchmark_3))


# text Pride and Prejudice, by Jane Austen
with open("book.txt") as book:
    raw_text = str.upper(str(book.readlines()))
    stripped = ''.join(filter(str.isalpha, raw_text))

#print(stripped)
slices = textwrap.wrap(stripped,10000)
count_char = 0
count_rho = 0
count_rho_bwt = 0
count_len_short = 0
count_len_short_bwt = 0
count_word = 1
for slice in slices:

    # unterbrechen
    count_rho = count_rho + 1
    count_len_short = count_len_short + 1
    break
    ##############

    s = Word(slice,name =str(count_word)+" of pride and prejudice" )
    print(s.analysis(s))
    count_char += len(s.string)
    count_rho += s.number_of_runs
    count_rho_bwt += s.bwt(s)[0].number_of_runs
    count_word += 1
    count_len_short += len(s.short)
    count_len_short_bwt += len(s.bwt(s)[0].short)
print(count_char)
print(count_rho)
print(count_rho_bwt)
print(count_rho_bwt / count_rho)
print(count_len_short_bwt)
print(count_len_short)
print(count_len_short_bwt/count_len_short)

example_pres = Word("MAMMAMIA",name="REVERSE")
print(example_pres.analysis(example_pres))