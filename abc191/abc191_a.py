# https://atcoder.jp/contests/abc191/submissions/20597336
V,T,S,D = map(int, input().split())
if V*T <= D <= V*S:
  print("No")
else:
  print("Yes")
