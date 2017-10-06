from math import sin, cos, pi, hypot, atan2

from helper import random_or, fit_range


def cosine_amplitude(signal_values, harmonic_index, N):
    _sum = sum(x * cos(2 * pi * i * harmonic_index / N) for i, x in enumerate(signal_values))
    return (2 / N) * _sum


def sine_amplitude(signal_values, harmonic_index, N):
    _sum = sum(x * sin(2 * pi * i * harmonic_index / N) for i, x in enumerate(signal_values))
    return (2 / N) * _sum


def harmonic_amplitude(sine, cosine):
    return hypot(sine, cosine)


def harmonic_phase(sine, cosine):
    return atan2(sine, cosine)


def fourier_transformation(signal_values, harmonic_index, N):
    cosine = cosine_amplitude(signal_values, harmonic_index, N)
    sine = sine_amplitude(signal_values, harmonic_index, N)
    return harmonic_amplitude(sine, cosine), harmonic_phase(sine, cosine)


def fourier_spectrum(signal_values):
    N = len(signal_values)
    return zip(*[fourier_transformation(signal_values, j, N) for j in range(N)])


def random_signal(harmonic_index, N, B1, B2, sum_range=range(50, 71)):
    assert B1 >= B2

    def sine(i, j=1):
        return sin((2 * pi * i * j) / N)

    return B1 * sine(harmonic_index) + sum(B2 * random_or(-1, 1) * sine(harmonic_index, j) for j in sum_range)


def moving_averaged_antialiasing(values, window):
    offset = (window - 1) // 2
    values_range = range(len(values))
    safe_val = lambda i: values(fit_range(i, values_range))
    return [safe_val(j) for i in values_range for j in range(i - offset, i + offset)]


def fourth_degree_parabola_antialiasing(values):
    mul = 1 / 231
    values_range = range(len(values))
    safe_val = lambda i: values(fit_range(i, values_range))

    def antialiased(i):
        return mul * (5 * safe_val(i - 3) -
                      30 * safe_val(i - 2) +
                      75 * safe_val(i - 1) +
                      131 * safe_val(i) +
                      75 * safe_val(i + 1) -
                      30 * safe_val(i + 2) +
                      5 * safe_val(i + 3))

    return [antialiased(i) for i in values_range]


def moving_median_antialiasing(values, window):
    offset = (window - 1) // 2
    values_range = range(len(values))

    def antialiased(i):
        window_values = [values[j] for j in range(fit_range(i - offset, values_range),
                                                  fit_range(i + offset, values_range))]
        return sorted(window_values[offset])

    return [antialiased(i) for i in values_range]
