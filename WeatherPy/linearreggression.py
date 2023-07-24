def linreg(x, y, x_label, y_label, title):
    #import dependencies required for function.
    from scipy.stats import linregress
    import matplotlib.pyplot as plt
    
    #Calculate the linear regression line
    slope, intercept, r_val, p_val, std_err = linregress(x, y)
    best_fit = slope * x + intercept
    
    #need to print the line equation   
    line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
    
    #Plot the scatter
    plt.scatter(x,y)
    
    #Plot the line equation
    plt.annotate(line_eq,(5.8,0.8),fontsize=15,color="red")
    
    #Plot the best fit line
    plt.plot(x,best_fit,"r-")
    
    # Set x-axis limits and ticks
    plt.xlim(-60, 85)
    plt.xticks(range(-60, 85, 20))
    
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    return plt.show(), print(f'The r-value is: {r_val}')