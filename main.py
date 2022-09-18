import string
def is_palindrome(text):
    text_arr = text.lower()
    for x in text_arr:
        if x in string.punctuation:
            text_arr= text_arr.replace(x,"")
    carr= list(text_arr)
    carr.reverse()
    arr ="".join(carr)
    text_arr = text_arr.split()
    arr = arr.split()

    karr= ''.join(text_arr)
    bar = ''.join(arr)
    if karr == bar:
        print(True)
    else:
        print(False)



is_palindrome('A')