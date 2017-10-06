from matplotlib import pyplot as plt


def plot_values(signal_values):
    return zip(*enumerate(signal_values))


def draw_plots(signals_values, signal_labels, spectrums, spectrums_labels):
    plt.subplots_adjust(bottom=0.25)
    plt.figure(1)
    lines = []
    for signal_values in signals_values:
        x_points, y_points = plot_values(signal_values)
        line, = plt.plot(x_points, y_points)
        lines.append(line)
    plt.figlegend(lines, signal_labels, loc='lower center')
    for i, spectrum in enumerate(spectrums):
        plt.figure(2 + i)
        amplitudes, phases = spectrum
        axes = plt.subplot(1, 2, 1)
        axes.stem(*plot_values(amplitudes), linefmt='b', markerfmt=' ', basefmt=' ')
        axes = plt.subplot(1, 2, 2)
        axes.stem(*plot_values(phases), linefmt='b', markerfmt=' ', basefmt=' ')

    plt.show()
