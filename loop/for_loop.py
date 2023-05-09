str1 = "mo ji sa"
rev_str=""
str_rev = str1.split(' ')
for i in str_rev:
    a =i.swapcase()
    b ="".join(a)
    rev_str.append(b)
print(rev_str)