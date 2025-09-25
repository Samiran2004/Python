def fun(n):
    if n == 0:
        return
    fun(n - 1)
    print(n, end=" ")

fun(4)
