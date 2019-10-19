'''
# @Author Anders Knospe 
# 
# This file shows some of the functionality of the AddSubSolver Class
'''
from AddSubSolver import AddSubSolver

aSS = AddSubSolver([1,3,4,9,3])
target = 10 
print(aSS)
print("is 10 possible? : " + str(aSS.is_sum_possible(target)))
print("path: " + aSS.get_path_to_sum(target)) + " = " + str(target)
print("recursive: " + str(aSS.recursive_num_operations()))
print("dp: " + str(aSS.dp_num_operations()))

