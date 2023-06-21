def openf(path, name):
    if path != "":
        return "".join(open(path + "/" + name + ".txt", "r", encoding="utf-8").readlines(0))
    else:
        return "".join(open(name + ".txt", "r", encoding="utf-8").readlines(0))