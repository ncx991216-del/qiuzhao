import pandas as pd

data = {
    "姓名": ["张三", "李四", "王五", "赵六"],
    "年龄": [25, 30, 28, 35],
    "城市": ["北京", "上海", "北京", "深圳"],
}

df = pd.DataFrame(data)
print(df[df["年龄"] > 25])  # 输出年龄大于25的行数据
