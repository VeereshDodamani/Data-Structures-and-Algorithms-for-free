strs = ["flower","xbow","flight"]

if not strs:
    print("")
else:
    min_length = min(len(s) for s in strs)

    i = 0
    while i < min_length:
        current_char = strs[0][i]
        for s in strs:
            if s[i] != current_char:
                print("Longest Common Prefif: ",strs[0][:i])
                exit()
        i += 1
