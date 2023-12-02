# SPECTROGRAM

Generate Spectrographs for audio.  

TODO:

* Generate test tones to check the diffing.  
* Do some different codec tests at different bitrates.  

## Spectrograph

A spectrogram, also known as a spectrograph or sonogram, is a visual representation of the frequency content of an audio signal as it changes over time. It is a powerful tool for understanding the spectral characteristics and temporal evolution of sounds. To interpret a spectrogram, you'll need to understand its three main components: time, frequency, and amplitude.

* Time (X-axis): The horizontal axis of a spectrogram represents time. As you move from left to right, you are moving forward in time through the audio signal. Each vertical slice of the spectrogram represents the frequency content of the audio signal at a specific point in time.  

* Frequency (Y-axis): The vertical axis of a spectrogram represents frequency, typically displayed on a linear or logarithmic scale. Lower frequencies are at the bottom of the graph, while higher frequencies are at the top. The distribution of energy across the frequency axis indicates the presence of different frequency components within the audio signal at a particular point in time.  

* Amplitude (Color/Intensity): The amplitude of each frequency component is represented by color or intensity in the spectrogram. In most spectrograms, darker colors or lower intensities correspond to lower amplitudes, while brighter colors or higher intensities correspond to higher amplitudes. The amplitude at each point in the spectrogram indicates the strength of the corresponding frequency component in the audio signal at that specific time.  

To interpret a spectrogram, follow these steps:

* Observe the time-domain features: Look for patterns and changes in the spectrogram as you move from left to right along the time axis. This can help you identify specific events or sections in the audio signal.

* Analyze the frequency content: Examine the distribution of energy across the frequency axis at different points in time. This can help you identify the presence of different frequency components, such as fundamental frequencies, harmonics, or noise.

* Assess the amplitude: Pay attention to the color or intensity of the spectrogram, which represents the amplitude of the various frequency components. This can help you understand the relative strength and importance of different frequencies within the audio signal.  

* Identify patterns and features: Look for patterns and features in the spectrogram that are characteristic of specific sounds or events. For example, musical notes may appear as horizontal lines or "ridges" at their fundamental frequencies and harmonics, while noisy or unvoiced speech may appear as a more diffuse distribution of energy across the frequency axis.  

By understanding and analyzing the time, frequency, and amplitude components of a spectrogram, you can gain valuable insights into the spectral characteristics and temporal evolution of audio signals, aiding in tasks such as sound identification, noise reduction, or feature extraction.

## Generate

```sh
mkdir -p ./output
ffmpeg -y -hide_banner -i "./sources/audiobooks/christmas_short_works_2008_0812_64kb_mp3/english_christmas1873_macdonald_mtd_64kb.mp3" -lavfi showspectrumpic=s=4096x1024 ./output/spectrogram.png  
```

## Sonic Visualiser

Use Sonic Visualiser to view spectrum analysis.  

NOTE: I've not worked out how to export them yet.  

```sh
brew install sonic-visualiser
```

## Audacity

You can get a spectrogram view in audacity by dropping down the where the sample name is displayed to the left.  You can select multi-view.  

```sh
brew install audacity
```

## Python Install

Create a tool to diff spectrograms.  

Example creates a 16khz wav. It downsamples another to 8khz and then upsamples to 16khz so the spectrograms can be compared (same numpy array shape).  

```sh
# create two sources 16khz and 8khz
ffmpeg -y -hide_banner -i "../sources/audiobooks/christmas_short_works_2008_0812_64kb_mp3/english_christmas1873_macdonald_mtd_64kb.mp3" -ac 1 -ar 16000 "../output/english_christmas1873_macdonald_mtd_16khz.wav"

ffmpeg -y -hide_banner -i "../sources/audiobooks/christmas_short_works_2008_0812_64kb_mp3/english_christmas1873_macdonald_mtd_64kb.mp3" -ac 1 -ar 8000 "../output/english_christmas1873_macdonald_mtd_8khz.wav"

ffmpeg -y -hide_banner -i "../output/english_christmas1873_macdonald_mtd_8khz.wav" -ac 1 -ar 16000 "../output/english_christmas1873_macdonald_mtd_8khz_up.wav"


export PIPENV_VENV_IN_PROJECT=1
pipenv install
pipenv install numpy scipy matplotlib

# process
pipenv run start:process --input "../output/english_christmas1873_macdonald_mtd_16khz.wav" --output "./english_christmas1873_macdonald_mtd_16khz.wav.csv"

pipenv run start:process --input "../output/english_christmas1873_macdonald_mtd_8khz_up.wav" --output "./english_christmas1873_macdonald_mtd_8khz.wav.csv"

# plot
pipenv run start:plot --input "./english_christmas1873_macdonald_mtd_16khz.wav.csv"

pipenv run start:plot --input "./english_christmas1873_macdonald_mtd_8khz.wav.csv"

# diff
pipenv run start:diff --base "./english_christmas1873_macdonald_mtd_16khz.wav.csv" --input "./english_christmas1873_macdonald_mtd_8khz.wav.csv"
```

## Shell

```sh
pipenv shell
code . 
./spectrogram.py --plot --input "../output/LNL222.mp3.wav" --output "./LNL222.mp3.csv"
./spectrogram.py --diff
```

## Resources

* Sonic Visualiser [here](https://www.sonicvisualiser.org/)  
* Audacity [here](https://www.audacityteam.org/)  
