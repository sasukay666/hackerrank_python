# Selection Sort
def selection_Sort(l)
  for i in range(len(l)-1):
      for j in range(i, len(l)):
          if l[i]>l[j]:
              l[i], l[j] = l[j], l[i]
  return l

# Program to sort a string using Selection Sorting method
def swap(string, i, j):
    tempi, tempj = string[i], string[j]
    return string[:i] + tempj + string[i+1:j] + tempi + string[j+1:]
def stringSort(stre):
    for i in range(len(stre)-1):
        for j in range(i, len(stre)):
            if ord(stre[i]) > ord(stre[j]):
                stre = swap(stre, i, j)
    return stre
if __name__ == '__main__':
    stre = input("Enter a string to sort: ")
    print(stringSort(stre), 'is the sorted string')
