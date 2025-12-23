"""
A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

Example

>>> print set()
set([])

>>> print set('HackerRank')
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

>>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

>>> print set((1,2,3,4,5,5))
set([1, 2, 3, 4, 5])

>>> print set(set(['H','a','c','k','e','r','r','a','n','k']))
set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
set(['Hacker', 'Rank'])

>>> print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
Basically, sets are used for membership testing and eliminating duplicate entries.

Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:

Function Description

Complete the average function in the editor below.

average has the following parameters:

int arr: an array of integers
Returns

float: the resulting float value rounded to 3 places after the decimal
Input Format

The first line contains the integer, , the size of .
The second line contains the  space-separated integers, .

Constraints


Sample Input

STDIN                                       Function
-----                                       --------
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]
Sample Output

169.375
Explanation

Here, set is the set containing the distinct heights. Using the sum() and len() functions, we can compute the average.
"""
def average(array):
    # your code goes here
    duplicate_removal=set(array)
    avg=sum(duplicate_removal)/len(duplicate_removal)
    return round(avg,3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

"""
Task
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
Sample Output

5
9
11
12
Language
Pypy 3
More
12345678
# Enter your code here. Read input from STDIN. Print output to STDOUT
M=int(input())
set_M=set(map(int,input().split()))
N=int(input())
set_N=set(map(int,input().split()))
diff=set_M.symmetric_difference(set_N)
for i in sorted(diff):
    print(i)
Line: 8 Col: 13

Test against custom input
Congratulations!

You have passed the sample test cases. Click the submit button to run your code against all the test cases.


Sample Test case 0

Sample Test case 1
Input (stdin)
4
2 4 5 9
4
2 4 11 12
Your Output (stdout)
5
9
11
12
Expected Output
5
9
11
12
"""
M=int(input())
set_M=set(map(int,input().split()))
N=int(input())
set_N=set(map(int,input().split()))
diff=set_M.symmetric_difference(set_N)
for i in sorted(diff):
    print(i)