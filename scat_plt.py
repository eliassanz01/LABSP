import matplotlib.pyplot as plt
import seaborn as sns

# Falta lo siguiente, lo actualizare en breves
#The obtained plot should contain a legend displaying the information regarding to groups

def scat_plt(var1, var2, groups):
    sns.scatterplot(x=var1, y=var2, c=groups)
    plt.show()


