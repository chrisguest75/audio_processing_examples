import logging
import os
import av
from iterate_folder import iterate_folder
from measure import audio_durations
from fractions import Fraction

def build(folder: str, output: str) -> None:

    logger = logging.getLogger()

    measures = iterate_folder(folder, audio_durations)

    for item in measures:
        #print(item)
        logger.info(item)


def build_file(files: list, output_file: str) -> None:
    av.logging.set_level(av.logging.VERBOSE)

    # Open the first file to extract audio parameters
    first_input = av.open(files[0])
    in_stream = first_input.streams.audio[0]
    sample_rate = in_stream.rate
    channels = in_stream.channels
    layout = in_stream.layout
    first_input.close()

    # Open the output container in write mode
    output = av.open(output_file, mode="w")
    # Create an output audio stream.
    # Here we use the 'pcm_s16le' codec (standard for WAV files).
    out_stream = output.add_stream("pcm_s16le", rate=sample_rate)
    out_stream.channels = channels
    out_stream.layout = layout
    # Set the time base to 1/sample_rate (each tick is one sample)
    out_stream.time_base = Fraction(1, sample_rate)

    # This variable will track our cumulative presentation timestamp (PTS)
    cumulative_pts = 0

    # Process each input file sequentially
    for fname in files:
        container = av.open(fname)
        audio_stream = container.streams.audio[0]
        
        # Demux packets from the audio stream
        for packet in container.demux(audio_stream):
            # Decode the packet into frames
            for frame in packet.decode():
                # Reassign the frame's PTS to ensure continuous timing.
                # Here, we assume each frame’s duration is given by its sample count.
                frame.pts = cumulative_pts
                cumulative_pts += frame.samples
                
                # Encode the frame to output packets and mux them
                for out_packet in out_stream.encode(frame):
                    output.mux(out_packet)
        
        container.close()

    # Flush the encoder to process any buffered frames
    for out_packet in out_stream.encode():
        output.mux(out_packet)

    # Finalize and close the output container
    output.close()