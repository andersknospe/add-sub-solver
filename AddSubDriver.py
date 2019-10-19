'''
# @Author Anders Knospe 
# 
# This file shows some of the functionality of the AddSubSolver Class
'''
from AddSubSolver import AddSubSolver

A = AddSubSolver([1,3,4,9,3])
target = 10 
print(A)
print("is 10 possible? : " + str(A.is_sum_possible(target)))
print("path: " + A.get_path_to_sum(target)) + " = " + str(target)
print("recursive: " + str(A.recursive_num_operations()))
print("dp: " + str(A.dp_num_operations()))

