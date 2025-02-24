# count the no of vowels in the given string

def countNoOfVowels(str,count=0):

    for ch in str:
        if ch.lower() in ["a","e","i","o","u"]:
            count +=1
    return count


str="piyushkumarsinha"
total=countNoOfVowels(str)
print(total)

