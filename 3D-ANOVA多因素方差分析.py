# 调用python库 numpy pandas statsmodels.formula.api matplotlib
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. 数据准备
# 假设数据: factor1, factor2为分类变量，value为因变量
np.random.seed(123)
data = pd.DataFrame({
    'factor1': np.repeat(['A', 'B', 'C'], 10),
    'factor2': np.tile(['X', 'Y'], 15),
    'value': np.random.rand(30)
})

# 2. 多因素ANOVA MOdel set
model = ols('value ~ C(factor1) + C(factor2) + C(factor1):C(factor2)', data=data).fit()
anova_results = sm.stats.anova_lm(model, typ=2)
print(anova_results)

# 3. 三维可视化3Dvisualisation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 为每个factor1和factor2组合创建一个点
for f1 in data['factor1'].unique():
    for f2 in data['factor2'].unique():
        mean_value = data[(data['factor1'] == f1) & (data['factor2'] == f2)]['value'].mean()
        ax.scatter(f1, f2, mean_value, label=f'{f1}-{f2} mean')

ax.set_xlabel('Factor 1')
ax.set_ylabel('Factor 2')
ax.set_zlabel('Mean Value')
plt.title('3D plot for Mean Values by Factor 1 and Factor 2')
plt.legend()
plt.show()
