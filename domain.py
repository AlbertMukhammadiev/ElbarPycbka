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


def get_less_domain(first, second):
    """
    Определение области, в которой первая парабола больше второй
    """
    xs = first.xs.copy()
    idxs = [i for i, (y1, y2) in enumerate(zip(first.ys, second.ys)) if y1 > y2]
    domain = xs[idxs]
    return domain


def get_result(chosen, others):
    """
    Поиск искомой области,
    где chosen парабола больше (не более n_less штук) остальных.
    """
    less_domains = [get_less_domain(chosen, parabola) for parabola in others]
    result = []
    for x in chosen.xs:
        n = len([domain for domain in less_domains if x in domain])
        if n < n_less:
            result.append(x)
    
    return result


n_parabolas = 5     # общее количество парабол
n_less = 4          # порог меньших парабол
n_xs = 1000         # количество элементов регулярной сетки по оси ox

fig, ax = plt.subplots()
chosen_one = create_parabola()
parabolas = [create_parabola() for _ in range(n_parabolas - 1)]
result_domain = get_result(
    chosen=chosen_one,
    others=parabolas
)

# отрисовка искомой области
ax.scatter(result_domain, np.zeros(len(result_domain)) - 1000, linewidth=0.5)

# отрисовка нулевой параболы и остальных
ax.plot(chosen_one.xs, chosen_one.ys, label='chosen', linewidth=4)
for parabola in parabolas:
    ax.plot(parabola.xs, parabola.ys)

ax.legend()
plt.show()
