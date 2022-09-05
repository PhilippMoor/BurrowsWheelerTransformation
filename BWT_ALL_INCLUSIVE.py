import math
import random
import time
import matplotlib
import matplotlib.pyplot as plt
random.seed(1)
class Word():
    def __init__(self,string,name=''):
        self.name = name
        self.string = string
        self.letters = self.find_distinct_letters(self.string)
        self.number_of_runs = 0
        self.is_palindromic = 0
        self.factors = []
        self.distinct_factors = []
        self.pal_factors = []
        self.conjugates = []
        # Initialization Process
        self.number_of_runs = self.find_number_of_runs(self.string)
        self.is_palindromic = 0
        self.conjugates = self.find_conjugates(self.string)
        self.short = self.shorten(self.string)
    def find_distinct_letters(self,string):
        distinct_letters = []
        for character in list(string):
            if not character in distinct_letters:
                distinct_letters.append(character)
        return distinct_letters
    def find_number_of_runs(self,word):
        n = 1
        current = word[0]
        for i in range(1,len(word)):
            if word[i] == current:
                continue
            else:
                n += 1
                current = word[i]
        return n
    def find_factors(self,word):
        n = len(word)
        list_of_factors = []
        list_of_distinct_factors = []
        list_of_palindromic_factors = []
        for i in range(1,n+1):
            for j in range(n+1-i):
                string = word[j:j+i]
                list_of_factors.append(string)
                if not string in list_of_distinct_factors:
                    list_of_distinct_factors.append(string)
                if string == string[::-1]: # inverse
                    list_of_palindromic_factors.append(string)
        self.factors = list_of_factors
        self.distinct_factors = list_of_distinct_factors
        self.pal_factors = list_of_palindromic_factors
        return
    def find_conjugates(self,word):
        conj = [word]
        n = len(word)
        count = 0
        while 1:
            count += 1
            if count == n:
                break
            word = self.rotate_right(word)
            conj.append(word)
        return conj
    def rotate_right(self,word):
        n = len(word)
        return word[n-1] + word[:n-1]
    def reverse(self,word):
        n = len(word)
        reversed_word = ''
        for i in range(n):
            reversed_word += word[n-i-1]
        return reversed_word
    def bwt(self,word):
        bwt = ''
        word.conjugates.sort()
        for conjugate in word.conjugates:
            bwt += conjugate[len(conjugate)-1]
        index = word.conjugates.index(word.string) + 1
        return [Word(bwt),index]
    def compression_ratio(self):
        rho_1 = self.bwt(self)[0].number_of_runs
        rho_2 = self.number_of_runs
        return round(rho_1 / rho_2,ndigits=3)*100
    def shortening_ratio(self):
        mu_1 = len(self.bwt(self)[0].short)
        mu_2 = len(self.short)
        return round(mu_1/mu_2,ndigits=3)*100
    def shorten(self, word):
        short = ''
        word_list = list(word)
        chunks = []
        new_chunk = []
        for character in word_list:
            if len(new_chunk) == 0:
                new_chunk.append(character)
                continue
            if character in new_chunk:
                new_chunk.append(character)
                continue
            else:
                chunks.append(new_chunk)
                new_chunk = [character]
        chunks.append(new_chunk)
        for chunk in chunks:
            if len(chunk) > 2:
                short += chunk[0]
                short += str(len(chunk))
            if len(chunk) == 2:
                short += chunk[0]
                short += chunk[1]
            if len(chunk) == 1:
                short += chunk[0]
        return short
    def analysis(self,word,analyzefactors = 0):
        if analyzefactors:
            self.find_factors(self.string)
            string = f"The << {self.name} >> " \
                     f"\n  - has string: {word.short}" \
                     f"\n  - has length: {len(word.string)}" \
                     f"\n  - has {word.number_of_runs} runs" \
                     f"\n  - has BWT: {word.bwt(word)[0].short}" \
                     f"\n  - with length {len(word.bwt(word)[0].short)}" \
                     f"\n  - and {word.bwt(word)[0].number_of_runs} runs in the bwt" \
                     f"\n  - the run_compression_rate is: {word.compression_ratio()}%" \
                     f"\n  - the shortening_ratio is {word.shortening_ratio()}%" \
                     f"\n  - has {len(word.factors)} factors" \
                     f"\n  - has {len(word.pal_factors)} palindromic factors " \
                     f"\n  - ratio palindromic factors to all: {int(round(len(word.pal_factors)/len(word.factors),2)*100)}% \n"
        else:
            string = f"The << {word.name} >> " \
                     f"\n  - has string: {word.short}" \
                     f"\n  - has length: {len(word.string)}" \
                     f"\n  - has {word.number_of_runs} runs" \
                     f"\n  - has BWT: {word.bwt(word)[0].short}" \
                     f"\n  - with length {len(word.bwt(word)[0].short)}" \
                     f"\n  - and {word.bwt(word)[0].number_of_runs} runs in the bwt" \
                     f"\n  - the run_compression_rate is: {word.compression_ratio()}%" \
                     f"\n  - the shortening_ratio is {word.shortening_ratio()}%\n"
        return string
    def find_unique_consecutive_appearances(self):
        self.find_factors(self.string)
        double_factor_list = []
        for factor in self.factors:
            n = len(factor)
            if not n%2 == 0:
                continue
            else:
                if factor[:int(n/2)] == factor[int(n/2):]:
                    if not factor[:int(n/2)] in double_factor_list:
                        double_factor_list.append(factor[:int(n/2)])
        return double_factor_list



