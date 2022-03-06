
class Visited:
    def __init__(self):
        self._visited = []

    @profile
    def not_seen(self, value):
        if value not in self._visited:
            self._visited.append(value)
            return True
        return False
