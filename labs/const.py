for line in open('messier.txt', encoding='latin_1'):
    if line.startswith('M'):
        if not line: break
        mn = line[:6].rstrip()
        cn = line[6:40].rstrip()
        ot = line[40:64].rstrip()
        co = line[64:].rstrip()
        if cn == "":
            cn = "no name"
        print(f"|{mn}|{cn}|{ot}|{co}|")
