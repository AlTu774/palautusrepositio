
class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class All:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        return True


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        one_true = False
        for matcher in self._matchers:
            if matcher.test(player):
                one_true = True
        return one_true


class Not:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return False
        return True

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr
    
    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class QueryBuilder:
    def __init__(self, matcher = All()):
        self.matcher = matcher
    
    def test(self,player):
        return self.matcher.test(player)
    
    def build(self):
        return self.matcher
    
    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self.matcher))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self.matcher))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self.matcher))
    
    def oneOf(self, m1, m2):
        return QueryBuilder(Or(m1, m2))