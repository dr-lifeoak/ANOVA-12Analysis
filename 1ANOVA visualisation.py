import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 读取 CSV 文件
file_path = R''  # 替换为您的文件路径
data = pd.read_csv(file_path)

# 确保 'Group' 和 'Value' 列名与您的 CSV 文件中的列名相匹配
group1 = data[data['Group'] == 'Group1']['Value']
group2 = data[data['Group'] == 'Group2']['Value']
group3 = data[data['Group'] == 'Group3']['Value']

# 执行单因素方差分析
f_value, p_value = stats.f_oneway(group1, group2, group3)
print(f"F-Value: {f_value}")
print(f"P-Value: {p_value}")

# 根据 p 值判断显著性
if p_value < 0.05:
    print("存在显著差异")
else:
    print("不存在显著差异")

# 创建箱形图和散点图
plt.figure(figsize=(12, 6))

# 箱形图
sns.boxplot(x='Group', y='Value', data=data)

# 散点图
sns.stripplot(x='Group', y='Value', data=data, jitter=True, color='black', edgecolor='auto')

plt.title('Boxplot and Scatter Plot of Values by Group')
plt.show()
