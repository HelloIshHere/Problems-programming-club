import string

n = input("inputs")
n = n.split(" ")


n0 = n[0]
n1 = n[1]
n2 = n[2]

nfinal = n0 + n1
if nfinal == n2:
    print('sucess')