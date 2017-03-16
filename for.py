z=0
marks = [{'school_class1': '1a', 'scores': [4,4,5,5,5,]}, {'school_class2': '2a', 'scores': [3,3,5,4,4]}]
for i in marks:
	s = i["scores"]
	print(sum(s))	
