import sys


# i'm blue da be di da be die
print("\033[0;94m", end='')


def make_path(filename):
    from os.path import expanduser
    home = expanduser("~")
    return home + "/.forgor/" + filename


def list_pages():
    files = get_files()
    if len(files) == 0:
        print("No pages found.")
    else:
        print("Available pages:")
        for file in files:
            print(" • " + file)
    print("Pages are stored in " + make_path(""))


def get_files():
    from os import listdir
    from os.path import isfile, join

    path = make_path("")
    only_files = [f for f in listdir(path) if isfile(join(path, f))]
    return only_files


def forgor(name):
    try:
        f = open(make_path(name), "r")
    except OSError:
        print("Could not read page \"" + name + "\"")
        list_pages()
        return
    text = f.read()
    f.close()
    print(text)


if len(sys.argv) == 2 and sys.argv[1] != "-h":
    # load the actual forgor program
    forgor(sys.argv[1])
else:
    # help message
    print("forgor 💀\n")
    print("Usage:")
    print("$> forgor <page name>")
    list_pages()

# Reset
print("\033[0m", end='')
