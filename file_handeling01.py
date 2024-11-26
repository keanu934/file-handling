def main():
 # opening a file

    # r means read, w means write, and a means append
    garfield_file = open("garfield.txt", "r")
    # garfield_data = garfield_file.read()
    # print(garfield_data)

    print("now printing line by line")
    for line in garfield_file:
        print(line, end="")


if __name__ == "__main__":
    main()
