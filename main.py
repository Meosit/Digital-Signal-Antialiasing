from draw import draw_plots
from signal import fourier_spectrum, \
    fourth_degree_parabola_antialiasing, \
    moving_averaged_antialiasing, \
    moving_median_antialiasing, \
    random_signal

N = 512
SIGNALS_LABELS = [
    'Original signal',
    'Moving averaged antialiasing',
    'Fourth degree parabola antialiasing (7 points)',
    'Moving median antialiasing'
]
SPECTRUMS_LABELS = [
    'Original spectrum',
    'Moving averaged antialiasing spectrum',
    'Fourth degree parabola antialiasing (7 points) spectrum',
    'Moving median antialiasing spectrum'
]
AVERAGED_WINDOW = 3
MEDIAN_WINDOW = 5
B1 = 5
B2 = 8


if __name__ == '__main__':
    random_signal_values = [random_signal(i, N, B1, B2) for i in range(N)]
    signals_values = [
        random_signal_values,
        moving_averaged_antialiasing(random_signal_values, AVERAGED_WINDOW),
        fourth_degree_parabola_antialiasing(random_signal_values),
        moving_median_antialiasing(random_signal_values, MEDIAN_WINDOW)
    ]
    spectrums = list(map(fourier_spectrum, signals_values))
    draw_plots(signals_values, SIGNALS_LABELS, spectrums, SPECTRUMS_LABELS)
