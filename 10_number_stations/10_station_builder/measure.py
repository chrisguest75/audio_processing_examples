import logging
import os
import av
from iterate_folder import iterate_folder


def audio_durations(file: str) -> None:
    av.logging.set_level(av.logging.VERBOSE)

    logger = logging.getLogger()
    input_file = av.open(file)

    if input_file.duration is not None:
        # container.duration is in microseconds, so convert it to seconds
        duration_seconds = input_file.duration / 1e6
    else:
        # If container.duration is not available, you can compute it from a specific stream.
        # For example, using the first video stream:
        stream = input_file.streams.video[0]
        duration_seconds = stream.duration * stream.time_base

    measure = {"file": file, "duration": duration_seconds}

    input_file.close()

    return measure


def measure(folder: str) -> None:
    logger = logging.getLogger()

    if not os.path.isfile(folder):
        measures = iterate_folder(folder, audio_durations)

        for item in measures:
            #print(item)
            logger.info(item)

        # find min and max durations
        min_duration = min([item["duration"] for item in measures])
        max_duration = max([item["duration"] for item in measures])

        logger.info({ "min_duration": {min_duration}, "max_duration": {max_duration} })            
    else:
        logger.error(f"Folder {folder} does not exist")


