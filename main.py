def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents


def num_strings(file_contents):
    return len(file_contents.split())


def char_count(file_contents):
    lower_string = file_contents.lower()
    num_char = {}
    for char in lower_string:
        if char.isalpha():
            if char in num_char:
                num_char[char] += 1
            else:
                num_char[char] = 1
    return num_char


def convert_and_sort(num_char):
    num_char = list(num_char.items())
    sorted_char = sorted(num_char, reverse=True, key=lambda x: x[1])
    return sorted_char


def report(num_strings, sorted_char):
    print("-- Begin Report --")
    print(f"{num_strings} words found in the document")

    for char, count in sorted_char:
        print(f"The '{char}' chracter was found {count} times")

    print("-- End Report --")


if __name__ == "__main__":
    contents = main()
    n_strings = num_strings(contents)
    char_counts = char_count(contents)
    sorted_chars = convert_and_sort(char_counts)
    report(n_strings, sorted_chars)
