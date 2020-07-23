from datetime import *
ans=date.today()
print(ans)
for i in range(1,5):
  new=ans+timedelta(days=i)
  print(new)
  
