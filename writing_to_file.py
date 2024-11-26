def main():
    while True:
        resp = input("Tell me something about odie: ")
        if resp.strip().lower() == 'q':
            break
        else:
            file = open("odie.txt", "a")
            file.write(f"{resp} + \n")
            file.close()


def write_list_to_file():
    about_odie = ["he's yella\n", "he's garfield's friend\n",
                  "his girlfriend is a brush\n"]

    file = open("odie.txt", "w")
    file.writelines(about_odie)
    file.close()


if __name__ == "__main__":
    # main()
    write_list_to_file()
