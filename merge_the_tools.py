def merge_the_tools(string, k):
    i = 0
    while i < len(string):
        substring = string[i:i+k]
        for char in set(substring):
            print(char, end="", sep="")
        print()
        i += k
merge_the_tools("addkdbooo",3)