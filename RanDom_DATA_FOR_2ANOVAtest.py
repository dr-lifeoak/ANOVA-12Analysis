import pandas as pd
import numpy as np

# 随机生成三组样本数据集
np.random.seed(1)
df = pd.DataFrame({
    'Factor1': np.random.choice(['Level 1', 'Level 2', 'Level 3'], 100),
    'Factor2': np.random.choice(['Group A', 'Group B', 'Group C'], 100),
    'Factor3': np.random.choice(['Type X', 'Type Y', 'Type Z'], 100),
    'Outcome': np.random.normal(50, 15, 100)
})

# 保存为CSV文件
csv_file_path = 'multivariate_anova_dataset.csv'  # 更改为你的文件路径
df.to_csv(csv_file_path, index=False)

