












def trapezoid (x_vals: np.ndarray, func: np.ufunc) -> float:
    """This will take x values and turn them into an array that will contain the x values
    needed to approximate the integral. Then the array will be used to approximate the integral. """
    fx = (x_vals[:-1] - x_vals[1:])
    """"In order to calculate the base of the trapezoid, we need to subtract all values of x  agoing from left
     to right FROM all of the values going right to left. 
      This will then give us all of the bases for our individual trapezoids """
    return np.sum((func(x_vals[:-1])+func(x_vals[1:])//2 * fx))
    """First we must return the individual points that correspond with our x values in our array
     and add the "left" point and the "right". After doing this we must then divide this value by 2 in order to
      get the average height for the specific trapezoid. Once we have determined the average height we must multiply
       by the size of the base to find. Summing up all these terms will give us the trapezoid
        approximation for the integral."""
