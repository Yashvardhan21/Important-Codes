def findPath(arr, n):
    ans = []
    ans = recur(arr,0,0,'',"",n,ans)
    ans.sort()
    ans = " ".join(map(str,ans))
    return ans

def recur(arr,i,j,c,s,n,ans):
    if i<0 or i>=n or j<0 or j>=n or arr[i][j]==0:
        return ans
    s = s+c
    if i==n-1 and j==n-1:
      ans.append(s)
    if arr[i][j]==1:
        arr[i][j]=0
        ans = recur(arr,i,j+1,'R',s,n,ans)
        ans = recur(arr,i+1,j,'D',s,n,ans)
        ans = recur(arr,i-1,j,'U',s,n,ans)
        ans = recur(arr,i,j-1,'L',s,n,ans)
        arr[i][j]=1   
    return ans

     
