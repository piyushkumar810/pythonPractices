def isValidBrackets(queries):
    res = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for s in queries:

        s = s.replace(" ", "")
        st = []
        ok = True
        for ch in s:
            if ch in "([{":
                st.append(ch)
            else:
                if not st or st[-1] != pairs.get(ch, None):
                    ok = False
                    break
                st.pop()
        if ok and not st:
            res.append("YES")
        else:
            res.append("NO")
    return res


if __name__ == '__main__':
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(input().strip())
    out = isValidBrackets(queries)
    for x in out:
        print(x)
