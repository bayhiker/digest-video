import os
import json
import ffmpeg
from shutil import rmtree


class VideoSegment:
    def __init__(self, start: str, length_in_seconds: int, note=None) -> None:
        self.start = start
        self.length_in_seconds = length_in_seconds
        self.note = note

    def __str__(self) -> str:
        return f"{self.start}-{self.length_in_seconds}-{self.note}"


class VideoEditor:
    def __init__(self, video_input: str, desc_file: str) -> None:
        self.video_input = video_input
        self.desc_file = desc_file
        self.output_folder = self.desc_file[0 : len(self.desc_file) - 5]

    def digest(self) -> None:
        config_json = json.load(open(self.desc_file))
        for t in config_json:
            print(f"Processing type {t}")
            segments: list[VideoSegment] = []
            for i in config_json[t]["segments"]:
                segments.append(VideoSegment(i["start"], i["length"], i["note"]))
            output_streams = []
            for segment in segments:
                print(f"Adding input segment {segment}")
                # f"{self.output_folder}/output-{segment.start.replace(':', '-')}.mp4"
                output_streams.append(
                    ffmpeg.input(
                        self.video_input, ss=segment.start, t=segment.length_in_seconds
                    ).filter("fade", type="in", start_time=0.4, duration=2)
                )
            merged_file = self.desc_file.replace(".json", f"-{t}.mp4")
            print(f"Writing to output file {merged_file}")
            ffmpeg.concat(*output_streams).output(merged_file).run()
