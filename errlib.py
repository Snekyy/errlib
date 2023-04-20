from scipy.stats import t

pi = 3.141592653589793238462643383279502884197169399

def mean(X):
	return sum(X)/len(X)

def stdev(X):
	n = len(X)
	x_mean = mean(X)
	x_stdev = (sum([(x_i - x_mean)**2 for x_i in X])/((n-1)))**0.5
	return x_stdev

def stdev_mean(X, N):
	return stdev(X)/N**0.5

def random_err(X):
	return t.ppf(1-0.05/2, len(X)-1)*stdev(X)

def full_err(X, pr_err):
	return (random_err(X)**2 + pr_err**2)**0.5


def param_stdev(X, Y, a):
	n = len(X)
	a_stdev = (((stdev(Y)**2/stdev(X)**2) - a**2)/(n-2))**0.5
	b_stdev = a_stdev*(mean(X)**2 + (n-1)*stdev(X)**2/n)**0.5
	return a_stdev, b_stdev


def bestfit_linear(X, Y):
	n = len(X)
	numer = n*sum([xi*yi for xi, yi in zip(X, Y)]) - sum(X)*sum(Y)
	denumer = n*sum([xi**2 for xi in X]) - sum(X)**2
	a = numer/denumer
	b = (sum(Y) - a*sum(X))/n
	return a, b

def bestfit_linear_with_err(X, Y, X_err, Y_err):
	n = len(X)
	value = [1/(X_err[i]*Y_err[i])**2 for i in range(0, len(X))]

	valueXx = [value[i]*X[i] for i in range(0, n)]
	valueXy = [value[i]*Y[i] for i in range(0, n)]
	valueXxXy = [valueXy[i]*X[i] for i in range(0, n)]
	valueXxXx = [valueXx[i]*X[i] for i in range(0, n)]

	num = sum(value)*sum(valueXxXy) - sum(valueXx)*sum(valueXy)
	denum = sum(value)*sum(valueXxXx) - (sum(valueXx))**2

	a = num/denum
	b = (sum(valueXy)-a*sum(valueXx))/sum(value)

	a_stdev, b_stdev = param_stdev(X, Y, a)
	a_err = a_stdev*t.ppf(1-0.05/2, n)
	b_err = b_stdev*t.ppf(1-0.05/2, n)
	return a, b, a_err, b_err


def bestfit_hyperbolic(X, Y):
	n = len(X)
	numerator = sum([Y[i] for i in range(0, n)])
	denumerator = sum([1/X[i] for i in range(0, n)])
	return numerator/denumerator

	
def bestfit_hyperbolic_with_err(X, Y, X_err, Y_err):
	n = len(X)
	value = [1/(X_err[i]*Y_err[i])**2 for i in range(0, n)]
	numerator = sum([value[i]*Y[i] for i in range(0, n)])
	denumerator = sum([value[i]/X[i] for i in range(0, n)])
	return numerator/denumerator
