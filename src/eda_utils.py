import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlations(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=False, cmap="viridis")
    plt.show()