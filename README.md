# Sample Command Line

```
python digest_video.py -c /path/to/config/config_name.json -i /path/to/input/video.mp4
```

# Sample Config JSON File

```
sample.json
{
  "welldone": {
    "segments": [
      { "start": "00:23:18.0", "length": 10, "note": "" },
      { "start": "00:57:20.0", "length": 20, "note": "" },
      { "start": "01:03:48.0", "length": 12, "note": "" }
    ]
  },
  "improve": {
    "segments": [
      { "start": "00:18:50.0", "length": 27, "note": "Go Faster!!!" },
      { "start": "00:19:19.0", "length": 13, "note": "" },
      { "start": "00:59:15.0", "length": 5, "note": "" },
      { "start": "01:01:12.0", "length": 7, "note": "" },
      { "start": "01:01:45.0", "length": 7, "note": "" },
      { "start": "01:02:44.0", "length": 6, "note": "" },
      { "start": "01:03:48.0", "length": 8, "note": "" }
    ]
  }
}
```

After running digest_video with this config fil, the following two digest video files will be generated:

```
/path/to/config/config_name-welldone.mp4
/path/to/config/config_name-improve.mp4

```
