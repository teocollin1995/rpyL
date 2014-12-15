__author__ = 'teo'

import rpy2.robjects as robjects

r = robjects.r

a = robjects.IntVector([1,2,3,4])

pi = robjects.r['pi']
pi1 = robjects.r('pi')
print(pi)
print(pi1)
print(pi[0])

piplus2 = robjects.r('pi') +2
a = piplus2.r_repr()
print(a)
piplus21 =robjects.r('pi')[0] +2
print(piplus21)

robjects.r('''
        f <- function(r, verbose=FALSE) {
            if (verbose) {
                cat("I am calling f().\n")
            }
            2 * pi * r
        }
        f(3)
        ''')
r_f = robjects.globalenv['f']
print(r_f.r_repr())
r_f2 = r_f(1)
r_f3 = robjects.globalenv['f'](1)
print(r_f(1))
print(r_f2)
print(r_f3)


letters = robjects.r['letters']
rcode = 'paste(%s, collapse="-")' %(letters.r_repr())
res = robjects.r(rcode)
print(res)

print(len(robjects.r['pi']))

res1 = robjects.StrVector(['abc','def'])
print(res1.r_repr())
res2 = robjects.IntVector([1,2,3])
print(res2)
res3 = robjects.FactorVector([1.1,2.2,3.3])
print(res3)

v = robjects.FloatVector([1.1, 2.2, 3.3, 4.4, 5.5, 6.6])
m = robjects.r['matrix'](v, nrow = 2)
print(m)

rsum=robjects.r['sum']
print(rsum(res2))
rsort = robjects.r['sort']
res4 = rsort(robjects.IntVector([1,2,3]), decreasing=True)
print(res4)


# more examples....


r = robjects.r

x = robjects.IntVector(range(10))
y = r.rnorm(10)

r.X11()

r.layout(r.matrix(robjects.IntVector([1,2,3,2]), nrow=2, ncol=2))
filevab = "/home/teo/the.png"
from rpy2.robjects.packages import importr
grdevices.png(file=filevab,width=512,height=512)
r.plot(r.runif(10), y, xlab="runif", ylab="foo/bar", col="red")
grdevices.dev_off()
