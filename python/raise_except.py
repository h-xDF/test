class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self,x):
        if x <= 0:
            raise NonPositiveError()
        else:
            super().append(x)
