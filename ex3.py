def getfreq(string):
    #makes all the elements of the string lowercase
    string = string.lower()
    #removes whitespaces from string
    string = string.replace(" ", "")

    freq = {}  
    #counts number of times a certain letter occurs  
    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

# assigns "hello world" to string
string = "hello world"

#prints result of the function
print(getfreq(string))