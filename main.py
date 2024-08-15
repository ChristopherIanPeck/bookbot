def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        return file_contents
        print("file read")


def num_words(file_contents):
    n_words = len(file_contents.split())

    print(n_words)


if __name__ == "__main__":
    contents = main()
    num_words(contents)
