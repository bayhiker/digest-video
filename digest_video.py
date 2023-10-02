import json
from argparse import ArgumentParser, ArgumentError
from video_editor import VideoEditor

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        prog="digest_video",
        description="Extract video clips with a json configuration file",
    )
    arg_parser.add_argument("-c", "--config", required=True, help="Configuration file")
    arg_parser.add_argument(
        "-i", "--input", required=True, help="Video file to extract from"
    )
    args = arg_parser.parse_args()
    if not args.config.endswith(".json"):
        arg_parser.error("Config file must be of json type")
    print(f"Parsing {args.input} with config file {args.config}")

    video_editor = VideoEditor(
        # "/home/mike/temp/soccer/video.mp4", "/home/mike/temp/soccer/test.json"
        args.input,
        args.config,
    )
    video_editor.digest()
