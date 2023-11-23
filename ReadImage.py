def ReadImage(file):
    f = open(file, mode="rb")
    raw = f.read()
    data = raw.hex()
    print(data)
    f.close()


