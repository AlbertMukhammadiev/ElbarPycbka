import matplotlib.pyplot as plt
import random
import numpy as np
from collections import namedtuple


Parabola = namedtuple('Parabola', ['xs', 'ys'])


def create_parabola(a=None, b=None):
    """
    Create parabola in (a + bx)^2 format

    :param a: a value
    :param b: b value
    :return: Parabola
    """
    xs = np.linspace(-10, 10, n_xs)
    if a is None:
        a = random.uniform(-10, 10)
    if b is None:
        b = random.uniform(-10, 10)
    return Parabola(xs=xs, ys=(a + xs * b) ** 2)


def draw(parabola):
    ax.plot(parabola.xs, parabola.ys)


def get_less_domain(first, second):
    xs = first.xs.copy()
    idxs = [i for i, (y1, y2) in enumerate(zip(first.ys, second.ys)) if y1 < y2]
    domain = xs[idxs]
    return domain



# n_parabolas = 20
# n_less = 5
n_xs = 1000
# parabolas = [create_parabola() for _ in range(n_parabolas)]
# chosen_parabola = random.choice(parabolas)





fig, ax = plt.subplots()
parabola1 = create_parabola()
parabola2 = create_parabola()
domain = get_less_domain(parabola1, parabola2)
draw(parabola1)
draw(parabola2)
ax.scatter(domain, np.zeros(len(domain)))

plt.show()
