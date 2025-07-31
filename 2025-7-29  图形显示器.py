def left_triangle(n,symbol):
  for i in range(1,n+1):
      print(symbol*i)
def right_triangle(n,symbol):
  for i in range (1,n+1):
      print((symbol*i).rjust(n))
def middle_triangle(n,symbol):
  for i in range(1,n+1):
      print((symbol*(2*i-1)).center(2*n-1))
def inverted_left_triangle(n,symbol):
  for i in range(n,0,-1):
      print(symbol*i)
def inverted_right_triangle(n,symbol):
  for i in range(n,0,-1):
      print((symbol*i).rjust(n))
def inverted_middle_triangle(n,symbol):
  for i in range(n,0,-1):
      print((symbol*(2*i-1)).center(2*n-1))
def square(n,symbol):
  for i in range(1,n+1):
      print(symbol*n)
def rectangle(height,symbol,width):
  for i in range(height):
      print(symbol*width)

shape = {
  1: left_triangle,
  2: right_triangle,
  3: middle_triangle,
  4: inverted_left_triangle,
  5: inverted_right_triangle,
  6: inverted_middle_triangle,
  7: square,
  8: rectangle
}

while True:
  print("1.左直角三角形\n2.右直角三角形\n3.等腰三角形\n4.倒立左直角三角形\n5.倒立右直角三角形\n6.倒立等腰三角形\n7.正方形\n8.长方形")
  user_choice = input("以上是可选的图形,请输入你想要的图形对应的代号数字,或输入exit退出选择:")
  if user_choice == "exit":
      print("退出程序")
      break
  elif int(user_choice) <= 8 and int(user_choice) > 0:
      symbol = input("请输入一个符号作为图形的使用文字：")
      height = int(input("请输入图形的高度："))
      user_choice = int(user_choice)
      if user_choice <= 7:
          shape[user_choice](height,symbol)
      elif user_choice == 8:
          width = int(input("请输入图形的宽度："))
          shape[user_choice](height,symbol,width)
      print("\n")
  else:
      print("输入错误")
