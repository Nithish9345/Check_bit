class CheckBit:
    def check(self, a, b):
        if a & (1 << b):
            return 1


a = int(input())
b = int(input())
object = CheckBit()
print(object.check(a, b))

