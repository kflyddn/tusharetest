# -*- coding:utf-8 -*-
import numpy as np
import sys, codecs

i = 0
m = 20
m1 = 20
dd = -0.6  # 每年递增金额
rate = 0.15  # 年化利率4%
rate1 = 0.1  # 年化利率10%
# import sys,codecs
fileObj = codecs.open("1.xml", 'w', "utf-8")
fileObj.write("test\n")

fileObj = codecs.open("s1.xml", 'a', "utf-8")
for i in range(1, 48):
    day = (m * rate / 22) * 10000
    day1 = (m1 * rate1 / 22) * 10000
    week = (m * rate / 4) * 10000
    week1 = (m1 * rate1 / 4) * 10000
    month = m * rate
    month1 = m1 * rate
    ddd = (dd * (i / 12 + 1))
    m = m * rate + m + ddd
    m1 = m1 * rate1 + m1 + ddd

    m = float('%.2f' % m)
    day = float('%.2f' % day)

    m1 = float('%.2f' % m1)
    day1 = float('%.2f' % day1)
    ff = np.fv(rate, i, dd, dd)
    # print(str(m)+"   "+str(i)+"  "+str(ff)+"  "+str(dd))
    line = ' %s目标 \t\t金额%s ~ %s\t\t递增%s\t\t约%s ~ %s \n' % (
    str(i), str(m), str(m1), str(round(ddd, 2)), str(day), str(round(day1, 2)))
    print(line)

    fileObj.write(line)
    line = ' %s目标 \t\t金额%s ~ %s\t\t递增%s\t\t约%s ~ %s \n' % (
    str(i), str(m), str(m1), str(round(ddd, 2)), str(week), str(round(week1, 2)))
    print(line)

    fileObj.write(line)
    line = ' %s目标 \t\t金额%s ~ %s\t\t递增%s\t\t约%s ~ %s \n\n\n' % (
    str(i), str(m), str(m1), str(round(ddd, 2)), str(month), str(round(month1, 2)))
    print(line)

    fileObj.write(line)

    # fileObj = open("1.xml",'a',"utf-8")
    # print(line)
    # fileObj.write(line)
# fileObj.close
# year =sys.argv[0]
# print(year)


print(ff)