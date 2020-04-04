'''Merge the Tools!
https://www.hackerrank.com/challenges/merge-the-tools/problem
problem - Enter a string of length n and break it into n/k parts, and then
remove the repeating alphabets
input format: a string and a integer in next line
'''

def merge_the_tools(string, k):
    list=[]
    str=''

    for i in range(0,len(string),k):
        list.append(string[i:i+k])

    for e in list:
        for i in e:
            if(i not in str):
                str+=i
        print(str)
        str=''

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
