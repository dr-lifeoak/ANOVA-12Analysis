import pandas as pd
from scipy import stats

# 读取 CSV 文件
file_path = r'C:\Users\cheng\Desktop\sample_data.csv'  # 替换为您的文件路径
data = pd.read_csv(file_path)

# 假设 CSV 文件有一个列名为 'Group' 表示分组，另一个列名为 'Value' 表示数值
group1 = data[data['Group'] == 'Group1']['Value']
group2 = data[data['Group'] == 'Group2']['Value']
group3 = data[data['Group'] == 'Group3']['Value']

# 执行单因素方差分析
f_value, p_value = stats.f_oneway(group1, group2, group3)

print(f"F-Value: {f_value}")
print(f"P-Value: {p_value}")
# 根据 p 值判断显著性（当p小于设定的信任值，就会拒绝0假设，即样本数据具有显著差异vice versa）
if p_value < 0.05:
    print("存在显著差异")
else:
    print("不存在显著差异")

