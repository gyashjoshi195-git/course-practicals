"""Q5: Longest Common Subsequence (LCS) using Dynamic Programming.

If X[i-1] == Y[j-1]: L[i][j] = L[i-1][j-1] + 1
else               : L[i][j] = max(L[i-1][j], L[i][j-1])
Time: O(m*n)   Space: O(m*n)
"""


def lcs(x, y):
    m, n = len(x), len(y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # backtrack to build the subsequence
    i, j, seq = m, n, []
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            seq.append(x[i - 1])
            i -= 1
            j -= 1
        elif L[i - 1][j] >= L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return L, "".join(reversed(seq))


if __name__ == "__main__":
    X, Y = "AGGTAB", "GXTXAYB"
    table, result = lcs(X, Y)
    print(f"X = {X}, Y = {Y}")
    print("DP table:")
    print("      " + "  ".join(" " + c for c in Y))
    for idx, row in enumerate(table):
        label = " " if idx == 0 else X[idx - 1]
        print(label, row)
    print("LCS length:", table[-1][-1])
    print("LCS       :", result)  # GTAB
