
def split_text_per_sign(text, signs_per_line):
    centred_text = []
    row = text[0]
    for word in text[1:]:
        if len(row + " " + word) > signs_per_line:
            centred_text.append(row)
            row = word
        else:
            row = row + " " + word

    centred_text.append(row)
    return centred_text



def center_text(lenght_of_the_line, text):
    centred_text = []
    for line in text:
        num_space = (lenght_of_the_line - len(line)) // 2
        line = num_space * (" ") + line + num_space * (" ")
        centred_text.append(line)

    return centred_text



def main():
    text = []
    centred_text = []
    lenght_of_the_line = int(input("Enter lenght of line: "))
    signs_per_line = int(input("Enter num of signs per line: "))
    while True:
        line = input("")
        if line == "":
            break
        text = text + line.split()


    centred_text = split_text_per_sign(text, signs_per_line)
    centred_text = center_text(lenght_of_the_line, centred_text)

    for x in centred_text:
        print(x)

if __name__ == '__main__':
    main()