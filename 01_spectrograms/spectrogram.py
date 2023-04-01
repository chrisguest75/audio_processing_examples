#!/usr/bin/env python3
import sys
import argparse
import io
import logging
import logging.config
import yaml
import numpy as np
import scipy.signal
import scipy.io.wavfile
import matplotlib.pyplot as plt
import csv

# TODO:
# Get a wav file from the internet
# Save it to the output folder
# convert it to ogg and aac
# calculate the spectrogram for both
# plot the spectrogram for both
# subtracts the spectrograms
# plot the difference
# save the difference as a csv file


def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.critical("Exception", exc_info=(exc_type, exc_value, exc_traceback))
    logging.critical('Unhandled Exception {0}: {1}'.format(exc_type, exc_value), extra={'exception': ''.join(traceback.format_tb(exc_traceback))})

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

def create_spectrograph(wav_file, output_file):
    logger.info("Processing", {"file": wav_file})
    # Read the WAV file
    sample_rate, data = scipy.io.wavfile.read(wav_file)

    # Calculate the spectrogram
    frequencies, times, spectrogram = scipy.signal.spectrogram(data, fs=sample_rate, nperseg=256, noverlap=128)

    # Save the spectrogram as a CSV file
    with open(output_file, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in spectrogram:
            csv_writer.writerow(row)

    logger.info("Output", {"file": output_file})

def plot_spectrogram(input_file):
    logger.info("Processing", {"file": input_file})
    # Read the CSV file
    with open(input_file, "r", newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        spectrogram = [list(map(float, row)) for row in csv_reader]

    spectrogram = np.array(spectrogram)

    # Normalize the spectrogram data (convert to dB)
    spectrogram_db = 10 * np.log10(spectrogram + np.finfo(float).eps)

    # Plot the spectrogram
    fig, ax = plt.subplots()
    img = ax.imshow(spectrogram_db, aspect="auto", origin="lower", cmap="inferno")
    ax.set_xlabel("Time")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Spectrogram {input_file}")
    fig.colorbar(img, ax=ax, label="Magnitude (dB)")
    plt.show()

def read_csv_file(filename):
    with open(filename, "r", newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        data = [list(map(float, row)) for row in csv_reader]
    return np.array(data)

def diff_spectrogram(input_file1, input_file2):
    logger.info("Diff", {"file1": input_file1, "file2": input_file2})

    # Read the spectrogram data from the CSV files
    spectrogram1 = read_csv_file(input_file1)
    spectrogram2 = read_csv_file(input_file2)

    # Subtract the spectrograms
    spectrogram_difference = np.abs(spectrogram1 - spectrogram2)

    # Convert the difference spectrogram to decibels
    spectrogram_difference_db = 10 * np.log10(spectrogram_difference + np.finfo(float).eps)

    # Plot the difference spectrogram
    fig, ax = plt.subplots()
    img = ax.imshow(spectrogram_difference_db, aspect="auto", origin="lower", cmap="inferno")
    ax.set_xlabel("Time")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Difference Spectrogram {input_file1} - {input_file2}")
    fig.colorbar(img, ax=ax, label="Magnitude (dB)")
    plt.show()

if __name__ == "__main__":
    print(f"Enter {__name__}")
    with io.open("./logging_config.yaml") as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)
    logger = logging.getLogger()

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description='Spectrogram')
    parser.add_argument('--process', dest='process', action='store_true')
    parser.add_argument('--plot', dest='plot', action='store_true')
    parser.add_argument('--diff', dest='diff', action='store_true')
    args = parser.parse_args()

    if args.process:
        create_spectrograph("../output/LNL222.mp3.wav","./LNL222.mp3.csv")
        create_spectrograph("../output/LNL222_5sec_ogg_wav_notrim.wav","./LNL222_5sec_ogg_wav_notrim.csv")
        create_spectrograph("../output/LNL222_5sec_aac_wav_trim.wav","./LNL222_5sec_aac_wav_trim.csv")

    if args.plot:
        plot_spectrogram("./LNL222.mp3.csv")
        plot_spectrogram("./LNL222_5sec_ogg_wav_notrim.csv")
        plot_spectrogram("./LNL222_5sec_aac_wav_trim.csv")

    if args.diff:
        diff_spectrogram("./LNL222.mp3.csv","./LNL222_5sec_ogg_wav_notrim.csv")

    exit(0)