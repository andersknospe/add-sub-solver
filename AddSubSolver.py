'''
# @Author Anders Knospe 
# 
# The AddSubSolver class provides a general tool for solving and analyzing the AddSub Problem
'''
class AddSubSolver():
	def __init__(self,numbers):
		self.numbers = numbers # numbers that can be used to create the sum

		self.num_cols = sum(numbers)+1 # greatest value reachable
		self.num_rows = len(numbers) # 

		# creates dp table of boolean values of target sums with certain items 
		self.dp_table = [[False for i in range(self.num_cols)] for i in range(self.num_rows)] # creates table m by n
		self.dp_table[0][self.numbers[0]] = True

		# creates path table keeping track of addsub paths
		self.path_table = [["" for i in range(self.num_cols)] for i in range(self.num_rows)] # creates table m by n
		self.path_table[0][self.numbers[0]] = " + " + str(self.numbers[0])

		for num_idx in range(1,self.num_rows):
			for target_sum in range(self.num_cols):

				if target_sum + self.numbers[num_idx] >= len(self.dp_table[0]):
					num_sub = False 

				else:
					num_sub = self.dp_table[num_idx-1][target_sum+self.numbers[num_idx]]
					
					self.path_table[num_idx][target_sum] = self.path_table[num_idx-1][target_sum+self.numbers[num_idx]] + " - " + str(self.numbers[num_idx])

				if target_sum - self.numbers[num_idx] < 0:
					num_add = self.dp_table[num_idx-1][abs(target_sum-self.numbers[num_idx])]
					
					self.path_table[num_idx][target_sum] = self.flip_signs(self.path_table[num_idx-1][abs(target_sum-self.numbers[num_idx])]) + " + " + str(self.numbers[num_idx])
				else: 
					num_add = self.dp_table[num_idx-1][target_sum-self.numbers[num_idx]]
					
					self.path_table[num_idx][target_sum] = self.path_table[num_idx-1][abs(target_sum-self.numbers[num_idx])] + " + " + str(self.numbers[num_idx])

				self.dp_table[num_idx][target_sum] = num_add #or num_sub #check if target can be achieved with an add or sub

	def __str__(self):
		rets = "  " + ''.join([str(x) + ' '* (3 - len(str(x))) for x in range(self.num_cols)]) + "\n"
		for row_idx,row in enumerate(self.dp_table):
			rets += str(self.numbers[row_idx]) + ' ' + ' '.join([self.get_symbol(boolean) for boolean in row]) + "\n"
		return rets.encode('utf-8')

	def size(self):
		return (self.num_cols,self.num_rows)

	# checks if target can be achieved with addsub summing (through dp table)
	def is_sum_possible(self,target_sum):
		if abs(target_sum) >= self.num_cols:
			return False 
		else:
			return self.dp_table[self.num_rows-1][abs(target_sum)]

	# returns path to target (if possible) by referencing path table
	def get_path_to_sum(self,target_sum):
		if abs(target_sum) >= self.num_cols:
			return "" 
		elif target_sum < 0: 
			return self.flip_signs(self.path_table[self.num_rows-1][abs(target_sum)])
		else:
			return self.path_table[self.num_rows-1][abs(target_sum)]

	def recursive_num_operations(self):
		return pow(2,self.num_rows)

	def dp_num_operations(self):
		return self.num_rows * self.num_cols

	# checks if target can be achieved with addsub summing (recursively)
	def is_sum_possible_recursive(self,target,numbers=None,current_sum=0):
		if numbers == None:
			numbers = self.numbers

		if current_sum == target:
			return True
		
		elif len(numbers) == 0:
			return False

		else: 
			plus_route = self.is_sum_possible_recursive(target, numbers[1:], current_sum + numbers[0])
			sub_route = self.is_sum_possible_recursive(target, numbers[1:], current_sum - numbers[0])
			return plus_route or sub_route

	#reinitializes the AddSubSolver with new numbers
	def re_init_with(self,numbers):
		self.__init__(numbers)

	# converts True & False to unicode symbols
	def get_symbol(self,boolean): 
		if boolean:
			return u'\u2705'
		else: 
			return u'\u274C'

	def flip_signs(self,string):
		return string.replace("+","p").replace("-","+").replace("p","-")

if __name__ == '__main__':
	globals()[sys.argv[1]]()







