from itertools import accumulate


def gcd(m, n):
    #assumes m < n
    if m % n == 0:
        return n
    return gcd(n, m % n)

assert gcd(5, 10) == 5
assert gcd(4, 12) == 4
assert gcd(9, 13) == 1

class Board(list):
    def __init__(self):
        board = [Rational(1, 40) for _ in range(0, 40)]
        self.length = len(board)
        super().__init__(self)
        self.extend(board)

    def total(self):
        total = Rational(0, 1)
        for square in self:
            total = total.add(square)
        return total.float()

    def true(self):
        return self.total() == 1.0

    def values(self):
        return [x.float() for x in self]

    def print_solution(self):
        values = self.values()[:]
        values = [[i, n] for i, n in enumerate(values)]
        values.sort(key = lambda x: x[1], reverse=True)
        values = values[:3]
        print(values)

class Rational:
    def __init__(self, num, den):
        g = gcd(num, den)
        self.num = num / g
        self.den = den / g

    def float(self):
        return self.num / self.den

    def add(self, r):
        self = Rational(self.num * r.den + r.num * self.den, self.den * r.den)
        return self

    def subtract(self, r):
        self = Rational(self.num * r.den - r.num * self.den, self.den * r.den)
        return self
    
    def mult(self, r):
        self = Rational(self.num * r.num, self.den * r.den)
        return self
    
    def prob_inverse(self):
        return Rational(1, 1).subtract(self)

    def __str__(self):
        return f'{self.num} / {self.den}'

assert Rational(2, 4).num == 1
assert (Rational(2, 4).add(Rational(3, 9))).den == 6
assert (Rational(3, 9).subtract(Rational(2, 4))).den == 6

def get_probabilities(high_die):
    def print_special_indices():
        for i in special_indices:
            print(f'{i}: {board[i]}')

    def check_board():
        # print_special_indices()
        board.print_solution()
        assert board.true()

    def transfer_probability(from_index, to_index, probability):
        board[from_index] = board[from_index].subtract(probability)
        board[to_index] = board[to_index].add(probability)

    special_indices = []
    rolls = [[d1, d2] for d1 in range(1, high_die + 1) for d2 in range(1, high_die + 1)]
    board = Board()
    doubles = [roll for roll in rolls if roll[0] == roll[1]]

    check_board()

    # how does only the doubles rule affect the probability distribution?
    # in pow(len(doubles), 3) out of pow(len(rolls), 3) rolls, that roll ends in Jail
    three_consecutive_doubles_probability = Rational(pow(len(doubles), 3), pow(len(rolls), 3))

    jail_index = 10
    special_indices.append(jail_index)

    for i, _ in enumerate(board):
        transfer_probability(i, jail_index, three_consecutive_doubles_probability)

    check_board()

    go_index = 0
    special_indices.append(go_index)

    cc_indices = [2, 17, 33]
    special_indices.extend(cc_indices)

    # on each of these indices, there's a 1/8 chance that you're sent to go, and a 1/8 chance you're sent to jail
    for i in cc_indices:
        # probability of the landing on it and drawing a card that forces motion is
        prob_draw_move = board[i].mult(Rational(1, 8))

        for j in [go_index, jail_index]:
            transfer_probability(i, j, prob_draw_move)

    check_board()

    ch_indices = [7, 22, 36]
    c1_index = 11
    e3_index = 24
    h2_index = 39
    r1_index = 5

    special_indices.extend(ch_indices + [c1_index, e3_index, h2_index, r1_index])
    for i in ch_indices:
        # probability of landing on it and drawing a card that forces motion is
        prob_draw_move = board[i].mult(Rational(10, 16))

        next_r_index = ((i // 5 + 1) * 5) % 40
        back_3_index = i - 3
        if i == 7:
            next_u_index = 12            
        if i == 22:
            next_u_index = 28
        if i == 36:
            next_u_index = 12

        result_indices = [
            go_index, jail_index, c1_index, e3_index, h2_index, r1_index, 
            # There are two Next R cards
            next_r_index, next_r_index, 
            next_u_index, back_3_index
            ]
        special_indices = list(set(special_indices + result_indices))

        for j in result_indices:
            transfer_probability(i, j, prob_draw_move)

    check_board()
    return board

def solution(high_die):
    print(f'die: {high_die}')
    get_probabilities(high_die).print_solution()

solution(6)
solution(4)