T,P=input(),input()
lenT,lenP=len(T),len(P)
# 입력부
D=[0]*lenP # 실패 배열 만들기
j=0 # pattern 인덱스
for i in range(1,lenP): # 0번째 실패배열은 무조건 0
  while j>0 and P[j]!=P[i]: j=D[j-1]
  if P[j]==P[i]:
    D[i]=j+1
    j+=1

ans,ansList,j=0,[],0
for i in range(lenT):
  while j>0 and T[i]!=P[j]: j=D[j-1]
  if T[i]==P[j]:
    if j==lenP-1:
      ans+=1
      ansList.append(i-lenP+2)
      j=D[j]
    else: j+=1

print(ans)
print(' '.join(map(str,ansList)))