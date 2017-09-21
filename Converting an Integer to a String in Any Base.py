class Soulution:
    def convert(self, num, base):
        pick = "0123456789ABCDEF"
        if num < base:
            return pick[num]
        else:
            return self.convert(num//base, base) + pick[num%base]

c = Soulution()
print(c.convert(128, 2))
