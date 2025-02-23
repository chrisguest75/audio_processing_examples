import logging
import os
import av
from iterate_folder import iterate_folder
from measure import audio_durations


def audio_timestretch(file: str, tempo: int, output: str) -> None:
    av.logging.set_level(av.logging.VERBOSE)

    input_file = av.open(file)
    output_file = av.open(output, mode="w", format="wav")

    input_stream = input_file.streams.audio[0]
    output_stream = output_file.add_stream("pcm_s16le", rate=input_stream.rate)

    graph = av.filter.Graph()
    graph.link_nodes(
        graph.add_abuffer(template=input_stream),
        graph.add("atempo", str(tempo)),
        graph.add("abuffersink"),
    ).configure()

    for frame in input_file.decode(input_stream):
        graph.push(frame)
        while True:
            try:
                for packet in output_stream.encode(graph.pull()):
                    output_file.mux(packet)
            except (av.BlockingIOError, av.EOFError):
                break

    # Flush the stream
    for packet in output_stream.encode(None):
        output_file.mux(packet)

    input_file.close()
    output_file.close()


def normalise(folder: str, output: str) -> None:
    logger = logging.getLogger()
    if not os.path.isdir(output):
        os.makedirs(output, exist_ok=True)
        logger.info({ "message": "Output folder created", "output": output })

    if not os.path.isfile(folder):
        measures = iterate_folder(folder, audio_durations)

        for item in measures:
            input_file = item["file"]
            filename = os.path.splitext(os.path.basename(input_file))
            output_file = os.path.join(output, filename[0] + ".wav")
            input_duration = item["duration"]

            logger.info({ "input_file": input_file, "output_file": output_file })
            tempo = min(0.9 / input_duration, 2.0) 
            tempo = max(tempo, 0.5)
            item["tempo"] = tempo
            audio_timestretch(input_file, tempo, output_file)

            logger.info(item)

        # find min and max durations
        min_duration = min([item["duration"] for item in measures])
        max_duration = max([item["duration"] for item in measures])

        logger.info({ "min_duration": {min_duration}, "max_duration": {max_duration} })
        
        measures = iterate_folder(output, audio_durations)

        for item in measures:
            #print(item)
            logger.info(item)

    else:
        logger.error(f"Folder {folder} does not exist")

