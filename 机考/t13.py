"""
输入描述：
输入一个英文语句，每个单词用空格隔开。保证输入只包含空格和字母。
输出描述：
得到逆序的句子
"""
lis = input().split()
a = lis[::-1]
b = ' '.join(a)
print(b)

