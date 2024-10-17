def reverseWords(str):
    words = str.split()
    result = []
    for word in words:
        chars = list(word)
        result.append("".join(chars[::-1]))

    return " ".join(result)

if __name__ == "__main__":
    result = reverseWords("The cat in the hat")
    print(result)