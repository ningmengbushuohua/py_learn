# 校验qq号
'''
合法的qq号：
    a.全部是数字
    b.位数5-11位
    c.开头不能为0
'''
# 使用传统的if
def check_qq1(qq:str):
    result = True
    if qq.isdigit():
        if len(qq) in range(5,12):
            if qq.startswith('0'):
                result = False
        else:
            result = False
    else:
        result = False
    return result

def check_qq2(qq:str):
    return qq.isdigit() and len(qq) in range(5,12) and not qq.startswith('0')

# 正则表达式
import re
def check_qq3(qq:str):
    r = re.match(r'[1-9]\d{4,10}$', qq)    # [1-9][0-9]{4,10}
    print(r)
    return True if r else False

if __name__ == '__main__':
    qq = '766753452424254211111'
    r1 = check_qq1(qq)
    r2 = check_qq2(qq)
    r3 = check_qq3(qq)
    print(r1,r2,r3)
