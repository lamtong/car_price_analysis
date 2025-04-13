import seaborn as sns
import matplotlib.pyplot as plt

def plot_props(title=None, title_size=14, y_label=None, x_y_size=12, x_label=None, lgn_loc='best', lgn_col=1, legend=True):
    '''This function sets the preferred plot settings

    Arguments:
        title -- the graph title (default: {None})
        title_size -- font size of title (default: {14})
        y_label -- y label (default: {None})
        x_label -- x label (default: {None})
        lgn_loc -- legend position (default: {'best'})
    '''

    # Show the plot with the title
    if title:
        plt.title(title, fontsize=title_size)
    
    # Setting preferred axes and tick color  
    sns.despine()
    for spine in plt.gca().spines.values():
        spine.set_color("#666666")
        
    plt.gca().tick_params(axis="x", colors="#666666")  # X-axis ticks
    plt.gca().tick_params(axis="y", colors="#666666")  # Y-axis ticks

    # x, y, and legend labels with color set to #666666
    plt.ylabel(y_label, fontsize=x_y_size, color="#666666")
    plt.xlabel(x_label, fontsize=x_y_size, color="#666666")
    
    if legend:
        plt.legend(loc=lgn_loc, frameon=False, ncols=lgn_col)
        
    plt.show()
