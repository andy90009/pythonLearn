
# map/reduce

# Python内建了map()和reduce()函数

# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

# 举例说明，比如我们有一个函数f(x)=x2，
# 要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现