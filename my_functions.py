def building_model(formula, data_frame):
    """
    takes in formula eg "y ~ x" and your data then outputs a model using the data
    """
    return (sm.formula.ols(formula= formula, data = data_frame))


def plotting_regression_plots(your_model, independent_variable):
    """
    Plots all necessary regression plots
    """
    fig, ax = plt.subplots(figsize=(8, 6))  # Create a figure and axis
    sm.graphics.plot_regress_exog(your_model, independent_variable, ax=ax)  # Plot regression plots on the axis
    ax.set_xlabel(independent_variable, color='orange')  # Set x-axis label color to orange
    ax.tick_params(axis='x', colors='orange')  # Set x-axis tick color to orange