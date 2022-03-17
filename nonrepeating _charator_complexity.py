from collections import Counter
def nonrepeatchar(string):
   charactor=Counter(string)
   for i in string:
      if(charactor[i]==1):
         print(i)
         break
string="geeksforgeeks"
nonrepeatchar(string)