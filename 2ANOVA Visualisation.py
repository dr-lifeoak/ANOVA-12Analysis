import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 加载或创建数据
df = pd.read_csv(r'T:\PY project\NCBItest\multivariate_anova_dataset1.csv')  # 替换为你的数据文件路径
# 假设数据集
np.random.seed(1)
df = pd.DataFrame({
    'Factor1': np.random.choice(['Factor1', 'Factor2', 'Factor3'], 100),
    'Outcome': np.random.normal(50, 15, 100)
})

# 设置画布大小和分辨率
plt.figure(figsize=(10, 6), dpi=300)

# 设置风格
sns.set(style="whitegrid")

# 定义紫色调色板
box_palette = ['purple']
swarm_color = 'violet'

# 绘制箱型图
sns.boxplot(x='Factor1', y='Outcome', data=df, palette=box_palette)

# 绘制散点图（swarmplot）
sns.swarmplot(x='Factor1', y='Outcome', data=df, color=swarm_color, alpha=0.7)

# 设置标题和标签
plt.title('Combined Box Plot and Swarm Plot in Purple Theme', fontsize=14)
plt.xlabel('Factor', fontsize=12)
plt.ylabel('Outcome', fontsize=12)

# 添加紧凑布局
plt.tight_layout()

# 保存图像
plt.savefig('/mnt/data/combined_plot_purple.png', format='png', dpi=300)

# 显示图表
plt.show()
