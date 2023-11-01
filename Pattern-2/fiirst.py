n = int(input())
row = 1
while row<=n:
      col=1
      while col<=row:
         print(col, end='')
         col+=1
      col=1   
      while col<=(n-row)*2:
          print(' ', end='')
          col+=1
      col=row
      while col>=1:
         
         print(col, end='')
         col-=1
         
      row+=1
      print()