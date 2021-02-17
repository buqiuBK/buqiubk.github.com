#!/usr/bin/env python

a = [1,2,3,4,'abc',[4,5,6]]

# 类型判断
b = isinstance(a,int)
c = isinstance(a,(int,str,list))

for i in a:
    if isinstance(i, (list,str)):

        for v in i:
            print(v)

    else:
        print(i)



