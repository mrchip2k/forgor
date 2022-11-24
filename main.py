import sys


def make_path(filename):
    from os.path import expanduser
    home = expanduser("~")
    return home + "/.forgor/" + filename


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
        print("Could not read \"" + name + "\"")
        print("Searched in:")
        print(make_path(name))
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
    print("Pages are stored in " + make_path(""))
    files = get_files()
    if len(files) == 0:
        print("No pages found.")
    else:
        print("Available pages:")
        for file in files:
            print(" • " + file)
