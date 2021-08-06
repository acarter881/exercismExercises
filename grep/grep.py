def grep(pattern, flags, files):
    n, l, i, v, x, m, res = "-n" in flags, "-l" in flags, "-i" in flags, "-v" in flags, "-x" in flags, len(files) > 1, ""

    pattern = pattern.lower() if i else pattern

    for file in files:
        for line_num, line in enumerate(open(file).readlines()):
            line_i = line.lower() if i else line

            if v ^ (not x and pattern in line_i or pattern + '\\n' == line_i or pattern + '\n' == line_i):
                if l:
                    res += file + '\n'
                    break
                res += (f"{file}:" if m else '') + (f"{line_num + 1}:" if n else '') + line
    return res