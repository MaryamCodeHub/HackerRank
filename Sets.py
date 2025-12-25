"""
Task
Now, let's use our knowledge of sets and help Mickey.
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
Formula used:
Function Description:Complete the average function in the editor below. average has the following parameters:
int arr: an array of integers
Returns
float: the resulting float value rounded to 3 places after the decimal
Input Format
The first line contains the integer, , the size of .
The second line contains the  space-separated integers, .
Sample Input
STDIN                                       Function
-----                                       --------
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]
Sample Output
169.375
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
"""

M=int(input())
set_M=set(map(int,input().split()))
N=int(input())
set_N=set(map(int,input().split()))
diff=set_M.symmetric_difference(set_N)
for i in sorted(diff):
    print(i)

"""
Task

Apply your knowledge of the .add() operation to help your friend Rupal.
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.
Find the total number of distinct country stamps.

Input Format
The first line contains an integer , the total number of country stamps.
The next  lines contains the name of the country where the stamp is from.
Output Format
Output the total number of distinct country stamps on a single line.

Sample Input
7
UK
China
USA
France
New Zealand
UK
France 

Sample Output
5
"""
n = int(input())
countries = set()

for _ in range(n):
    countries.add(input().strip())

print(len(countries))
