def find_lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    lcs_length = dp[m][n]
    
    lcs_str = ""
    i = m
    j = n
    
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str = X[i - 1] + lcs_str
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    return lcs_length, lcs_str

def main():
    x_seq = input("Enter the first sequence (X): ")
    y_seq = input("Enter the second sequence (Y): ")
    
    length, lcs_result = find_lcs(x_seq, y_seq)
    
    print("\n--- Results ---")
    print(f"Length of Longest Common Subsequence : {length}")
    print(f"Longest Common Subsequence           : {lcs_result}")

if __name__ == "__main__":
    main()