class CreateWord(Word):
    def randomword(alphabetlist = [],wordlength = 1,name=''):   #maybe add randomlength
        random_word = ''
        for i in range(wordlength):
            random_word += random.choice(alphabetlist)
        return Word(random_word,name)
    def morphismword(alphabetlist = [],morphismlist = [],start = '',number_of_iterations=1,name=''):
        if not len(alphabetlist) == len(morphismlist):
            print("MORPHISM NOT WELL DEFINED")
            return 0
        random_word = start
        counter = 0
        while 1:
            new_word = ''
            if counter == number_of_iterations:
                break
            for character in random_word:
                new_word += morphismlist[alphabetlist.index(character)]
            random_word = new_word
            counter += 1
        return Word(random_word,name)
    def permute(permutation,input_string):
        alphabet = ["A","B","C","D"]
        new_string = ""
        for char in input_string:
            index = alphabet.index(char)
            new_string += permutation[index]
        return new_string
    def expand(input_string,diagram_number):
        d_1 = [["DA","DA"],["AC","ADBC"],["CB","CB"],
               ["BB","BCCB"],["BC","BC"],["CA","CBDA"],["AD","AD"]] # check (Y)
        d_2 = [["DC", "DBC"], ["CA", "CBDA"], ["AB", "ADBCCB"],
               ["BB", "BCCB"], ["BA", "BCCBDA"], ["AC", "ADBC"], ["CD", "CBD"]]
        d_3 = [["CD", "CBD"], ["DB", "DBCCB"], ["BA", "BCCBDA"],
               ["AA", "ADBCCBDA"], ["AB", "ADBCCB"], ["BD", "BCCBD"], ["DC", "DBC"]]
        d_4 = [["CB", "CCB"], ["BD", "BCCBD"], ["DA", "DBCCBDA"],
               ["AA", "ADBCCBDA"], ["AD", "ADBCCBD"], ["DB", "DBCCB"], ["BC", "BCC"]]
        d_5 = [["BC", "BCC"], ["CA", "CCBDA"], ["AD", "ADBCCBD"],
               ["DD", "DBCCBD"], ["DA", "DBCCBDA"], ["AC", "ADBCC"], ["CB", "CCB"]]
        d_6 = [["BA", "BDA"], ["AC", "ADBCC"], ["CD", "CCBD"],
               ["DD", "DBCCBD"], ["DC", "DBCC"], ["CA", "CCBDA"], ["AB", "ADB"]]
        d_7 = [["AB", "ADB"], ["BD", "BD"], ["DC", "DBCC"],
               ["CC", "CC"], ["CD", "CCBD"], ["DB", "DB"], ["BA", "BDA"]]
        diag_list = [d_1,d_2,d_3,d_4,d_5,d_6,d_7]
        valid = []
        for d in diag_list:
            l = []
            for entry in d:
                l.append(entry[0])
            valid.append(l)
        diag = diag_list[diagram_number-1]
        valid = valid[diagram_number-1]
        new_string = ""
        for i in range(len(input_string)-1):
            checkstr = input_string[i]+input_string[i+1]
            if not checkstr in valid:
                print(f" {checkstr} not in Diagram {diagram_number} {valid}")
            for x in diag:
                if x[0] == checkstr:
                    new_string += x[1][:-1]
        new_string += input_string[-1]
        return str(new_string)
    def expand_binary(input_string,diagram_number):
        d_1 = [["BA", "BA"], ["AA", "ABA"], ["AB", "AB"]]
        d_2 = [["BA", "BA"], ["AA", "ABA"], ["AB", "AB"]]
        d_3 = [["AB", "AB"], ["BB", "BB"], ["BA", "BA"]]
        diag_list = [d_1,d_2,d_3]
        valid = []
        for d in diag_list:
            l = []
            for entry in d:
                l.append(entry[0])
            valid.append(l)
        diag = diag_list[diagram_number-1]
        valid = valid[diagram_number-1]
        new_string = ""
        for i in range(len(input_string)-1):
            checkstr = input_string[i]+input_string[i+1]
            if not checkstr in valid:
                print(f" {checkstr} not in Diagram {diagram_number} {valid}")
            for x in diag:
                if x[0] == checkstr:
                    new_string += x[1][:-1]
        new_string += input_string[-1]
        return str(new_string)
    def permutation_to_i(i):
        permutation_list = ["ABCD","DCBA","DABC","CBAD","CDAB","BADC","BCDA","ADCB"]
        #permutation_list = ["ABCD", "DCBA", "BCDA", "CBAD", "CDAB", "BADC", "DABC", "ADCB"]  #new version
        permutation = permutation_list[i]
        #print(f"permutation to D_{i} with {permutation_list[i]}")
        return permutation
    def permutation_to_i_binary(i):
        permutation_list = ["AB","BA","BA","AB"]
        permutation = permutation_list[i]
        print(f"permutation to D_{i} with {permutation_list[i]}")
        return permutation
    def octagonword(sequence_list=[],input_string = "BA",name="generic_name"):
        current = input_string
        for i in range(len(sequence_list)):
            diagram = sequence_list[i]
            if i < len(sequence_list)-1:
                next_diagram = sequence_list[i+1]
                expanded = CreateWord.expand(current,diagram)
                permutation = CreateWord.permutation_to_i(next_diagram)
                permuted = CreateWord.permute(permutation,expanded)
                current = permuted
            else:
                expanded = CreateWord.expand(current, sequence_list[-1])
                current = expanded
        return Word(current,name)
    def binary_word(sequence_list=[],input_string = "BA",name="generic_name"):
        current = input_string
        for i in range(len(sequence_list)):
            diagram = sequence_list[i]
            if i < len(sequence_list)-1:
                next_diagram = sequence_list[i+1]
                expanded = CreateWord.expand_binary(current,diagram)
                permutation = CreateWord.permutation_to_i_binary(next_diagram)
                permuted = CreateWord.permute(permutation,expanded)
                current = permuted
            else:
                expanded = CreateWord.expand_binary(current, sequence_list[-1])
                current = expanded
        return Word(current,name)
    def repetitionword(input_word,number_of_rep = 1,name=''):
        repeated_word = input_word*number_of_rep
        return Word(repeated_word,name)

def helper_function_diagrams(diagram=[['B','A'],['A','A'],['A','B']],iterations=15,start='A'):
    word = start
    for i in range(iterations):
        last_char = word[len(word)-1]
        while 1:
            random_transition = diagram[random.randint(0,len(diagram)-1)]
            if random_transition[0] == last_char:
                word = word + random_transition[1]
                break
    return word
def helper_function_derivate(input_string,rule='sandwich'):
    output_string = ''
    if rule == 'sandwich':
        for i in range(1,len(input_string)-1):
            if input_string[i-1] == input_string[i+1]:
                output_string = output_string + input_string[i]
    if rule == 'oneblock':
        for i in range(len(input_string)):
            if input_string[i] == input_string[i+1]:
                output_string = output_string + input_string[i]
    return output_string
