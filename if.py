
first = str(input ("Введите первую строчку: "))
second = str(input ("Введите вторую строчку: "))
def func(first, second):
	if first==second:
		 print(1)
	if first!=second and len(first)>len(second):
		 print(2)
	if first!= second and second=='learn':
		 print(3)

func(first, second)