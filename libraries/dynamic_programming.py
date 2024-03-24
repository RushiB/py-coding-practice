
class fibo_gen:

    def __init__(self) -> None:
        self.fibo_ser = []
    # 0,1,1,2,3,5,8,13
    # 0 1 2 3 4 5 6 7
    def get_n_fibonacci(self, index) -> int:
        # print(f'get_n_fibonacci({index}) -->')
        result = 0
        
        # len 1 => idx is 0
        # len 2 => idx is 1
        if index+1 <= len(self.fibo_ser):
            result = self.fibo_ser[index]
        elif index == 0:
            first_elem = 0
            self.fibo_ser.append(0)
            result = first_elem
        elif index == 1:
            # if 
            self.fibo_ser = [0,1]
            result = self.fibo_ser[index]
        elif index >= 2:
            res = 0
            res = self.get_n_fibonacci(index-1) + self.get_n_fibonacci(index-2)
            self.fibo_ser.append(res)
            result = res
        else:
            print('ERROR!')
    
        print(f'get_n_fibonacci({index}) <-- ser={self.fibo_ser}')

        return result


def test_fibo():
    fgen = fibo_gen()
    print(fgen.get_n_fibonacci(8))
    
    print(fgen.get_n_fibonacci(0))
    print(fgen.get_n_fibonacci(3))
    print(fgen.get_n_fibonacci(7))


def test_func():
    test_fibo
