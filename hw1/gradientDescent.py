# compute cost

def cost(x, y, theta):
    m = len(y)
    if len(theta) == 2:
        hx = [ (theta[0] + (theta[1] * x[i])) for i in range(len(x))]
        hx_y_2 = [ (hx[i] - y[i])**2 for i in range(len(y)) ]
        j = float(sum(hx_y_2))/(2 * m)
        
        return j
    
    else:
        return "Error"
        
# gradient descent func

def gradientDescent(x, y, theta, alpha, num_iters):
    m = len(y)
    j_history = []
    
    for iter in range (0, num_iters - 1):
        hx = [ (theta[0] + (theta[1] * x[i])) for i in range(len(x))]
        hx_y_x = [ (hx[i] - y[i]) * hx[i] for i in range(len(y)) ]
        hx_y = [ (hx[i] - y[i])  for i in range(len(y)) ]
        grad0 = alpha / m * sum(hx_y)
        grad1 = alpha / m * sum(hx_y_x)
        
        theta[0] = theta[0] - grad0
        theta[1] = theta[1] - grad1
        
        j_history[iter] = cost(x, y, theta)
        
        print j_history
    
    return theta
           
        
