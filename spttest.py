def countc(s, c):
    found = 0
    for i in range(len(s)):
        if s[i] == c:
            found += 1
    return found


if __name__ == "__main__":
    print(countc("helen", "a")) 
