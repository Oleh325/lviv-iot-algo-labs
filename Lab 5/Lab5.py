from timeit import default_timer as timer

def KMP_search(pattern, text):
    result: list[int] = []
 
    lps = get_lps_list(pattern, len(pattern))
 
    i = 0
    j = 0
    while (len(text) - i) >= (len(pattern) - j):
        
        if pattern[j] == text[i]:
            i += 1
            j += 1
 
        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
 
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return result if result else -1
 
def get_lps_list(pattern, pattern_length):
    lps = [0]*pattern_length
    
    len = 0
    i = 1
    while i < pattern_length:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def main():
        start = timer()
        print(KMP_search("ABCDE", "ABCDABCDABCDABCDABCDABCDEABCDABCDABCDEABCDABCDABCDABCDABCDABCDABCDABCDABCDE"))
        end = timer()
        print(f"Completed in {(end - start) * 1000}ms")

if __name__ == "__main__":  
    main()
    