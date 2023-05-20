
"""
#  Pause timer:
import time
count = 0
if count % 50 == 0 :
  print('Pausing...')
  time.sleep(2.5)


print("Heloo")
#for loop - sample
for i in [5, 4, 3, 2, 1] :
  print (i)

#  for loop_with strings -sample
friends = ["Joza", "Bane" , "Mika"]
for i in friends :
  print("Hello ",i)
print ("Finish")

#  loop ideoms -mamking msrt loop
print("Before:")
for i in [9,41,12,3,74,14] :
  print("")
  print("go: ",i)
  print("")
  print ("next...")
print("Done!")

#  What is the largest number

largest_so_far = -1
print("Before" , largest_so_far)
for i in [9, 41, 12, 3, 74, 15] :
  if i > largest_so_far :
    largest_so_far = i
  
  print("Loop:", largest_so_far, i)
  print("After", largest_so_far)
print("The largest number is:", largest_so_far)

#  Print the smallest number
smallest = None
print("Before:", smallest)
for number in [9, 41, 12, 7, 74, 3, 15]:
    if smallest is None or number < smallest:
        smallest = number
        #break
    print("Loop:", number, smallest)
    print("Smallest:", smallest)

print("The smallest number in loop is:", smallest)

#  Finding the smallest value
smallest = None
print("Before" , smallest)
for value in [9, 41, 12, 3, 74, 15, 7] :
  if smallest is None :
    smallest = value
  elif value < smallest :
    smallest = value
  print(smallest, value)
  print("Loop:", smallest, value)
  print("After", smallest)
print("The smallest number is:", smallest)




#  Counting in a loop
zork = 0
print("Before", zork)
for i in [9, 41, 12, 3, 74, 15] :
  zork = zork + 1
  print("Loop:", zork, i)
print("After", zork)

#  Summing in a Loop 
zork = 0
print("Before", zork)
for i in [9, 41, 12, 3, 74, 15] :
  zork = zork + i
  print("Loop:", zork, i)
print("After", zork)

#  Finding the Average in a Loop
count = 0
sum = 0
print("Before", count, sum)
for value in [9, 41, 12, 3, 74, 15] :
  count = count + 1
  sum = sum + value
  print(count, sum, value)
print("After", count, sum , sum / count)

#  Filtering in a Loop
print("Before")
for value in [9, 41, 12, 3, 74, 15] :
  if value > 20 :
    print("Large number", value)
print("After")

#  Search Using a Boolean Variable
found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15] :
  if value == 3 :
    found = True 
  print(found, value)

print("After" ,found)

#  https://www.youtube.com/watch?v=kjxXZQw0uPg _sample one
num = 0 
tot = 0.0
while True :
  string_val = input("Enter a number: ")
  if string_val == "done" :
    break
  #try:
  floating_point_val = float(string_val)
  print("The answer is: ", floating_point_val)
  #except: 
   # print("Invalid input")
    #continue
  
  num = num + 1
  tot = tot + floating_point_val
print ("ALL DONE")
print(tot, num, tot/num)



#      _sample two
num = 0 
tot = 0.0
while True :
  string_val = input("Enter a number: ")
  if string_val == "done" :
    break
  try:
    floating_point_val = float(string_val)
  #print("The floating number is: ", floating_point_val)
  except: 
    print("Invalid input")
    continue
  num = num + 1
  tot = tot + floating_point_val
#print ("ALL DONE")
print(tot, num, tot/num)


#  STRINgS """"""""""""""
string = "123"
#string = string + 1  ---------no good couse (string)need integer transformation
add = int(string) + 1
print(add)


name = input("Writte you name and than press Enter: ")
print("Wellcome",name)
apple = input("Enter a number: ")
x = int(apple) - 10
print(x)
print("I take ten for my memory")
apple = input("Enter a number again: ")
x= int(apple) + 10 
print("now i will return to you ten from my memory.... Thnx for helping me")
print(x)


fruit ="banana"
print(fruit)
print(len(fruit))
letter = fruit[1]
print(letter)

x = 3
w = fruit[x -1]
print(w)


#  Looping Through Strings, using WHILE index
fruit = "banana"
index = 0
while index < len(fruit) :
  letter = fruit[index]
  print(index, letter)
  index = index + 1

#  Using FOR statement
fruit ="banana"
for letter in fruit :
  print(letter)

fruit ="orange"
for i in fruit :
  #print(fruit)
  print(i)

#  WHILE and FOR Loop
fruit ="banana"
for letter in fruit :
  print(letter)

index = 0
while index < len(fruit) :
  letter = fruit[index]
  print(letter)
  index = index + 1
 
#  Looping and Counting
word = "banana"
count = 0
for letter in word :
  if letter == "b" :
    count =count + 1
print(count)

for n in "banana":
    print(n)
   
#  Slicing Strings
s = "Monty Python"
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[:])
print(s[8:])
 
#  Using IN as a logical operator
fruit = "banana"      #CODE DOESNT WORK True and False not show
"n" in fruit
"m" in fruit
"nan" in fruit 
if "a" in fruit :
  print("Found it")
  
#  String Comparison
word = "ananas"
if word == "banana" :
  print("All right, bananas.")
if word < "banana" :
  print("Your word, " + word + ", comes before banana.")
elif word > "banana" :
    print("Your word, " + word + ", comes after banana.")
else: 
    print("All right, bananas.")

#  String Library ------------STRING ARE OBJECTS AND HAS METHODS
greet = "Hello Bob"
methodize = greet.lower()
print(methodize)
print(greet)
print("Hi There".lower())

#  Methods
#stuff = "Hello world"
#type(stuff)
#<class "str">
#dir(stuff)
#["capitalize", "casefold", "center", "count", "encode", "endswith", "expandtabs", "find", "format", "format_map", "index", "isalnum", "isalpha", "isdecimal", "isdigit", "isidentifier", "islower", "isnumeric", "isprintable", "isspace", "istitle", "isupper", "join", "ljust", "lower", "lstrip", "maketrans", "partition", "replace", "rfind", "rindex", "rjust", "rpatition", "rsplit", "rstrip", "split", "splitlines", "startswith", "strip", "swapcase", "title", "translate", "upper", "zfill" ]


word = "bananana"
i = word.find("na")
print (i)


#  praxis
str = "X-DSPAM-Confidence: 0.8475"
print(str)
colon = str.find(":")
print(colon)
piece = str[colon+1:]
print(piece)
value = float(piece)
print(value)

#  The newline Character
text = "Hello\nWorld"
print(text)

text = "X\nY"
print(text)

print(len(text)) #"\n"- is the one charachter

#  File Handle
file_handle = open("main.py")
print(file_handle)

#  File Handle as a Sequence
file_to_open = open("main.py")
print(file_to_open)
for open_and_look_file in file_to_open :
  print(open_and_look_file)

#  Simple loop-just to remind myself
text = "orange"
for loop in text :
  print(loop)

#  Counting Lines in a File
file_to_open = open("main.py")
print(file_to_open)
count = 0
for open_and_look_file in file_to_open :
  count = count + 1
  print("open_and_look_file- has:" , count, "lines.")
  
#  Example nuber 2
fhand = open("main.py")
count = 0
for line in fhand:
  count = count + 1
print("Line Count", count)

#  Reading the *Whole* File (newlines and all into a _single string_)
file_to_open = open("main.py")
inp = file_to_open.read()
print(len(inp))
print(inp[:100])
print(inp[:2000])

#  Searching Through a File
find_me = open("main.py")
for line in find_me :
  #line = line.rstrip()  #use this code to "strip" empty line  
  if line.startswith("#") :
    print(line) #like it 


#  Skiping with continue------but i dont see, yet, the maening
find_me = open("main.py")
for line in find_me :
  line = line.rstrip()
  if not "#  String" in line :
    continue
  print(line)

#  Prompt for File Name
file_name = input("Enter a file name: ")
file_name =open(file_name)
count = 0
for line in file_name :
  if line.startswith("#") :
    count = count + 1
print("There were", count, "# lines in", file_name)

#  Bad File Names
fname = input("Enter a file name: ")
try:
  fhand = open(fname)
except:
  print("File cannot be opened: ", fname)
  quit()
count = 0 
for line in fhand:
  if line.startswith("#") :
    count = count + 1
print("There were", count, "# lines in", fname)

# Praxis -opening and look into file-uperrCase method
fh = open("main.py")
print(fh)
for line in fh:
  file = line.rstrip()
  print(file.upper())
  
#  List and mutation and length
list = [2, 4, 6, 1, 9, 7, 100]
print(list)
for loop in list :
  print(loop)
print("done!")
print(list[0])
list[0] = 1000
print(list)
print("The total length of list is: ", len(list))

# Range of Loop - Using the range function
#NOT WORKING LIKE [0,1,2,3]- SOLUTION!!!
f = ["nane","nj", "nin", "neko"]
print(len(f))
print(range(len(f)))


#  Concatenating list using "+"
a = [1, 2, 3 ]
b = [3, 4, 5, 6]
c= a + b
print(c)
print(a)

# Use "slice" to slicing the list
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

 
# List Methods:
#x = list()
#type(x)
#<type "list">
#dir(x)
#["append", "count", "extend", "index", "insert", "pop", "remove", #"reverse", "sort",]

#Building a List from Scrach
#make_list = list()
#make_list.append("book")
#make_list.append(99)
#print(make_list)
#make_list.append("cookie")
#print(make_list)

#  Is something in list?
some = [1, 9, 21, 10, 16]
print(9 in some)
print (15 in some)
print(20 in some)

#  Lists are in Order
names = [ "Mike", "Jack" , "Bob" ]
print(names)
print(names[0])
names.sort()
print(names)
print(names[0])

#  Built-in Functions and Lists
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
#print(sum(nums))  #fix bug line
#print(sum(nums)/len(nums))
      
#Praxis two "same- solution" examples:
#sample 1      #fix code to be complet -to go to next lines
#total = 0
#count = 0
#while True : 
#  inp = input("Enter a number: ")
#  if inp == "done" : break
#  value = float(inp)
#total = total + value
#count = count + 1
#average = total / count
#print("Average", average)

#sample2
#numlist = list()       #fix bug in line
#while True : 
#  inp = input("Enter a number: ")
#  if inp == "done" : break
#  value = float(inp)
#  print(value)
#  numlist.append(value)
#  average = sum(numlist) / len(numlist)
#print("Average: ", average)


#  Best Friens: Strings and Lists 
abc = "With three words"
list = abc.split()
print(list)
print(len(list))
print(list[1])
for loop in list : print(loop)

line = "A lot            of spaces"
etc = line.split()
print(etc)
line = "first;second;third"
thing = line.split()
print(thing)
print(len(thing))
thing = line.split(";")
print(thing)
 
#From stephen.mar@uct.ac.za Sat Jan 6 09:14:16 2008
#fhand = open("mbox-short.txt")


#for line in fhand:
#  line = line.rstrip()
#  if not line.startswith("From ") : 
#    continue
#  words = line.split()
#  print(words[2])  #prints:Sat
#words = line.split()
#email = words[1]
#pieces = email.split("@")
#print(pieces[1])#prints:uct.ac.za__but code doesnt work for now
 
#  Sample of splicing mail
words = 'His e-mail is q-lar@freecodecamp.org'
piece = words.split()
parts = piece[3].split('-')
n_mail = parts[1]
print(parts)
print(parts[1])
print(n_mail)

#  Dictionaries
purse = dict()
purse["money"] = 12
purse["candy"] = 3
purse["tissues"] = 75
print(purse)
print(purse["candy"])
purse["candy"] = purse["candy"] + 2
print(purse)

#  Comparing Lists and Dictionaries
#list = list() #list has a "key"= [0],[1],[2]..etc
#list.append(21)
#list.append(183)
#print(list)
#list[0] = 32
#print(list)

dictionary = dict() #dict has a "key" = ["course"], ["age"]
dictionary["age"] = 23
print(dictionary)
dictionary["course"] = 182
print(dictionary)
dictionary["age"] = 40
print(dictionary)

#  Dictionary Literals (Constants)
jjj = {"chuck" : 1, "fred" : 42, "jan" : 100}
print(jjj)
ooo = {} #empty dictionary
print(ooo)

dict = {"Fri": 20, "Thu": 6, "Sat": 1}
dict["Thu"] = 13
dict["Sat"] = 2
dict["Sun"] = 9
print(dict)

#  Histogram some sample- not so good sample 
#counts = dict()
#names = ["csev", "cwen", "csev", "zqian", "cwen"]
#for name in names : 
#  if name not in counts :
#    counts[name] = 1
#  else : 
#    counts[name] = counts[name] + 1
#print(counts)

#  The "get" method for dictionaries
#counts = dict()
#names = ["csev", "cwen", "csev", "zqian", "cwen"]
#for loop_n in names :
#  counts[loop_n] = counts.get(loop_n, 0) + 1
#  print(counts)
#print("csev" in counts)

#  Simple dictionary test
counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('quincy', 0))
print(counts.get('kris', 0))
print(counts.get('mrugesh', 0))

# Counting patern (histogram)
#counts = dict()
#print("Enter a line of text:")
#line = input("")

#text = line.split()

#print("Words:", text)

#print("Counting...")
#for word in text :
#  counts[word] = counts.get(word,0) + 1
#print('Counts', counts)
#line of text: the clown ran after car and the car ran into the tent and the tent fell down on the clown and he car

# Definite Loops and Dictionaries
counts = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for key in counts:
  print(key, counts[key])

print(counts.keys())
print(counts.values())
print(counts.items())
 
#  Bonus: Two Iteration VAriables! (key-value) pairs
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for aaa,bbb in jjj.items() :
  print(aaa,bbb)

# Another Sample
#name = input('Enter file: ')
#handle = open(name)
#
#counts = dict()
#for line in handle :
#  words = line.split()
#  for word in words :
#    counts[word] = counts.get(word,0) + 1

#bigcount = None
#bigword = None
#for word,count in counts.items() :
#  if bigcount is None or count > bigcount :
#    bigword = wordbigcount = count
#print(bigword, bigcount)

#   test
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])


#  Tuples 
x = ['GLen', 'Saly', 'Jack']
print(x[2])
y = (1, 9, 2)

print(y[0])
print(max(y))
for iter_loop in y:
  print(iter_loop)
# Are "imutable" Unlike a list, once you create a tuple, you CANNOT ALTER its content - similar to string 
x = ('Glen','Sally', 'Joseph')
x = [9, 8, 7]
x[2] = 6
print(x)

y = 'ABC'
#y[2] ='D'
z = (5, 4, 3)
#z[2] = 0

#Things NOTto do with tulips 
x = (3, 2, 1)
#x.sort()
#x.append(5)
#x.reverse()
print('_____________________________')#just a trick to separate praxis
# A Tale of two Sequences
#1 == list()
#dir(1)
#['append', 'count', 'extend','index', 'insert' 'pop', 'remove','reverse', 'sort' ]
#t = tuple()
#dir(t)
#['count', 'index'] 

#Tuples and Asingment
(x,y) = (4, 'freed')
print(y)
print(x)
print(4)
(a,b) = (99, 34)
print(a)

#Tuples and Dictionaries
#d = dict()
#d['csev'] = 2
#d['cwen'] = 4
#for (k,v) in d.items():
#  print(k,v)
  #print(d)
#print(d)
#print(dict)
#print(dict())
#tups = d.items()
#print(tups)

#  Tuples are Comparable
print((0, 1, 2) < (5, 1, 2))
print((0, 1, 20000) < (0, 3, 4))
print(('Jones', 'Sally') < ('Jones', 'Sam'))
print(('Jones', 'Sally') > ('Adams', 'Sam'))

#Praxis
#d = dict()
#d['quincy'] = 1 
#d['beau'] = 5
#d['kris'] = 9
#for (x) in d.items():
#    print(x)

#for (x, y) in d.items():
#    print(x, y)

#  Sorting a List of Tuples
d = {'a':10,  'c':22,'b':1}
print(d.items())
print(sorted(d.items()))

#Using sorted()
print('_________________')
d = {'a':10,'b':1,'c':22}
t = sorted(d.items())
print(t)
#for loop in sorted(d.items()): not good solution
  #print(loop)
for (k,v) in sorted(d.items()): #good solution
  print(k,v)
for k,v in sorted(d.items()):
  print(k,v)


#  Sort by values instead of key
#c = {'a':10, 'b':1, 'c':22}
#tmp = list()
#for k,v in c.items():
#  tmp.append( (v,k) )
#print(tmp)
#tmp = sorted(tmp, reverse = True)
#print(tmp)

#  TOP 10 most common words
#fhand = open('main.py')
#count = dict()
#for line in fhand:
#  words = line.split()
#  for word in words:
#    count[word] = count.get(word, 0 ) + 1


#lst = list()
#for key, val in count.items():
#  newtup = (val,key)
#  lst.append(newtup)
#lst = sorted(lst, reverse=True)
#for val,key in lst[:10] : 
#  print(key,val)
print('__________________________________')

#  EVEN SHORTer VERSION below:
c = {'a':10, 'b':1,'c':22}
print(sorted( [ (v,k) for k,v in c.items() ] ) )

#Praxis
#lst = []
#counts = dict() #This line must be defined
#for key, val in counts.items():
#    newtup = (val, key)
#    lst.append(newtup)
#lst = sorted(lst, reverse=True)
#print(lst)
#print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )
  
#praxixs sample
fname = input ( 'Enter File: ')
if len(fname) < 1 :
  fname = 'main.py'
hand = open(fname)

#di = dict()
#for lin in hand: 
#  lin = lin.rstrip()
#  wds= lin.rstrip()
#  wds = lin.split()
#  for w in wds:
    # idiom : retrieve/create/update counter
#    di[w] = di.get(w,0) + 1

#print(di)

#x = di.items()
#print(x)
#largest = -1
#theword = None
#for k,v in di.items():
#  if v > largest :
#    largest = v
#    theword = k #cature/remember the key that was largest
#print(theword,largest)
#x = sorted(di.items()) 
#print(x[:5])
#tmp = list()
#for k,v in di.items():
  #print(k,v)
#  newt = (v,k)
#  tmp.append(newt)

#print('Fliped', tmp)
#tmp = sorted(tmp,reverse = True)
#print('Sorted',tmp[:5])

#for v,k in tmp[:5] :
#  print(k,v)

#  The Regular Expression Module "regex " "regexcap"

#The regular expression quick guide:
# '^'  Matches the -beginning- of a line
# '$'  Maches the -end- of the line
# '.'  Maches -any- charachter 
# '\s' Maches -whitespace- 
# '\S' Maches any - non-whitespace - character
# '*'  -Repeats- a character zero or more times
# '*?' -Repeats- a character zero or more times (non-gready) 
# '+'  -Repeats- a character one or more times 
# '+?' -Repeats- a character one or more times (non-greedy)
# '[aeiou]' Maches a single character -in- the listed -set- 
# '[^XYZ]'  Maches a single charcter -not in- the listed -set-
# [a-z09]   The set of characters can include in -range-
# '('  Indicates where string -extraction- is to start
# ')'  Indicates where string -extraction- is to end

#notes
# "import re" -imports regular expressions library-
# "re.search" - to see if a string maches a regular expression, similar to usig the find() method for strings
# "re.findall()" to extract a portions of a string that match your regular expression, similar to a combination of find() and slicing: var[5:10]

hand = open('main.py')
for line in hand:
  line = line.strip()
  if line.find('#The regular expression quick guide:') >= 0 :
    print(line)
   
#impport re                      #-broken_code
#hand = open('main.py')
#for line in hand:
#  line = line.rstrip()
#  if re.search('^From:', line) : 
#    print(line)

hand = open('main.py')
for line in hand:
  line = line.rstrip()
  if line.startswith('#') >= 0 :
    print(line)

#  Maching and Extracting Data __"[0-9]+"__one or more digits
import re
x = "My 2 favorite numbers are 19 na 42"
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[MAEIOU]+',x)
print(y)
#_________________________________________________
#  Warning: Greedy Maching-tending to the longest string!
import re
x = "From: Using the : character"
y = re.findall('^F.+:',x)
print(y)

#  Non-Greedy Maching
import re
y = 'From: Using the : character'
y = re.findall('^F.+?:',x)
print(y)

#  Fine-Tuniing String Extraction
import re
x = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('\S+@\S+',x)
print(y)
y = re.findall('^From (\S+@\S+)',x)
print(y)

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)

print(lst)
print('______________________________________________')
#  String Parsing Examples
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

#  The Double Split Pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

words = line.split()
print(words)
email = words[1]
print(email)
pieces = email.split('@')
print(pieces[1])
#the regex version:
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin)
print(y)
#Even Cooler Regex Version
y = re.findall('^From .*@([^ ]*)',lin)
print(y)

#  Spam Confidence
#import re 
#hand = open('mbox-short.txt')
#numlist = list()
#for line in hand: 
#  line = line.rstrip()
#  stuff = refindall('^X-DSPAM-Confidence: ([0-9].+)',line)
#  if len(stuff) !=1 :
#    continue
#    num = float(stuff[0])
#    numlist.append(num)
#
#print('Maximum:', max(numlist))

#  Escape Charachter
import re 
x = 'We just recived $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)
#_____________________________________
  #  Transport Conrol Protocol (TCP)
 
  #TCP Port Numbers:
#"Incoming E-Mail" -----------25        *SMTP-Mail
#                            
#"Login"----------------------23        *Telnet
#                            -22        *SSH-secure
#"Web Server"-----------------80        *HTTP
#                                 -443  *HTTPS-secure
#"Personal Mail Box"----------109 -110  *POP-mail retrieval
#        *FTP-----------------21  -file transver
#        *DNS-----------------53  -domain name
#        *IMAP----------------143/220/993 MAil Retrieval 

#  Python has  built in support for TCP Sockets:

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org',80) )
cmd = 'GET http://data.p4e.org/romeo.txt HTTP/1.0\n\n'.encode()

#SAMPLE2 -url lib:
#import urllib.request.urllib.parse,urllib.error

#fhand = urllib.request.urlopen('http://data.p4e.org/romeo.txt')
#for line in fhand:
#  print(line.decode().strip())
  

while True :
  data = mysock.recv(512)
  if (len(data) < 1) :
    break
    print(data.decode())

mysock.close()

#Representing simple string

print(ord('H'))
print(ord('a'))

# Using -urllib- in Python:
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
  print(line.decode().strip())

#counts = dict()
#for line in fhand:
#  words = line.decode().split()
#  for word in words:
#    counts[word] = counts.get(word, 0) +1
#
#print(counts)

#Reading Web Pages:
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://www.dr-chuck.com/page1htm')
for line in fhand:
  print(line.decode().strip())


#  JSON sample:
import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
print(info[1]['name'])



#  API - Application Program Interface
#http://maps.googleapis.com/maps/api/geocode/json?adress=Ann+Arbor%2C+MI
{
"status": "OK",
 "results": [
   {
     "geometry": {
       "location_type": "APROXIMATE",
        "location": {
          "lat": 42.2808256,
           "lng": -83.7430378
        }
     },
     "adress_components": [
       {
         "long_name": "Ann Arbor",
          "types": [
             "locality",
               "political"
          ],
          "short_name": "Ann Arbor"
       }
     ],
     "formatted_adress": "Ann Arbor, MI, USA",
     "types": [
       "locality",
       "political"
     ]
   }
 ]
}

import urllib.request, urllib.parse, urllib.error
import json

servicurl = 'http:/maps//.googleapis.com/maps/api/geocode/json'

while True:
  adress = input('Enter location: ')
  if len(adress) < 1: break
  url = serviceurl + urllib.parse.urlencode({'adress': adress})

print('Retrieving', url)
uh = urllib.request.uriopen(url)
data = uh.read().decode()
print('Retrieved', len(data),'charachters')

#try:
#  js = json.loads(data)
#except:
#  js = None

#if not js or 'status' not in js or js['status'] != 'OK':
#  print('=== Failure To Retrieve ===')
#  print(data) 
#  continue

lat = js['results'][0]['formatted_address']
print(locaion)

#  Web Scraping-using robots to retreive their content(Beautiful_Soup)


#  Python Objects
#*CLASS- a template---------------------------------Dog
#*METHOD or Message-Adefined capability of class----Bark
#*FIELD or Attribute-A bit of data in class---------length
#*OBJECT or INSTANCE-A particular instance of class-Lassie

class PartyAnimal:
  x=0
  
  def party(self):
    self.x=self.x + 1
    print('So far',self.x)
    
an = PartyAnimal()
print('Type', type(an))
print('dir',dir(an))

an.party()
an.party()
an.party()
an.party()
an.party()

#  A Nerdy Way to Find Capabilities
x = list()
print(type(x))
print(dir(x))

y = 'hi'
print(type(y))
print(dir(y))

# Object Lifecycle -Constuctor-Destructor
class PartyAnimal:
  x = 0 
  def __init__(nastanak) :
    print('I am constructed')

  def party(nastanak) : 
    nastanak.x = nastanak.x + 1
    print('So far',nastanak.x)

  def __del__(nastanak): 
    print('I am destructed',nastanak.x)

an = PartyAnimal()
an.party()
an.party()
an = 42


print('an conatains',an) #object is destructed... only integer left
#an.party() is gone


#  Many Instances
class PartyAnimal : 
  x = 0
  name = ""
  def __init__(self,z) : 
    self.name = z
    print(self.name,"constructed")

  def party(self) : 
    self.x = self.x + 1
    print(self.name,"party count",self.x)

s = PartyAnimal("zSally")
s.party()

j = PartyAnimal("zJim")
j.party()
s.party()
 
#  Praxiy -Object-
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Maya')

q.party()
m.party()
q.party()

#  Inheritance (subclassing,reusing)-write once-reuseManyTimes

class PartyAnimal :
  x = 0
  name = ""
  def __init__(self, nam) :
    self.name = nam
    print(self.name, "constructed")

def party(self) : 
  self.x = self.x + 1
  print(self.name,"party count", self.x)

class FootballFan(PartyAnimal) : 
  points = 0
  def touchdown(self) :
    self.points = self.points + 7
    self.pary()
    print(self.name,"points",self.points)

s = PartyAnimal('Sally')  #something is wrong with code
s.party()

j = FootballFan('Jim')
j.party()
j.touchdown()

#  SQL -the power of databases


#  Data visualisation: Excersise
  #  Geodata_geoload.py:
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy__IDByT70'
if api_key is False:
  serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
else : 
  serviceurl = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
# Additional detail for urlib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
#fh = open("https://github.com/csev/py4e/blob/master/code3/geodata/where.data")
count = 0
for line in fh:
  if count > 200 : 
    print ('Retrieved 200 locations, restart to retrieve more')
    break

  address = line.strip()
  print('')
  cur.execute("SELECT geodata FROM Locations WHERE address= ?",  (memoryview(address.encode()), ))

  try:
    data = cur.fetchone()[0]
    print("Found in database", address)
    continue
  except:
    pass

  parms = dict()
  parms["query"] = address
  if api_key is not False: parms['key'] = api_key
  url = serviceurl + urllib.parse.urlencode(parms)

  print('Retrieving', url)
  uh = urllib.request.urlopen(url, context=ctx)
  data = uh.read().decode()
  print('Retrived', len(data), 'characters', data[:20].replace('\n', ' '))
  count = count + 1 

  try:
    js = json.loads(data)
  except:
    print(data)  #We print in case unicode causes an error
    continue

  if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') : 
    print('=== Failure to retrieve ===')
    print(data)
    break

  cur.execute('''INSERT INTO Locations (address, geodata)
        VALUES (?, ?)''', (memoryview(address.encode()), memoryview(data.encode()) ) )
  conn.commit()
  if count % 10 == 0:
    print('Pausing for a bit...')
    time.sleep(3)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")

# geodump.py
import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js','w', "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur : 
  data = str(row[1].decode())
  try: js = json.loads(str(data))
  except: continue

  if not('status' in js and js['status'] == 'OK') : continue
    
  lat = js["results"][0]["geometry"]["location"]["lat"]
  lng = js["results"][0]["geometry"]["location"]["lng"]
  if lat == 0 or lng == 0 : continue
  where = js ['results'][0]['formatted_address']
  where = where.replace("'","")
  try : 
    print(where, lat, lng)
    
    count = count + 1
    if count > 1 : fhand.write(",\n")
    output = "["+str(lat)+","+str(lng)+", '"+where+"']"
    fhand.write(output)

  except:
    continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
#conn.commit() "hmmm? for SQL library to work"


#More resources: https://github.com/csev/py4e/tree/master/code3

#- Exercise: Geodata

#- Exercise: Gmane Model

#- Exercise: Gmane Spider

#- Exercise: Gmane Viz (vizualization pipewire_histagram)

#- Exercise: Page Rank

#- Exercise: Page Spider

#- Exercise: Page Viz
"""

a