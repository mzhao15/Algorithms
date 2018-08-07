

def binary_search(array,x):
	"""find x in a sorted array """
	num = len(array)
	left = 0
	right = num-1
	while left<=right:
		mid = (left+right)//2
		#print('left:{},mid:{},right:{}'.format(left,mid,right))
		if array[mid] == x:
			return mid
		elif array[mid] < x:
			left = mid+1
		else:
			right = mid-1

		
