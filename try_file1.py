# -*- coding: UTF-8 -*-

# 写文件
filename = "test.txt"
f = open(filename, 'w')  # write 方式第一次写一行

for i in range(10):
    data = 'Hello World'
    data = 'Row = %d HW' % i
    data = 'Row no.= %02d Hello World\n' % (i + 1
)
    f.write(data)

f.close()
