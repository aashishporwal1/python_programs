
def longest_word(lst):
    max_len=len(lst[0])
    longest=lst[0]

    for i in lst:
        if len(i)>max_len:
            max_len=len(i)
            longest=i
    print("Longest word is :",longest)

lst=["hey","what","you","doing",'tomorrow']
longest_word(lst)
