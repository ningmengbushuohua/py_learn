# 进度条--->tqdm
from tqdm import tqdm

# 1. 使用tqdm 模块要记住：进度条运行时，不能有print

# 进度条有一定的长度，进度条是有限的，容器型数据类型正符合
for i in tqdm(range(1,100000001), desc='这是一个进度条'):
    # pass关键字：保存结构的完整性，不参与程序执行
    pass