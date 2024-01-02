import pandas as pd
import numpy as np

# 生成三个样本组的数据
np.random.seed(0)
group1 = np.random.normal(100, 10, 30)
group2 = np.random.normal(90, 10, 30)
group3 = np.random.normal(95, 10, 30)

# 创建 DataFrame
df = pd.DataFrame({
    'Group': ['Group1'] * 30 + ['Group2'] * 30 + ['Group3'] * 30,
    'Value': np.concatenate([group1, group2, group3])
})

# 保存到 CSV 文件
df.to_csv('sample_data.csv', index=False)

