class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        else:
            return False
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        if pos >= 1:
            return True
        else:
            return False
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        if neg == 0:
            return True
        else:
            return False

    def gen(iterable, *funcs, judge):
        for i in iterable:
            pos = 0
            neg = 0
            for fun in funcs:
                if fun(i):
                    pos += 1
                else:
                    neg += 1
            if judge(pos,neg):
                yield i


    def __init__(self, iterable, *funcs, judge=judge_any):
        self.posled = []
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        return multifilter.gen(self.iterable, self.funcs, self.judge)
        # возвращает итератор по результирующей последовательности

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)]
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
