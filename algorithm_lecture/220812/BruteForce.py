source = "This is a book~!"
pattern = "is"

def BruteForce(pattern, source):
    # source(text)를 처음부터 끝까지 차례로 순회하면서 pattern의 길이만큼 윈도우를 만들어서
    for i in range(len(source)-len(pattern)+2):
        # pattern의 처음부터 윈도우 문자열과 비교
        for j in range(len(pattern)):
            if source[i + j] == pattern[j]:
                pass
            else:
                break
        else:
            return i
    else:
        return -1

print(BruteForce(pattern, source))