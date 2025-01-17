book = "books/frankenstein.txt"

def main():
    with open(book) as f:
        file_contents = f.read()
        #print(file_contents)
        #print("\n")
        #print(word_count(file_contents))
        #print("\n")
        #print(cha_count(file_contents))
        report_print(file_contents)



    return 0

def word_count(text):
    count = 0
    words = text.split()
    for word in words:
        count +=1
    return count

def cha_count(text):
    count = {}
    for char in text:
        if char.lower() not in count:
            count[char.lower()] = 1
        else:
            count[char.lower()] += 1
    return count

def report_print(text):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count(text)} words found in the document")
    print("\n")
    dic = cha_count(text)
    for key in dic:
        if key.isalpha():
            print(f"The '{key}' character was found {dic[key]} times")
    return 0

main()
