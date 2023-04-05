# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# 1)    创建一个空列表lst；
lst = []
# 2)    在lst列表中依次追加10个数值(78, 93, 66, 83, 100, 95, 77, 93, 85, 98)；
data = (78, 93, 66, 83, 100, 95, 77, 93, 85, 98)
lst = [temp_data for temp_data in data]
print(lst)
# 3)    输出lst列表中第7个元素的数值；
print(lst[6])
# 77

# 4)    输出lst列表中第1~5个元素的数值；
print(lst[:5])
# [78, 93, 66, 83, 100]

# 5)    调用insert()函数，在lst列表第7个元素之前添加数值59；
lst.insert(6,59)
print(lst)

# 6)    利用变量num保存数值93，调用count()函数，查询num变量值在lst列表中出现的次数；
num = 93
count = lst.count(93)
print(count)
# 2

# 7)    使用in查询lst列表中是否有num变量值的评分；
print(num in lst)

# 8)    调用index()函数，查询lst列表中100的序号；
print(lst.index(100))
# 4

# 9)    找出lst列表中数值为59的元素，并加1；
lst[lst.index(59)] += 1
print(lst)

# 10) 调用del()函数删除lst列表中的第1个元素；
del lst[0]
print(lst)


# 11) 调用len()函数获得lst列表中元素的个数；
print(len(lst))
# 10

# 12) 调用sort()函数，对列表中所有元素进行排序，输出列表中最高分和最低分；
lst.sort()
print(f"最高分{lst[-1]}, 最低分{lst[0]}")


# 13) 调用reverse()函数，颠倒lst列表中元素的顺序；
lst.reverse()
print(lst)


# 14) 调用pop()函数删除lst列表中尾部的元素，返回删除的元素；
del_element = lst.pop()
print(del_element)
# 60

# 15) lst列表中用append()函数追加数值83，并输出。调用remove()函数删除lst列表中第一个数值83；
lst.append(83)
lst.remove(83)
print(lst)
# [100, 98, 95, 93, 93, 85, 77, 66, 83]

# 16) 创建2个列表lst1和lst2，lst1中包含2个元素值：78，91，lst2中包含3个元素值：84，92，65，合并这两个列表，并输出全部元素；
#
lst1 = [78,91]
lst2 = [84,92,65]
lst1.extend(lst2)
print(lst1)
# [78, 91, 84, 92, 65]

# 17) 创建lst1列表，其中包含数值2个元素值：78，91，将lst1中元素赋值5遍保存在lst2列表中，输出lst2列表中全部元素;
lst1 = [78,91]
lst2 = []
for _ in range(5):
    for lst1_el in lst1:
        lst2.append(lst1_el)
print(f"lst2是:{lst2}")
# 18) 清空lst列表，将lst2列表复制给lst列表，将lst列表中第2个元素变为2，并分别输出lst列表、lst2列表全部元素
lst.clear()
print(lst)
lst = lst2.copy()
lst[1] = 2

print(f"lst2是:{lst2}")
print(f"lst是:{lst}")

# lst2是:[78, 91, 78, 91, 78, 91, 78, 91, 78, 91]
# lst是:[78, 2, 78, 91, 78, 91, 78, 91, 78, 91]

products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
for n,pro in enumerate(products):
    print(f"当前商品有{n + 1}   {pro}")
product_choice = []
while True:
    product_num = input("请选择你想要购买的商品编号，按Q或者q退出:")
    if product_num == 'Q' or product_num == 'q':
        print('选择结束')
        break
    if int(product_num) < 1 or int(product_num) > len(products):
    #if int(product_num) not in range(1,len(products) + 1):
        print("输入错误，请输入正确的商品编号")
        continue
    product_choice.append(products[int(product_num) - 1][0])
print(f"你选择的商品是{product_choice}")