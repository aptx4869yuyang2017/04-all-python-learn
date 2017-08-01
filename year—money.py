#!/usr/bin/env python
# coding:utf8

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

def self_control(year):
    money = 0
    for i in xrange(1, 12 * year):
        money = (money + 1000)*(1 + 0.1 / 12)  # 年化收益 10%
    raw_money = 1000 * 12 * year

    str_out = '投资年限 {} 年，账户总金额 {} 元, 个人存入 {} 元，收益比例（账户总额除以个人存入金额）{} '.format(year, money, raw_money, money / raw_money)
    return str_out

def company_control(year):
    money = 0
    for i in xrange(1, 12 * year):
        money = (money + 2000)*(1 + 0.05 / 12) # 年化收益 5%
    raw_money = 1000 * 12 * year

    str_out = '投资年限 {} 年，账户总金额 {} 元, 个人存入 {} 元，收益比例（账户总额除以个人存入金额）{} '.format(year, money, raw_money, money / raw_money)
    return str_out

for i in [5, 10, 15, 20, 25, 30, 35]:
    print self_control(i)
    print company_control(i)
    print "----------------------------------"
