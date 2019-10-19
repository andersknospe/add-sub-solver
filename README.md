# AddSub Solver
This project is primarily an algorithm for solving the AddSub Problem. 

## AddSub Problem
Given a set of integers (*S*) and a target integer (*i*), find if it is possible to use a combination of addition and subtraction to yield the target integer. For example, the set [1,4,6,2,5] and the target integer 6 would return True as ( - 1 + 4 + 6 + 2 - 5) = 6.

The AddSubSolver class implemented in this project provides two approachs to solving this problem. The first uses recursion (*O(2<sup>n</sup>)*) while the second utilizes dynamic programming (*O(n^2), more specifically O(|S|·ΣS*). In addition, the dynamic programming implemented in this algorithm does not need negative numbers in its DP table, as for any positive number that can be derived, the negative variant can be derived by switching all signs. 

## Usage

After downloading the files required for this program, you may want to run the `AddSubDriver.py` file to see how the AddSubSolver class is used. 


