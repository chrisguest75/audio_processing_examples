from abc import ABC, abstractmethod
import logging
import av
from av.audio.resampler import AudioResampler
import numpy as np


# create am abstract class for audio input
def audio_input_factory(audio_file: str):
    """Factory function to create an audio input object based on the audio type."""
    if audio_file.endswith('.mp3') or audio_file.endswith('.wav') or audio_file.endswith('.m4a'):
        audio_type = 'audio'
    elif audio_file.endswith('.pcm'):
        audio_type = 'pcm'
    else:
        raise ValueError(f"Unsupported audio file type: {audio_file}")
    
    if audio_type == 'audio':
        return AudioIn(audio_file)
    elif audio_type == 'pcm':
        return PCMAudioIn(audio_file)
    else:
        raise ValueError(f"Unsupported audio type: {audio_type}")


class AudioInput(ABC):
    def get_audio(self, layout='mono', format='s16', rate=16000):
        raise NotImplementedError("Subclasses should implement this method!")


class AudioIn(AudioInput):
    def __init__(self, audio_file: str):
        self.audio_file = audio_file
    
    def get_audio(self, layout='mono', format='s16', rate=16000):
        #av.logging.set_level(av.logging.VERBOSE)
        logger = logging.getLogger()    

        container = av.open(self.audio_file)
        audio_stream = next(s for s in container.streams if s.type == 'audio')

        logger.info(f"Loading audio {self.audio_file} converting to sample rate {rate}, channels {layout}, sample format {format}")
        resampler = AudioResampler(
                format=format,
                layout=layout,
                rate=rate
        )

        buffer = b''
        for packet in container.demux(audio_stream):
            logger.debug(f"Size: {packet.size} bytes, Duration: {packet.duration} frames, Timebase: {packet.time_base}, PTS: {packet.pts}, DTS: {packet.dts}, Corrupted: {packet.is_corrupt}")

            for frame in packet.decode():
                # Resample audio frame
                resampled_frame = resampler.resample(frame)
                # Extract PCM bytes directly from resampled frame
                pcm_int16 = resampled_frame[0].to_ndarray()[0]
                # convert chunk to float32le
                pcm_float32 = pcm_int16.astype(np.float32, order='C') / 32768.0
                # Write PCM bytes to WAV file
                pcm_bytes = pcm_float32.tobytes()
                buffer = buffer + pcm_bytes
                
                if len(buffer) >= 8000:
                    # yield the buffer and reset it
                    chunk = buffer
                    buffer = b''
                    yield chunk
                #logger.debug(f"Received: {frame} Resampled: {resampled_frame} PCM: {len(pcm_float32)} bytes")
                #yield 

        container.close()


class PCMAudioIn(AudioInput):
    def __init__(self, audio_file: str):
        self.audio_file = audio_file
    
    def get_audio(self, layout='mono', format='f32le', rate=16000):
        #av.logging.set_level(av.logging.VERBOSE)
        logger = logging.getLogger()    

        # open file an read in 1 second chunks 
        with open(self.audio_file, 'rb') as f:
            while True:
                chunk = f.read(rate * 4)

                if not chunk:
                    break
                logger.debug(f"PCM: {len(chunk)} bytes")
                yield chunk
