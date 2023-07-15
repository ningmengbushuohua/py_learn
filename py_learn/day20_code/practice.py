'''
1.家具类(HouseItem) 有 名字 和 占地面积属性，其中

- 席梦思(bed) 占地 4 平米
- 衣柜(chest) 占地 2 平米
- 餐桌(table) 占地 1.5 平米

房子类(House) 有 户型、总面积 、剩余面积 和 家具名称列表 属性

- 新房子没有任何的家具
- 将 家具的名称 追加到 家具名称列表 中
- 判断 家具的面积 是否 超过剩余面积，如果超过，提示不能添加这件家具

a.将以上三件 家具对象 添加 到 房子对象 中
b.打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
使用面向对象思想，编码完成上述功能。
'''

class Houseitem():
    __slots__ = ('name','area')
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return f'该家具的名称为{self.name},占地面积是{self.area}'
    __repr__ = __str__

class House():
    __slots__ = ('shape','total_area','left_area','house_item_list')
    def __init__(self,shape,total_area,left_area):
        self.house_item_list = []
        self.shape = shape
        self.total_area = total_area
        self.left_area = left_area
    def add_house_item(self,item):
        if self.left_area > item.area:
            self.house_item_list.append(item)
            self.left_area -= item.area
        else:
            print('剩余面积不足，无法添加')
    def __str__(self):
        return f'房子的户型是{self.shape},总面积是{self.total_area},' \
               f'剩余面积是{self.left_area},家具名称列表是{self.house_item_list}'
    __repr__ = __str__

if __name__ =='__main__':
    bed = Houseitem('席梦思',4)
    chest = Houseitem('衣柜',2)
    table = Houseitem('餐桌',1.5)

    home = House('四室三厅',150,80)
    home.add_house_item(bed)
    home.add_house_item(chest)
    home.add_house_item(table)
    print(home)
