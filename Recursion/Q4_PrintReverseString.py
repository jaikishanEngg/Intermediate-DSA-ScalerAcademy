#
# Created on Sat Apr 02 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Write a recursive function that, given a string S, prints the characters of S in reverse order.

Problem Constraints
1 <= |s| <= 1000

Input Format
First line of input contains a string S.

Output Format
Print the character of the string S in reverse order.

Example Input
Input 1:
    scaleracademy
Input 2:
    cool

Example Output
Output 1:
    ymedacarelacs
Output 2:
    looc

Example Explanation
Explanation 1:
    Print the reverse of the string in a single line.
'''
import sys

def stringReverse(s, n, i):
    if(i >= 0):
        if i == n:
            return ''
        return stringReverse(s, n, i+1) + s[i]

def main():
    s = input()
    n = len(s)
    if(n > sys.getrecursionlimit()):
        sys.setrecursionlimit(n+5)
    ans = stringReverse(s, len(s), 0)
    print(ans)

if __name__ == '__main__':
    main()