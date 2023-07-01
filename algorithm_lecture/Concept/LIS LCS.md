# [알고리즘] LIS LCS



## LIS (Longest Increasing Subsequence, 최장 증가 부분 수열)

- 1 ~ N 번까지 순서대로 i번째 dp값을 최신화해준다. j는 i보다 작은 수, 즉 배열의 앞에 있는 숫자라고 할 때 i번째 숫자가 j번째보다 크고 dp[i]가 dp[j]+1보다 작으면 dp[i]의 값을 dp[j]+1로 최신화해준다.

```python
# DP를 활용한 O(N^2) 풀이법
def LIS():
  for i in range(N):
    dp[i] = 1
    for j in range(i):
      if arr[i] > arr[j] and dp[i] < dp[j] + 1:
        dp[i] = dp[j] + 1
    ans = max(ans, dp[i])
```

- 배열을 순회하면서 원소를 확인하는데 LIS의 끝에 추가될 수 있다면 추가를 하고 그렇지 않다면 자신보다 같거나 큰 원소를 lower_bound를 활용하여 찾아내 자신과 교체.
- 이렇게 되면 LIS 배열 자체를 알 수는 없지만 LIS 배열의 길이는 알 수 있다!
- 배열 자체를 알고 싶으면 또 다른 배열을 하나 추가하여 자신이 몇번째 LIS 원소로 추가되었는지를 기억한 다음 배열의 뒤에서부터 역추적하여 LIS 배열을 구할 수 있다.

```python
# lower_bound를 활용한 O(NlogN) 풀이법
def LIS():
  lis = [0]
  for num in Numbers:
    if lis[-1] < num:
      lis.append(num)
    else:
      # 이분 탐색
      left, right = 0, len(lis)
      while left < right:
        mid = (left + right) // 2
        if lis[mid] < num:
          left = mid + 1
        else:
          right = mid
      lis[right] = num
	ans = lis(lis) - 1
  
# ex)
# [100, 50, 70, 90, 75, 87, 105, 78, 110, 60] 
# 기존 LIS => [50, 70, 75, 87, 105, 110]
# lower_bound LIS => [0, 50, 60, 75, 78, 105, 110]
```



## LCS (Longest Common Subsequence, 최장 공통 부분수열)

- 2개 이상의 문자열에서 공통으로 나타내는 부분 문자열 중 가장 긴 문자열
- ex) DNA의 공통 염기서열을 찾아 데이터를 압축하거나 무선 서명을 통해 휴대폰에서 사용자를 인증할때 사용
- LCS 함수의 정의

```python
lcs = [[0] * (len(A)+1) for _ in range(len(B)+1)]

def LCS(i, j):
  if i == 0 or j == 0:
    lcs[i][j] = 0
  elif A[i] == B[j]:
    lcs[i][j] = lcs[i-1][j-1] + 1
  elif A[i] != B[j]:
    lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
```

- ex)

```python
A = "ACAYKP"
B = "CAPCAK"

LCS = [[0]*(len(A)+1) for _ in range(len(B)+1)]

for i in range(1, len(A)+1):
  for j in range(1, len(B)+1):
    if A[i-1] == B[j-1]:
      LCS[i][j] = LCS[i-1][j-1] + 1
    else:
      LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])
      
print(LCS[len(A)][len(B)])
```







#### 참고 사이트

- https://allmymight.tistory.com/46