class ExtendStack(list):
    def sum(self):
        buf = self[len(self) - 2] = self[len(self) - 1] + self[len(self) - 2]
        self.pop()
        self.pop()
        self.append(buf)

    def sub(self):
        buf = self[len(self) - 2] = self[len(self) - 1] - self[len(self) - 2]
        self.pop()
        self.pop()
        self.append(buf)

    def mul(self):
        buf = self[len(self) - 2] = self[len(self) - 1] * self[len(self) - 2]
        self.pop()
        self.pop()
        self.append(buf)

    def div(self):
        buf = self[len(self) - 2] = self[len(self) - 1] // self[len(self) - 2]
        self.pop()
        self.pop()
        self.append(buf)


x = ExtendStack()
[x.append(i) for i in range(5) ]
