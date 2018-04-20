def cost(x, y, theta):
    m = len(y)
    if len(theta) == 2:
        hx = [ (theta[0] + (theta[1] * x[i])) for i in range(len(x))]
        hx_y_2 = [ (hx[i] - y[i])**2 for i in range(len(y)) ]
        j = float(sum(hx_y_2))/(2 * m)
        return j
    else:
        return 'Error'
