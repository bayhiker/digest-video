# Sample Command Line

python digest_video.py -c /path/to/config.json -i /path/to/video.mp4

# Sample Config JSON File

```
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
