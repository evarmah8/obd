from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TextQuery(BaseModel):
  text_query: str

# Replace this with your actual logic to retrieve data
# This is just an example using the provided hardcoded_json_data
def get_data():
  hardcoded_json_data = """
{
  "completed_at": "2024-03-12T16:53:07.951721Z",
  "created_at": "2024-03-12T16:52:07.819072Z",
  "error": null,
  "id": "3bu5hm3b3zenvypmunr777hiom",
  "input": {
    "file": "https://replicate.delivery/pbxt/KYeA5Qe9ejGPx20liTKwkawC46BJD26ei87J7oSIW0wWux2t/Dag%20Heward%20Mills%20Obadiah.mp3",
    "prompt": "Mark and Lex talking about AI.",
    "file_url": "",
    "num_speakers": 2,
    "group_segments": true,
    "offset_seconds": 0,
    "transcript_output_format": "words_only"
  },
  "logs": "ffmpeg version 4.4.2-0ubuntu0.22.04.1 Copyright (c) 2000-2021 the FFmpeg developers\nbuilt with gcc 11 (Ubuntu 11.2.0-19ubuntu1)\nconfiguration: --prefix=/usr --extra-version=0ubuntu0.22.04.1 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --arch=amd64 --enable-gpl --disable-stripping --enable-gnutls --enable-ladspa --enable-libaom --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libcodec2 --enable-libdav1d --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libjack --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librabbitmq --enable-librubberband --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libsrt --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzimg --enable-libzmq --enable-libzvbi --enable-lv2 --enable-omx --enable-openal --enable-opencl --enable-opengl --enable-sdl2 --enable-pocketsphinx --enable-librsvg --enable-libmfx --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libx264 --enable-shared\nlibavutil      56. 70.100 / 56. 70.100\nlibavcodec     58.134.100 / 58.134.100\nlibavformat    58. 76.100 / 58. 76.100\nlibavdevice    58. 13.100 / 58. 13.100\nlibavfilter     7.110.100 /  7.110.100\nlibswscale      5.  9.100 /  5.  9.100\nlibswresample   3.  9.100 /  3.  9.100\nlibpostproc    55.  9.100 / 55.  9.100\nInput #0, mp3, from '/tmp/tmp1bomli5dDag Heward Mills Obadiah.mp3':\nMetadata:\nencoder         : Lavf58.76.100\nDuration: 00:04:30.58, start: 0.023021, bitrate: 128 kb/s\nStream #0:0: Audio: mp3, 48000 Hz, stereo, fltp, 128 kb/s\nMetadata:\nencoder         : Lavc58.13\nStream mapping:\nStream #0:0 -> #0:0 (mp3 (mp3float) -> pcm_s16le (native))\nPress [q] to stop, [?] for help\nOutput #0, wav, to 'temp-1710262368349896032.wav':\nMetadata:\nISFT            : Lavf58.76.100\nStream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 16000 Hz, mono, s16, 256 kb/s\nMetadata:\nencoder         : Lavc58.134.100 pcm_s16le\nsize=       0kB time=00:00:00.00 bitrate=N/A speed=N/A\nsize=    8454kB time=00:04:30.53 bitrate= 256.0kbits/s speed= 841x\nvideo:0kB audio:8454kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.000901%\nStarting transcribing\nFinished with transcribing, took 15.696 seconds\nFinished with diarization, took 3.4773 seconds\nFinished with merging, took 0.00084114 seconds\nFinished with cleaning, took 0.00011468 seconds\nProcessing time: 19.174 seconds\ndone with inference",
  "metrics": {
    "predict_time": 20.365582,
    "total_time": 60.132649
  },
  "output": {
    "language": "en",
    "segments": [
      {
        "end": "55.42",
        "start": "0.75",
        "words": [
          {
            "end": 1.19,
            "word": "The",
            "start": 0.75,
            "probability": 0.8955078125
          },
          {
            "end": 1.33,
            "word": "book",
            "start": 1.19,
            "probability": 0.779296875
          },
          {
            "end": 1.51,
            "word": "of",
            "start": 1.33,
            "probability": 0.99951171875
          },
          {
            "end": 2.19,
            "word": "Obadiah,",
            "start": 1.51,
            "probability": 0.9993489583333334
          },
          {
            "end": 2.81,
            "word": "King",
            "start": 2.23,
            "probability": 0.9853515625
          },
          {
            "end": 3.17,
            "word": "James",
            "start": 2.81,
            "probability": 1
          },
          {
            "end": 3.63,
            "word": "Version,",
            "start": 3.17,
            "probability": 0.97998046875
          },
          {
            "end": 4.77,
            "word": "read",
            "start": 3.97,
            "probability": 0.98681640625
          },
          {
            "end": 5.47,
            "word": "by",
            "start": 4.77,
            "probability": 0.95263671875
          },
          {
            "end": 5.93,
            "word": "Justin",
            "start": 5.47,
            "probability": 0.99560546875
          },
          {
            "end": 6.43,
            "word": "Bible.",
            "start": 5.93,
            "probability": 0.9599609375
          },
          {
            "end": 7.65,
            "word": "May",
            "start": 7.35,
            "probability": 0.9873046875
          },
          {
            "end": 7.85,
            "word": "God",
            "start": 7.65,
            "probability": 0.99951171875
          },
          {
            "end": 8.15,
            "word": "bless",
            "start": 7.85,
            "probability": 0.99951171875
          },
          {
            "end": 8.43,
            "word": "you",
            "start": 8.15,
            "probability": 1
          },
          {
            "end": 9.29,
            "word": "with",
            "start": 8.43,
            "probability": 0.99267578125
          },
          {
            "end": 9.47,
            "word": "an",
            "start": 9.29,
            "probability": 0.9990234375
          },
          {
            "end": 10.15,
            "word": "unquenchable",
            "start": 9.47,
            "probability": 0.9998779296875
          },
          {
            "end": 10.53,
            "word": "thirst",
            "start": 10.15,
            "probability": 1
          },
          {
            "end": 11.29,
            "word": "for",
            "start": 10.53,
            "probability": 0.99951171875
          },
          {
            "end": 11.47,
            "word": "his",
            "start": 11.29,
            "probability": 0.51171875
          },
          {
            "end": 11.71,
            "word": "holy",
            "start": 11.47,
            "probability": 0.93212890625
          },
          {
            "end": 12.09,
            "word": "word,",
            "start": 11.71,
            "probability": 0.99755859375
          },
          {
            "end": 12.97,
            "word": "the",
            "start": 12.31,
            "probability": 0.9990234375
          },
          {
            "end": 13.29,
            "word": "Bible.",
            "start": 12.97,
            "probability": 1
          },
          {
            "end": 15.7,
            "word": "Obadiah,",
            "start": 15.1,
            "probability": 0.98974609375
          },
          {
            "end": 16.3,
            "word": "the",
            "start": 15.7,
            "probability": 0.9716796875
          },
          {
            "end": 16.68,
            "word": "vision",
            "start": 16.3,
            "probability": 0.9931640625
          },
          {
            "end": 17.06,
            "word": "of",
            "start": 16.68,
            "probability": 1
          },
          {
            "end": 17.82,
            "word": "Obadiah.",
            "start": 17.06,
            "probability": 1
          },
          {
            "end": 18.74,
            "word": "Thus",
            "start": 18.14,
            "probability": 0.97119140625
          },
          {
            "end": 19,
            "word": "saith",
            "start": 18.74,
            "probability": 0.9970703125
          },
          {
            "end": 19.16,
            "word": "the",
            "start": 19,
            "probability": 1
          },
          {
            "end": 19.36,
            "word": "Lord",
            "start": 19.16,
            "probability": 0.99951171875
          },
          {
            "end": 19.64,
            "word": "God",
            "start": 19.36,
            "probability": 0.99951171875
          },
          {
            "end": 20.14,
            "word": "concerning",
            "start": 19.64,
            "probability": 0.990234375
          },
          {
            "end": 20.76,
            "word": "Edom.",
            "start": 20.14,
            "probability": 0.99853515625
          },
          {
            "end": 21.38,
            "word": "We",
            "start": 20.86,
            "probability": 0.998046875
          },
          {
            "end": 21.52,
            "word": "have",
            "start": 21.38,
            "probability": 1
          },
          {
            "end": 21.72,
            "word": "heard",
            "start": 21.52,
            "probability": 1
          },
          {
            "end": 21.86,
            "word": "a",
            "start": 21.72,
            "probability": 1
          },
          {
            "end": 22.08,
            "word": "rumor",
            "start": 21.86,
            "probability": 0.9970703125
          },
          {
            "end": 22.34,
            "word": "from",
            "start": 22.08,
            "probability": 1
          },
          {
            "end": 22.48,
            "word": "the",
            "start": 22.34,
            "probability": 1
          },
          {
            "end": 22.82,
            "word": "Lord,",
            "start": 22.48,
            "probability": 1
          },
          {
            "end": 23.2,
            "word": "and",
            "start": 22.9,
            "probability": 0.9990234375
          },
          {
            "end": 23.36,
            "word": "an",
            "start": 23.2,
            "probability": 1
          },
          {
            "end": 23.8,
            "word": "ambassador",
            "start": 23.36,
            "probability": 0.99951171875
          },
          {
            "end": 24.08,
            "word": "is",
            "start": 23.8,
            "probability": 0.9951171875
          },
          {
            "end": 24.3,
            "word": "sent",
            "start": 24.08,
            "probability": 1
          },
          {
            "end": 24.56,
            "word": "among",
            "start": 24.3,
            "probability": 0.99951171875
          },
          {
            "end": 24.78,
            "word": "the",
            "start": 24.56,
            "probability": 1
          },
          {
            "end": 25.2,
            "word": "heathen.",
            "start": 24.78,
            "probability": 0.9998372395833334
          },
          {
            "end": 26.04,
            "word": "Arise",
            "start": 25.44,
            "probability": 0.999755859375
          },
          {
            "end": 26.18,
            "word": "ye,",
            "start": 26.04,
            "probability": 0.93408203125
          },
          {
            "end": 26.62,
            "word": "and",
            "start": 26.28,
            "probability": 1
          },
          {
            "end": 26.72,
            "word": "let",
            "start": 26.62,
            "probability": 1
          },
          {
            "end": 26.9,
            "word": "us",
            "start": 26.72,
            "probability": 1
          },
          {
            "end": 27.1,
            "word": "rise",
            "start": 26.9,
            "probability": 1
          },
          {
            "end": 27.34,
            "word": "up",
            "start": 27.1,
            "probability": 1
          },
          {
            "end": 27.6,
            "word": "against",
            "start": 27.34,
            "probability": 1
          },
          {
            "end": 27.9,
            "word": "her",
            "start": 27.6,
            "probability": 0.99951171875
          },
          {
            "end": 28.12,
            "word": "in",
            "start": 27.9,
            "probability": 0.90625
          },
          {
            "end": 28.46,
            "word": "battle.",
            "start": 28.12,
            "probability": 1
          },
          {
            "end": 29.9,
            "word": "Behold,",
            "start": 29.3,
            "probability": 0.589111328125
          },
          {
            "end": 30.32,
            "word": "I",
            "start": 30,
            "probability": 0.9990234375
          },
          {
            "end": 30.46,
            "word": "have",
            "start": 30.32,
            "probability": 0.9990234375
          },
          {
            "end": 30.72,
            "word": "made",
            "start": 30.46,
            "probability": 1
          },
          {
            "end": 30.86,
            "word": "thee",
            "start": 30.72,
            "probability": 0.99853515625
          },
          {
            "end": 31.18,
            "word": "small",
            "start": 30.86,
            "probability": 1
          },
          {
            "end": 31.48,
            "word": "among",
            "start": 31.18,
            "probability": 1
          },
          {
            "end": 31.7,
            "word": "the",
            "start": 31.48,
            "probability": 1
          },
          {
            "end": 32.12,
            "word": "heathen.",
            "start": 31.7,
            "probability": 1
          },
          {
            "end": 32.64,
            "word": "Thou",
            "start": 32.14,
            "probability": 0.999267578125
          },
          {
            "end": 32.8,
            "word": "art",
            "start": 32.64,
            "probability": 0.99951171875
          },
          {
            "end": 33.1,
            "word": "greatly",
            "start": 32.8,
            "probability": 1
          },
          {
            "end": 33.82,
            "word": "despised.",
            "start": 33.1,
            "probability": 0.99658203125
          },
          {
            "end": 34.92,
            "word": "The",
            "start": 34.62,
            "probability": 0.99462890625
          },
          {
            "end": 35.22,
            "word": "pride",
            "start": 34.92,
            "probability": 1
          },
          {
            "end": 35.44,
            "word": "of",
            "start": 35.22,
            "probability": 1
          },
          {
            "end": 35.68,
            "word": "thine",
            "start": 35.44,
            "probability": 0.999755859375
          },
          {
            "end": 35.96,
            "word": "heart",
            "start": 35.68,
            "probability": 1
          },
          {
            "end": 36.3,
            "word": "hath",
            "start": 35.96,
            "probability": 0.97998046875
          },
          {
            "end": 36.68,
            "word": "deceived",
            "start": 36.3,
            "probability": 1
          },
          {
            "end": 37.02,
            "word": "thee.",
            "start": 36.68,
            "probability": 1
          },
          {
            "end": 37.54,
            "word": "Thou",
            "start": 37.16,
            "probability": 0.997802734375
          },
          {
            "end": 37.7,
            "word": "that",
            "start": 37.54,
            "probability": 0.9990234375
          },
          {
            "end": 38.12,
            "word": "dwellest",
            "start": 37.7,
            "probability": 0.999267578125
          },
          {
            "end": 38.28,
            "word": "in",
            "start": 38.12,
            "probability": 1
          },
          {
            "end": 38.36,
            "word": "the",
            "start": 38.28,
            "probability": 1
          },
          {
            "end": 38.82,
            "word": "clefts",
            "start": 38.36,
            "probability": 0.84033203125
          },
          {
            "end": 38.86,
            "word": "of",
            "start": 38.82,
            "probability": 0.9970703125
          },
          {
            "end": 39.04,
            "word": "the",
            "start": 38.86,
            "probability": 1
          },
          {
            "end": 39.34,
            "word": "rock,",
            "start": 39.04,
            "probability": 1
          },
          {
            "end": 39.96,
            "word": "whose",
            "start": 39.5,
            "probability": 0.9794921875
          },
          {
            "end": 40.52,
            "word": "habitation",
            "start": 39.96,
            "probability": 0.999267578125
          },
          {
            "end": 40.78,
            "word": "is",
            "start": 40.52,
            "probability": 1
          },
          {
            "end": 41.12,
            "word": "high,",
            "start": 40.78,
            "probability": 1
          },
          {
            "end": 41.54,
            "word": "that",
            "start": 41.3,
            "probability": 0.8837890625
          },
          {
            "end": 41.98,
            "word": "saith",
            "start": 41.54,
            "probability": 0.806884765625
          },
          {
            "end": 42.16,
            "word": "in",
            "start": 41.98,
            "probability": 1
          },
          {
            "end": 42.34,
            "word": "his",
            "start": 42.16,
            "probability": 0.99755859375
          },
          {
            "end": 42.66,
            "word": "heart,",
            "start": 42.34,
            "probability": 1
          },
          {
            "end": 43.3,
            "word": "Who",
            "start": 42.86,
            "probability": 0.91796875
          },
          {
            "end": 43.8,
            "word": "shall",
            "start": 43.3,
            "probability": 0.99951171875
          },
          {
            "end": 44.12,
            "word": "bring",
            "start": 43.8,
            "probability": 1
          },
          {
            "end": 44.44,
            "word": "me",
            "start": 44.12,
            "probability": 1
          },
          {
            "end": 45.22,
            "word": "down",
            "start": 44.44,
            "probability": 0.9990234375
          },
          {
            "end": 45.48,
            "word": "to",
            "start": 45.22,
            "probability": 1
          },
          {
            "end": 45.58,
            "word": "the",
            "start": 45.48,
            "probability": 1
          },
          {
            "end": 46.04,
            "word": "ground?",
            "start": 45.58,
            "probability": 1
          },
          {
            "end": 47.2,
            "word": "Though",
            "start": 46.6,
            "probability": 0.9755859375
          },
          {
            "end": 47.54,
            "word": "thou",
            "start": 47.2,
            "probability": 1
          },
          {
            "end": 47.96,
            "word": "exalt",
            "start": 47.54,
            "probability": 0.998779296875
          },
          {
            "end": 48.48,
            "word": "thyself",
            "start": 47.96,
            "probability": 0.99951171875
          },
          {
            "end": 48.8,
            "word": "as",
            "start": 48.48,
            "probability": 1
          },
          {
            "end": 48.88,
            "word": "the",
            "start": 48.8,
            "probability": 1
          },
          {
            "end": 49.26,
            "word": "eagle,",
            "start": 48.88,
            "probability": 0.99853515625
          },
          {
            "end": 49.96,
            "word": "and",
            "start": 49.46,
            "probability": 0.99462890625
          },
          {
            "end": 50.1,
            "word": "though",
            "start": 49.96,
            "probability": 0.99658203125
          },
          {
            "end": 50.3,
            "word": "thou",
            "start": 50.1,
            "probability": 1
          },
          {
            "end": 50.6,
            "word": "set",
            "start": 50.3,
            "probability": 0.99951171875
          },
          {
            "end": 50.8,
            "word": "thy",
            "start": 50.6,
            "probability": 0.99609375
          },
          {
            "end": 51.1,
            "word": "nest",
            "start": 50.8,
            "probability": 1
          },
          {
            "end": 51.4,
            "word": "among",
            "start": 51.1,
            "probability": 1
          },
          {
            "end": 51.6,
            "word": "the",
            "start": 51.4,
            "probability": 1
          },
          {
            "end": 51.98,
            "word": "stars,",
            "start": 51.6,
            "probability": 1
          },
          {
            "end": 52.92,
            "word": "thence",
            "start": 52.38,
            "probability": 0.95263671875
          },
          {
            "end": 53.08,
            "word": "will",
            "start": 52.92,
            "probability": 0.99951171875
          },
          {
            "end": 53.28,
            "word": "I",
            "start": 53.08,
            "probability": 1
          },
          {
            "end": 53.54,
            "word": "bring",
            "start": 53.28,
            "probability": 1
          },
          {
            "end": 53.78,
            "word": "thee",
            "start": 53.54,
            "probability": 1
          },
          {
            "end": 54.24,
            "word": "down,",
            "start": 53.78,
            "probability": 1
          },
          {
            "end": 54.96,
            "word": "saith",
            "start": 54.4,
            "probability": 0.998779296875
          },
          {
            "end": 55.18,
            "word": "the",
            "start": 54.96,
            "probability": 1
          },
          {
            "end": 55.42,
            "word": "Lord.",
            "start": 55.18,
            "probability": 0.994140625
          }
        ],
        "speaker": "SPEAKER_01",
        "avg_logprob": -0.18464543928320593
      },
      {
        "end": "71.96",
        "start": "55.88",
        "words": [
          {
            "end": 56.48,
            "word": "If",
            "start": 55.88,
            "probability": 0.9970703125
          },
          {
            "end": 56.84,
            "word": "thieves",
            "start": 56.48,
            "probability": 0.99853515625
          },
          {
            "end": 57.16,
            "word": "came",
            "start": 56.84,
            "probability": 0.9970703125
          },
          {
            "end": 57.42,
            "word": "to",
            "start": 57.16,
            "probability": 1
          },
          {
            "end": 57.6,
            "word": "thee.",
            "start": 57.42,
            "probability": 1
          },
          {
            "end": 58.32,
            "word": "If",
            "start": 57.72,
            "probability": 0.9501953125
          },
          {
            "end": 58.44,
            "word": "thieves",
            "start": 58.32,
            "probability": 0.324462890625
          },
          {
            "end": 58.44,
            "word": "came",
            "start": 58.44,
            "probability": 0.9912109375
          },
          {
            "end": 58.44,
            "word": "to",
            "start": 58.44,
            "probability": 0.998046875
          },
          {
            "end": 58.44,
            "word": "thee.",
            "start": 58.44,
            "probability": 0.99462890625
          },
          {
            "end": 58.48,
            "word": "If",
            "start": 58.46,
            "probability": 0.00164031982421875
          },
          {
            "end": 58.74,
            "word": "robbers",
            "start": 58.48,
            "probability": 0.5026321411132812
          },
          {
            "end": 58.98,
            "word": "by",
            "start": 58.74,
            "probability": 0.8935546875
          },
          {
            "end": 59.34,
            "word": "night,",
            "start": 58.98,
            "probability": 0.99951171875
          },
          {
            "end": 59.98,
            "word": "how",
            "start": 59.44,
            "probability": 0.99658203125
          },
          {
            "end": 60.24,
            "word": "art",
            "start": 59.98,
            "probability": 0.96923828125
          },
          {
            "end": 60.44,
            "word": "thou",
            "start": 60.24,
            "probability": 0.99853515625
          },
          {
            "end": 60.66,
            "word": "cut",
            "start": 60.44,
            "probability": 1
          },
          {
            "end": 60.98,
            "word": "off?",
            "start": 60.66,
            "probability": 1
          },
          {
            "end": 61.92,
            "word": "Would",
            "start": 61.4,
            "probability": 0.9931640625
          },
          {
            "end": 62.06,
            "word": "they",
            "start": 61.92,
            "probability": 0.99951171875
          },
          {
            "end": 62.24,
            "word": "not",
            "start": 62.06,
            "probability": 1
          },
          {
            "end": 62.38,
            "word": "have",
            "start": 62.24,
            "probability": 1
          },
          {
            "end": 62.84,
            "word": "stolen",
            "start": 62.38,
            "probability": 0.99609375
          },
          {
            "end": 63.12,
            "word": "till",
            "start": 62.84,
            "probability": 0.99560546875
          },
          {
            "end": 63.3,
            "word": "they",
            "start": 63.12,
            "probability": 1
          },
          {
            "end": 63.46,
            "word": "had",
            "start": 63.3,
            "probability": 0.99951171875
          },
          {
            "end": 63.8,
            "word": "enough?",
            "start": 63.46,
            "probability": 1
          },
          {
            "end": 64.86,
            "word": "If",
            "start": 64.34,
            "probability": 0.9990234375
          },
          {
            "end": 64.98,
            "word": "the",
            "start": 64.86,
            "probability": 0.99951171875
          },
          {
            "end": 65.18,
            "word": "great",
            "start": 64.98,
            "probability": 0.5390625
          },
          {
            "end": 65.8,
            "word": "gatherers",
            "start": 65.18,
            "probability": 0.99951171875
          },
          {
            "end": 66.06,
            "word": "came",
            "start": 65.8,
            "probability": 1
          },
          {
            "end": 66.32,
            "word": "to",
            "start": 66.06,
            "probability": 1
          },
          {
            "end": 66.5,
            "word": "thee,",
            "start": 66.32,
            "probability": 0.99951171875
          },
          {
            "end": 67.08,
            "word": "would",
            "start": 66.68,
            "probability": 0.99755859375
          },
          {
            "end": 67.2,
            "word": "they",
            "start": 67.08,
            "probability": 1
          },
          {
            "end": 67.38,
            "word": "not",
            "start": 67.2,
            "probability": 1
          },
          {
            "end": 67.6,
            "word": "leave",
            "start": 67.38,
            "probability": 1
          },
          {
            "end": 67.86,
            "word": "some",
            "start": 67.6,
            "probability": 1
          },
          {
            "end": 68.3,
            "word": "grapes?",
            "start": 67.86,
            "probability": 0.99951171875
          },
          {
            "end": 69.8,
            "word": "How",
            "start": 69.28,
            "probability": 0.99853515625
          },
          {
            "end": 70.04,
            "word": "are",
            "start": 69.8,
            "probability": 1
          },
          {
            "end": 70.18,
            "word": "the",
            "start": 70.04,
            "probability": 1
          },
          {
            "end": 70.48,
            "word": "things",
            "start": 70.18,
            "probability": 1
          },
          {
            "end": 70.66,
            "word": "of",
            "start": 70.48,
            "probability": 1
          },
          {
            "end": 71.12,
            "word": "Esau",
            "start": 70.66,
            "probability": 0.999755859375
          },
          {
            "end": 71.6,
            "word": "searched",
            "start": 71.12,
            "probability": 0.99951171875
          },
          {
            "end": 71.96,
            "word": "out?",
            "start": 71.6,
            "probability": 1
          }
        ],
        "speaker": "SPEAKER_00",
        "avg_logprob": -0.1461657818327559
      },
      {
        "end": "263.77",
        "start": "72.34",
        "words": [
          {
            "end": 72.86,
            "word": "How",
            "start": 72.34,
            "probability": 1
          },
          {
            "end": 73.06,
            "word": "are",
            "start": 72.86,
            "probability": 1
          },
          {
            "end": 73.28,
            "word": "his",
            "start": 73.06,
            "probability": 0.9990234375
          },
          {
            "end": 73.56,
            "word": "hidden",
            "start": 73.28,
            "probability": 1
          },
          {
            "end": 73.92,
            "word": "things",
            "start": 73.56,
            "probability": 1
          },
          {
            "end": 74.3,
            "word": "sought",
            "start": 73.92,
            "probability": 0.99169921875
          },
          {
            "end": 74.58,
            "word": "up?",
            "start": 74.3,
            "probability": 0.998046875
          },
          {
            "end": 75.72,
            "word": "All",
            "start": 75.2,
            "probability": 0.9990234375
          },
          {
            "end": 75.9,
            "word": "the",
            "start": 75.72,
            "probability": 1
          },
          {
            "end": 76.06,
            "word": "men",
            "start": 75.9,
            "probability": 1
          },
          {
            "end": 76.2,
            "word": "of",
            "start": 76.06,
            "probability": 1
          },
          {
            "end": 76.3,
            "word": "thy",
            "start": 76.2,
            "probability": 0.99951171875
          },
          {
            "end": 76.98,
            "word": "confederacy",
            "start": 76.3,
            "probability": 0.9977213541666666
          },
          {
            "end": 77.22,
            "word": "have",
            "start": 76.98,
            "probability": 0.99951171875
          },
          {
            "end": 77.52,
            "word": "brought",
            "start": 77.22,
            "probability": 1
          },
          {
            "end": 77.78,
            "word": "thee",
            "start": 77.52,
            "probability": 1
          },
          {
            "end": 78.16,
            "word": "even",
            "start": 77.78,
            "probability": 0.951171875
          },
          {
            "end": 78.36,
            "word": "to",
            "start": 78.16,
            "probability": 1
          },
          {
            "end": 78.48,
            "word": "the",
            "start": 78.36,
            "probability": 1
          },
          {
            "end": 78.78,
            "word": "border.",
            "start": 78.48,
            "probability": 0.9990234375
          },
          {
            "end": 79.44,
            "word": "The",
            "start": 79.04,
            "probability": 1
          },
          {
            "end": 79.64,
            "word": "men",
            "start": 79.44,
            "probability": 1
          },
          {
            "end": 79.8,
            "word": "that",
            "start": 79.64,
            "probability": 1
          },
          {
            "end": 79.9,
            "word": "were",
            "start": 79.8,
            "probability": 1
          },
          {
            "end": 80.06,
            "word": "at",
            "start": 79.9,
            "probability": 0.99853515625
          },
          {
            "end": 80.32,
            "word": "peace",
            "start": 80.06,
            "probability": 1
          },
          {
            "end": 80.56,
            "word": "with",
            "start": 80.32,
            "probability": 1
          },
          {
            "end": 80.78,
            "word": "thee",
            "start": 80.56,
            "probability": 1
          },
          {
            "end": 81.12,
            "word": "have",
            "start": 80.78,
            "probability": 0.99658203125
          },
          {
            "end": 81.5,
            "word": "deceived",
            "start": 81.12,
            "probability": 0.99951171875
          },
          {
            "end": 81.86,
            "word": "thee,",
            "start": 81.5,
            "probability": 1
          },
          {
            "end": 82.36,
            "word": "and",
            "start": 81.98,
            "probability": 0.986328125
          },
          {
            "end": 82.8,
            "word": "prevailed",
            "start": 82.36,
            "probability": 0.820068359375
          },
          {
            "end": 83.12,
            "word": "against",
            "start": 82.8,
            "probability": 1
          },
          {
            "end": 83.5,
            "word": "thee.",
            "start": 83.12,
            "probability": 1
          },
          {
            "end": 84.12,
            "word": "They",
            "start": 83.72,
            "probability": 0.9990234375
          },
          {
            "end": 84.36,
            "word": "that",
            "start": 84.12,
            "probability": 1
          },
          {
            "end": 84.58,
            "word": "eat",
            "start": 84.36,
            "probability": 0.99951171875
          },
          {
            "end": 84.74,
            "word": "thy",
            "start": 84.58,
            "probability": 0.998046875
          },
          {
            "end": 85.04,
            "word": "bread",
            "start": 84.74,
            "probability": 1
          },
          {
            "end": 85.46,
            "word": "have",
            "start": 85.04,
            "probability": 0.9990234375
          },
          {
            "end": 85.72,
            "word": "laid",
            "start": 85.46,
            "probability": 1
          },
          {
            "end": 85.84,
            "word": "a",
            "start": 85.72,
            "probability": 1
          },
          {
            "end": 86.1,
            "word": "wound",
            "start": 85.84,
            "probability": 0.9990234375
          },
          {
            "end": 86.46,
            "word": "under",
            "start": 86.1,
            "probability": 0.9990234375
          },
          {
            "end": 86.68,
            "word": "thee.",
            "start": 86.46,
            "probability": 1
          },
          {
            "end": 87.38,
            "word": "There",
            "start": 86.86,
            "probability": 0.998046875
          },
          {
            "end": 87.56,
            "word": "is",
            "start": 87.38,
            "probability": 1
          },
          {
            "end": 87.8,
            "word": "none",
            "start": 87.56,
            "probability": 0.9990234375
          },
          {
            "end": 88.34,
            "word": "understanding.",
            "start": 87.8,
            "probability": 0.4248046875
          },
          {
            "end": 89.78,
            "word": "Shall",
            "start": 89.26,
            "probability": 0.501953125
          },
          {
            "end": 90.3,
            "word": "I",
            "start": 89.78,
            "probability": 0.9990234375
          },
          {
            "end": 90.54,
            "word": "not",
            "start": 90.3,
            "probability": 0.99951171875
          },
          {
            "end": 90.88,
            "word": "in",
            "start": 90.54,
            "probability": 0.986328125
          },
          {
            "end": 91.04,
            "word": "that",
            "start": 90.88,
            "probability": 1
          },
          {
            "end": 91.36,
            "word": "day,",
            "start": 91.04,
            "probability": 1
          },
          {
            "end": 91.66,
            "word": "saith",
            "start": 91.42,
            "probability": 0.993896484375
          },
          {
            "end": 91.86,
            "word": "the",
            "start": 91.66,
            "probability": 1
          },
          {
            "end": 92.08,
            "word": "Lord,",
            "start": 91.86,
            "probability": 0.9931640625
          },
          {
            "end": 92.64,
            "word": "even",
            "start": 92.28,
            "probability": 0.99658203125
          },
          {
            "end": 93,
            "word": "destroy",
            "start": 92.64,
            "probability": 1
          },
          {
            "end": 93.32,
            "word": "the",
            "start": 93,
            "probability": 1
          },
          {
            "end": 93.6,
            "word": "wise",
            "start": 93.32,
            "probability": 1
          },
          {
            "end": 93.88,
            "word": "men",
            "start": 93.6,
            "probability": 1
          },
          {
            "end": 94.12,
            "word": "out",
            "start": 93.88,
            "probability": 1
          },
          {
            "end": 94.28,
            "word": "of",
            "start": 94.12,
            "probability": 1
          },
          {
            "end": 94.56,
            "word": "Edom,",
            "start": 94.28,
            "probability": 0.99853515625
          },
          {
            "end": 95.04,
            "word": "and",
            "start": 94.66,
            "probability": 0.98681640625
          },
          {
            "end": 95.54,
            "word": "understanding",
            "start": 95.04,
            "probability": 0.99609375
          },
          {
            "end": 96.02,
            "word": "out",
            "start": 95.54,
            "probability": 0.99951171875
          },
          {
            "end": 96.16,
            "word": "of",
            "start": 96.02,
            "probability": 1
          },
          {
            "end": 96.26,
            "word": "the",
            "start": 96.16,
            "probability": 1
          },
          {
            "end": 96.52,
            "word": "mount",
            "start": 96.26,
            "probability": 0.857421875
          },
          {
            "end": 96.84,
            "word": "of",
            "start": 96.52,
            "probability": 1
          },
          {
            "end": 97.22,
            "word": "Esau?",
            "start": 96.84,
            "probability": 0.999755859375
          },
          {
            "end": 98.16,
            "word": "And",
            "start": 97.64,
            "probability": 0.96826171875
          },
          {
            "end": 98.28,
            "word": "thy",
            "start": 98.16,
            "probability": 0.9765625
          },
          {
            "end": 98.6,
            "word": "mighty",
            "start": 98.28,
            "probability": 1
          },
          {
            "end": 98.86,
            "word": "men,",
            "start": 98.6,
            "probability": 1
          },
          {
            "end": 99.1,
            "word": "O",
            "start": 99.02,
            "probability": 0.99462890625
          },
          {
            "end": 99.5,
            "word": "temen,",
            "start": 99.1,
            "probability": 0.47998046875
          },
          {
            "end": 99.94,
            "word": "shall",
            "start": 99.62,
            "probability": 0.9990234375
          },
          {
            "end": 100.14,
            "word": "be",
            "start": 99.94,
            "probability": 1
          },
          {
            "end": 100.46,
            "word": "dismayed,",
            "start": 100.14,
            "probability": 0.9990234375
          },
          {
            "end": 101.34,
            "word": "to",
            "start": 101,
            "probability": 0.99658203125
          },
          {
            "end": 101.46,
            "word": "the",
            "start": 101.34,
            "probability": 1
          },
          {
            "end": 101.76,
            "word": "end",
            "start": 101.46,
            "probability": 1
          },
          {
            "end": 101.94,
            "word": "that",
            "start": 101.76,
            "probability": 0.9873046875
          },
          {
            "end": 102.22,
            "word": "every",
            "start": 101.94,
            "probability": 0.994140625
          },
          {
            "end": 102.44,
            "word": "one",
            "start": 102.22,
            "probability": 1
          },
          {
            "end": 102.62,
            "word": "of",
            "start": 102.44,
            "probability": 1
          },
          {
            "end": 102.72,
            "word": "the",
            "start": 102.62,
            "probability": 0.99951171875
          },
          {
            "end": 102.94,
            "word": "mount",
            "start": 102.72,
            "probability": 0.99853515625
          },
          {
            "end": 103.12,
            "word": "of",
            "start": 102.94,
            "probability": 1
          },
          {
            "end": 103.56,
            "word": "Esau",
            "start": 103.12,
            "probability": 1
          },
          {
            "end": 103.98,
            "word": "may",
            "start": 103.56,
            "probability": 0.998046875
          },
          {
            "end": 104.18,
            "word": "be",
            "start": 103.98,
            "probability": 1
          },
          {
            "end": 104.34,
            "word": "cut",
            "start": 104.18,
            "probability": 1
          },
          {
            "end": 104.6,
            "word": "off",
            "start": 104.34,
            "probability": 1
          },
          {
            "end": 104.84,
            "word": "by",
            "start": 104.6,
            "probability": 1
          },
          {
            "end": 105.22,
            "word": "slaughter.",
            "start": 104.84,
            "probability": 1
          },
          {
            "end": 106.12,
            "word": "For",
            "start": 105.6,
            "probability": 0.99853515625
          },
          {
            "end": 106.26,
            "word": "thy",
            "start": 106.12,
            "probability": 0.99951171875
          },
          {
            "end": 106.62,
            "word": "violence",
            "start": 106.26,
            "probability": 1
          },
          {
            "end": 106.94,
            "word": "against",
            "start": 106.62,
            "probability": 1
          },
          {
            "end": 107.2,
            "word": "thy",
            "start": 106.94,
            "probability": 1
          },
          {
            "end": 107.44,
            "word": "brother",
            "start": 107.2,
            "probability": 1
          },
          {
            "end": 107.86,
            "word": "Jacob,",
            "start": 107.44,
            "probability": 0.99951171875
          },
          {
            "end": 108.84,
            "word": "shame",
            "start": 108.2,
            "probability": 0.99951171875
          },
          {
            "end": 109.1,
            "word": "shall",
            "start": 108.84,
            "probability": 1
          },
          {
            "end": 109.42,
            "word": "cover",
            "start": 109.1,
            "probability": 1
          },
          {
            "end": 109.68,
            "word": "thee,",
            "start": 109.42,
            "probability": 1
          },
          {
            "end": 110.2,
            "word": "and",
            "start": 109.82,
            "probability": 1
          },
          {
            "end": 110.32,
            "word": "thou",
            "start": 110.2,
            "probability": 1
          },
          {
            "end": 110.62,
            "word": "shalt",
            "start": 110.32,
            "probability": 0.999267578125
          },
          {
            "end": 110.8,
            "word": "be",
            "start": 110.62,
            "probability": 1
          },
          {
            "end": 111.04,
            "word": "cut",
            "start": 110.8,
            "probability": 1
          },
          {
            "end": 111.34,
            "word": "off",
            "start": 111.04,
            "probability": 1
          },
          {
            "end": 111.74,
            "word": "forever.",
            "start": 111.34,
            "probability": 0.95751953125
          },
          {
            "end": 113.44,
            "word": "On",
            "start": 112.92,
            "probability": 0.99853515625
          },
          {
            "end": 113.56,
            "word": "the",
            "start": 113.44,
            "probability": 1
          },
          {
            "end": 113.8,
            "word": "day",
            "start": 113.56,
            "probability": 1
          },
          {
            "end": 113.96,
            "word": "that",
            "start": 113.8,
            "probability": 1
          },
          {
            "end": 114.12,
            "word": "thou",
            "start": 113.96,
            "probability": 1
          },
          {
            "end": 114.66,
            "word": "stoodest",
            "start": 114.12,
            "probability": 0.99365234375
          },
          {
            "end": 114.78,
            "word": "on",
            "start": 114.66,
            "probability": 1
          },
          {
            "end": 114.88,
            "word": "the",
            "start": 114.78,
            "probability": 1
          },
          {
            "end": 115.1,
            "word": "other",
            "start": 114.88,
            "probability": 1
          },
          {
            "end": 115.56,
            "word": "side,",
            "start": 115.1,
            "probability": 1
          },
          {
            "end": 116.22,
            "word": "and",
            "start": 115.74,
            "probability": 0.99951171875
          },
          {
            "end": 116.32,
            "word": "the",
            "start": 116.22,
            "probability": 1
          },
          {
            "end": 116.54,
            "word": "day",
            "start": 116.32,
            "probability": 1
          },
          {
            "end": 116.74,
            "word": "that",
            "start": 116.54,
            "probability": 1
          },
          {
            "end": 116.84,
            "word": "the",
            "start": 116.74,
            "probability": 0.99951171875
          },
          {
            "end": 117.36,
            "word": "strangers",
            "start": 116.84,
            "probability": 0.9990234375
          },
          {
            "end": 117.94,
            "word": "carried",
            "start": 117.36,
            "probability": 0.99365234375
          },
          {
            "end": 118.22,
            "word": "away",
            "start": 117.94,
            "probability": 0.9990234375
          },
          {
            "end": 118.72,
            "word": "captive,",
            "start": 118.22,
            "probability": 0.62744140625
          },
          {
            "end": 118.94,
            "word": "his",
            "start": 118.94,
            "probability": 0.0418701171875
          },
          {
            "end": 119.44,
            "word": "forces,",
            "start": 118.94,
            "probability": 0.9443359375
          },
          {
            "end": 119.9,
            "word": "and",
            "start": 119.58,
            "probability": 0.9951171875
          },
          {
            "end": 120.36,
            "word": "foreigners",
            "start": 119.9,
            "probability": 0.9970703125
          },
          {
            "end": 120.74,
            "word": "entered",
            "start": 120.36,
            "probability": 0.99755859375
          },
          {
            "end": 121.06,
            "word": "into",
            "start": 120.74,
            "probability": 0.9990234375
          },
          {
            "end": 121.28,
            "word": "his",
            "start": 121.06,
            "probability": 0.998046875
          },
          {
            "end": 121.78,
            "word": "gates,",
            "start": 121.28,
            "probability": 1
          },
          {
            "end": 122.14,
            "word": "and",
            "start": 121.84,
            "probability": 0.99951171875
          },
          {
            "end": 122.36,
            "word": "cast",
            "start": 122.14,
            "probability": 0.99951171875
          },
          {
            "end": 122.68,
            "word": "lots",
            "start": 122.36,
            "probability": 0.98876953125
          },
          {
            "end": 122.92,
            "word": "upon",
            "start": 122.68,
            "probability": 1
          },
          {
            "end": 123.52,
            "word": "Jerusalem,",
            "start": 122.92,
            "probability": 1
          },
          {
            "end": 124.34,
            "word": "even",
            "start": 123.8,
            "probability": 0.998046875
          },
          {
            "end": 124.76,
            "word": "thou",
            "start": 124.34,
            "probability": 0.998046875
          },
          {
            "end": 125.5,
            "word": "wast",
            "start": 124.76,
            "probability": 0.9560546875
          },
          {
            "end": 125.72,
            "word": "as",
            "start": 125.5,
            "probability": 0.99072265625
          },
          {
            "end": 126.06,
            "word": "one",
            "start": 125.72,
            "probability": 1
          },
          {
            "end": 126.24,
            "word": "of",
            "start": 126.06,
            "probability": 1
          },
          {
            "end": 126.54,
            "word": "them.",
            "start": 126.24,
            "probability": 1
          },
          {
            "end": 128.23,
            "word": "But",
            "start": 127.75,
            "probability": 0.9912109375
          },
          {
            "end": 128.39,
            "word": "thou",
            "start": 128.23,
            "probability": 1
          },
          {
            "end": 128.75,
            "word": "shouldest",
            "start": 128.39,
            "probability": 0.68798828125
          },
          {
            "end": 128.93,
            "word": "not",
            "start": 128.75,
            "probability": 1
          },
          {
            "end": 129.09,
            "word": "have",
            "start": 128.93,
            "probability": 1
          },
          {
            "end": 129.37,
            "word": "looked",
            "start": 129.09,
            "probability": 1
          },
          {
            "end": 129.53,
            "word": "on",
            "start": 129.37,
            "probability": 0.99951171875
          },
          {
            "end": 129.63,
            "word": "the",
            "start": 129.53,
            "probability": 1
          },
          {
            "end": 129.87,
            "word": "day",
            "start": 129.63,
            "probability": 0.99951171875
          },
          {
            "end": 130.03,
            "word": "of",
            "start": 129.87,
            "probability": 1
          },
          {
            "end": 130.13,
            "word": "thy",
            "start": 130.03,
            "probability": 0.99853515625
          },
          {
            "end": 130.55,
            "word": "brother,",
            "start": 130.13,
            "probability": 0.99951171875
          },
          {
            "end": 130.91,
            "word": "in",
            "start": 130.67,
            "probability": 0.86279296875
          },
          {
            "end": 131.03,
            "word": "the",
            "start": 130.91,
            "probability": 1
          },
          {
            "end": 131.35,
            "word": "day",
            "start": 131.03,
            "probability": 1
          },
          {
            "end": 131.51,
            "word": "that",
            "start": 131.35,
            "probability": 1
          },
          {
            "end": 131.61,
            "word": "he",
            "start": 131.51,
            "probability": 1
          },
          {
            "end": 131.99,
            "word": "became",
            "start": 131.61,
            "probability": 1
          },
          {
            "end": 132.15,
            "word": "a",
            "start": 131.99,
            "probability": 0.99609375
          },
          {
            "end": 132.57,
            "word": "stranger.",
            "start": 132.15,
            "probability": 0.9990234375
          },
          {
            "end": 133.35,
            "word": "Neither",
            "start": 133.11,
            "probability": 0.998046875
          },
          {
            "end": 133.83,
            "word": "shouldest",
            "start": 133.35,
            "probability": 0.995849609375
          },
          {
            "end": 133.99,
            "word": "thou",
            "start": 133.83,
            "probability": 1
          },
          {
            "end": 134.17,
            "word": "have",
            "start": 133.99,
            "probability": 1
          },
          {
            "end": 134.81,
            "word": "rejoiced",
            "start": 134.17,
            "probability": 1
          },
          {
            "end": 135.25,
            "word": "over",
            "start": 134.81,
            "probability": 0.9716796875
          },
          {
            "end": 135.41,
            "word": "the",
            "start": 135.25,
            "probability": 1
          },
          {
            "end": 135.71,
            "word": "children",
            "start": 135.41,
            "probability": 0.9990234375
          },
          {
            "end": 135.95,
            "word": "of",
            "start": 135.71,
            "probability": 1
          },
          {
            "end": 136.25,
            "word": "Judah",
            "start": 135.95,
            "probability": 0.99951171875
          },
          {
            "end": 136.45,
            "word": "in",
            "start": 136.25,
            "probability": 0.94873046875
          },
          {
            "end": 136.53,
            "word": "the",
            "start": 136.45,
            "probability": 1
          },
          {
            "end": 136.83,
            "word": "day",
            "start": 136.53,
            "probability": 0.99951171875
          },
          {
            "end": 136.91,
            "word": "of",
            "start": 136.83,
            "probability": 1
          },
          {
            "end": 137.05,
            "word": "their",
            "start": 136.91,
            "probability": 0.9990234375
          },
          {
            "end": 137.49,
            "word": "destruction.",
            "start": 137.05,
            "probability": 0.99951171875
          },
          {
            "end": 138.35,
            "word": "Neither",
            "start": 137.91,
            "probability": 0.99951171875
          },
          {
            "end": 138.85,
            "word": "shouldest",
            "start": 138.35,
            "probability": 0.999755859375
          },
          {
            "end": 138.99,
            "word": "thou",
            "start": 138.85,
            "probability": 1
          },
          {
            "end": 139.13,
            "word": "have",
            "start": 138.99,
            "probability": 1
          },
          {
            "end": 139.43,
            "word": "spoken",
            "start": 139.13,
            "probability": 1
          },
          {
            "end": 140.03,
            "word": "proudly",
            "start": 139.43,
            "probability": 0.99951171875
          },
          {
            "end": 140.47,
            "word": "in",
            "start": 140.03,
            "probability": 1
          },
          {
            "end": 140.55,
            "word": "the",
            "start": 140.47,
            "probability": 1
          },
          {
            "end": 140.83,
            "word": "day",
            "start": 140.55,
            "probability": 1
          },
          {
            "end": 140.97,
            "word": "of",
            "start": 140.83,
            "probability": 1
          },
          {
            "end": 141.21,
            "word": "distress.",
            "start": 140.97,
            "probability": 0.99951171875
          },
          {
            "end": 142.87,
            "word": "Thou",
            "start": 142.39,
            "probability": 0.9990234375
          },
          {
            "end": 143.21,
            "word": "shouldest",
            "start": 142.87,
            "probability": 0.999755859375
          },
          {
            "end": 143.37,
            "word": "not",
            "start": 143.21,
            "probability": 1
          },
          {
            "end": 143.49,
            "word": "have",
            "start": 143.37,
            "probability": 1
          },
          {
            "end": 143.81,
            "word": "entered",
            "start": 143.49,
            "probability": 1
          },
          {
            "end": 144.05,
            "word": "into",
            "start": 143.81,
            "probability": 1
          },
          {
            "end": 144.23,
            "word": "the",
            "start": 144.05,
            "probability": 1
          },
          {
            "end": 144.47,
            "word": "gate",
            "start": 144.23,
            "probability": 0.998046875
          },
          {
            "end": 144.59,
            "word": "of",
            "start": 144.47,
            "probability": 1
          },
          {
            "end": 144.73,
            "word": "my",
            "start": 144.59,
            "probability": 0.9990234375
          },
          {
            "end": 145.15,
            "word": "people,",
            "start": 144.73,
            "probability": 1
          },
          {
            "end": 145.51,
            "word": "in",
            "start": 145.25,
            "probability": 0.99169921875
          },
          {
            "end": 145.63,
            "word": "the",
            "start": 145.51,
            "probability": 1
          },
          {
            "end": 145.89,
            "word": "day",
            "start": 145.63,
            "probability": 1
          },
          {
            "end": 146.01,
            "word": "of",
            "start": 145.89,
            "probability": 1
          },
          {
            "end": 146.17,
            "word": "their",
            "start": 146.01,
            "probability": 1
          },
          {
            "end": 146.77,
            "word": "calamity.",
            "start": 146.17,
            "probability": 0.99951171875
          },
          {
            "end": 147.27,
            "word": "Yea,",
            "start": 146.97,
            "probability": 0.99169921875
          },
          {
            "end": 147.65,
            "word": "thou",
            "start": 147.41,
            "probability": 1
          },
          {
            "end": 148.03,
            "word": "shouldest",
            "start": 147.65,
            "probability": 1
          },
          {
            "end": 148.19,
            "word": "not",
            "start": 148.03,
            "probability": 1
          },
          {
            "end": 148.35,
            "word": "have",
            "start": 148.19,
            "probability": 1
          },
          {
            "end": 148.61,
            "word": "looked",
            "start": 148.35,
            "probability": 1
          },
          {
            "end": 148.77,
            "word": "on",
            "start": 148.61,
            "probability": 1
          },
          {
            "end": 148.91,
            "word": "their",
            "start": 148.77,
            "probability": 1
          },
          {
            "end": 149.47,
            "word": "affliction,",
            "start": 148.91,
            "probability": 0.9986979166666666
          },
          {
            "end": 149.71,
            "word": "in",
            "start": 149.61,
            "probability": 0.73828125
          },
          {
            "end": 149.81,
            "word": "the",
            "start": 149.71,
            "probability": 0.99951171875
          },
          {
            "end": 150.07,
            "word": "day",
            "start": 149.81,
            "probability": 0.99951171875
          },
          {
            "end": 150.21,
            "word": "of",
            "start": 150.07,
            "probability": 1
          },
          {
            "end": 150.37,
            "word": "their",
            "start": 150.21,
            "probability": 0.9990234375
          },
          {
            "end": 150.97,
            "word": "calamity,",
            "start": 150.37,
            "probability": 1
          },
          {
            "end": 151.43,
            "word": "nor",
            "start": 151.05,
            "probability": 0.9970703125
          },
          {
            "end": 151.59,
            "word": "have",
            "start": 151.43,
            "probability": 0.982421875
          },
          {
            "end": 151.79,
            "word": "laid",
            "start": 151.59,
            "probability": 0.99951171875
          },
          {
            "end": 152.11,
            "word": "hands",
            "start": 151.79,
            "probability": 1
          },
          {
            "end": 152.27,
            "word": "on",
            "start": 152.11,
            "probability": 0.99951171875
          },
          {
            "end": 152.39,
            "word": "their",
            "start": 152.27,
            "probability": 1
          },
          {
            "end": 152.87,
            "word": "substance,",
            "start": 152.39,
            "probability": 1
          },
          {
            "end": 153.23,
            "word": "in",
            "start": 152.93,
            "probability": 0.982421875
          },
          {
            "end": 153.35,
            "word": "the",
            "start": 153.23,
            "probability": 1
          },
          {
            "end": 153.59,
            "word": "day",
            "start": 153.35,
            "probability": 1
          },
          {
            "end": 153.75,
            "word": "of",
            "start": 153.59,
            "probability": 1
          },
          {
            "end": 153.87,
            "word": "their",
            "start": 153.75,
            "probability": 0.99951171875
          },
          {
            "end": 154.45,
            "word": "calamity.",
            "start": 153.87,
            "probability": 1
          },
          {
            "end": 155.09,
            "word": "Neither",
            "start": 154.63,
            "probability": 0.98828125
          },
          {
            "end": 155.55,
            "word": "shouldest",
            "start": 155.09,
            "probability": 0.684814453125
          },
          {
            "end": 155.71,
            "word": "thou",
            "start": 155.55,
            "probability": 0.9873046875
          },
          {
            "end": 155.89,
            "word": "have",
            "start": 155.71,
            "probability": 0.98779296875
          },
          {
            "end": 156.17,
            "word": "stood",
            "start": 155.89,
            "probability": 0.99951171875
          },
          {
            "end": 156.37,
            "word": "in",
            "start": 156.17,
            "probability": 0.96728515625
          },
          {
            "end": 156.45,
            "word": "the",
            "start": 156.37,
            "probability": 1
          },
          {
            "end": 157.09,
            "word": "crossway,",
            "start": 156.45,
            "probability": 0.9736328125
          },
          {
            "end": 157.47,
            "word": "to",
            "start": 157.17,
            "probability": 0.99951171875
          },
          {
            "end": 157.67,
            "word": "cut",
            "start": 157.47,
            "probability": 1
          },
          {
            "end": 157.91,
            "word": "off",
            "start": 157.67,
            "probability": 1
          },
          {
            "end": 158.21,
            "word": "those",
            "start": 157.91,
            "probability": 1
          },
          {
            "end": 158.49,
            "word": "of",
            "start": 158.21,
            "probability": 1
          },
          {
            "end": 158.63,
            "word": "his",
            "start": 158.49,
            "probability": 0.96826171875
          },
          {
            "end": 158.89,
            "word": "that",
            "start": 158.63,
            "probability": 0.95458984375
          },
          {
            "end": 159.07,
            "word": "did",
            "start": 158.89,
            "probability": 1
          },
          {
            "end": 159.43,
            "word": "escape.",
            "start": 159.07,
            "probability": 1
          },
          {
            "end": 160.33,
            "word": "Neither",
            "start": 159.81,
            "probability": 0.99951171875
          },
          {
            "end": 160.85,
            "word": "shouldest",
            "start": 160.33,
            "probability": 0.999755859375
          },
          {
            "end": 161.03,
            "word": "thou",
            "start": 160.85,
            "probability": 1
          },
          {
            "end": 161.23,
            "word": "have",
            "start": 161.03,
            "probability": 1
          },
          {
            "end": 161.55,
            "word": "delivered",
            "start": 161.23,
            "probability": 1
          },
          {
            "end": 161.89,
            "word": "up",
            "start": 161.55,
            "probability": 1
          },
          {
            "end": 162.23,
            "word": "those",
            "start": 161.89,
            "probability": 0.904296875
          },
          {
            "end": 162.47,
            "word": "of",
            "start": 162.23,
            "probability": 1
          },
          {
            "end": 162.67,
            "word": "his",
            "start": 162.47,
            "probability": 1
          },
          {
            "end": 163.03,
            "word": "that",
            "start": 162.67,
            "probability": 0.07159423828125
          },
          {
            "end": 163.21,
            "word": "did",
            "start": 163.03,
            "probability": 1
          },
          {
            "end": 163.43,
            "word": "remain",
            "start": 163.21,
            "probability": 1
          },
          {
            "end": 163.87,
            "word": "in",
            "start": 163.43,
            "probability": 0.99267578125
          },
          {
            "end": 163.95,
            "word": "the",
            "start": 163.87,
            "probability": 1
          },
          {
            "end": 164.19,
            "word": "day",
            "start": 163.95,
            "probability": 1
          },
          {
            "end": 164.35,
            "word": "of",
            "start": 164.19,
            "probability": 1
          },
          {
            "end": 164.61,
            "word": "distress.",
            "start": 164.35,
            "probability": 1
          },
          {
            "end": 165.95,
            "word": "For",
            "start": 165.43,
            "probability": 0.99951171875
          },
          {
            "end": 166.07,
            "word": "the",
            "start": 165.95,
            "probability": 1
          },
          {
            "end": 166.31,
            "word": "day",
            "start": 166.07,
            "probability": 1
          },
          {
            "end": 166.43,
            "word": "of",
            "start": 166.31,
            "probability": 1
          },
          {
            "end": 166.53,
            "word": "the",
            "start": 166.43,
            "probability": 1
          },
          {
            "end": 166.83,
            "word": "Lord",
            "start": 166.53,
            "probability": 0.99462890625
          },
          {
            "end": 167.17,
            "word": "is",
            "start": 166.83,
            "probability": 0.9912109375
          },
          {
            "end": 167.45,
            "word": "near",
            "start": 167.17,
            "probability": 1
          },
          {
            "end": 167.75,
            "word": "upon",
            "start": 167.45,
            "probability": 0.998046875
          },
          {
            "end": 168.13,
            "word": "all",
            "start": 167.75,
            "probability": 1
          },
          {
            "end": 168.35,
            "word": "the",
            "start": 168.13,
            "probability": 1
          },
          {
            "end": 168.83,
            "word": "heathen.",
            "start": 168.35,
            "probability": 0.9998372395833334
          },
          {
            "end": 169.41,
            "word": "As",
            "start": 168.89,
            "probability": 0.99951171875
          },
          {
            "end": 169.65,
            "word": "thou",
            "start": 169.41,
            "probability": 1
          },
          {
            "end": 169.97,
            "word": "hast",
            "start": 169.65,
            "probability": 0.76611328125
          },
          {
            "end": 170.35,
            "word": "done,",
            "start": 169.97,
            "probability": 1
          },
          {
            "end": 170.87,
            "word": "it",
            "start": 170.45,
            "probability": 0.845703125
          },
          {
            "end": 171.09,
            "word": "shall",
            "start": 170.87,
            "probability": 1
          },
          {
            "end": 171.23,
            "word": "be",
            "start": 171.09,
            "probability": 1
          },
          {
            "end": 171.49,
            "word": "done",
            "start": 171.23,
            "probability": 1
          },
          {
            "end": 171.73,
            "word": "unto",
            "start": 171.49,
            "probability": 1
          },
          {
            "end": 172.01,
            "word": "thee.",
            "start": 171.73,
            "probability": 1
          },
          {
            "end": 172.81,
            "word": "Thy",
            "start": 172.29,
            "probability": 0.998046875
          },
          {
            "end": 173.31,
            "word": "reward",
            "start": 172.81,
            "probability": 1
          },
          {
            "end": 173.93,
            "word": "shall",
            "start": 173.31,
            "probability": 0.99951171875
          },
          {
            "end": 174.29,
            "word": "return",
            "start": 173.93,
            "probability": 1
          },
          {
            "end": 174.67,
            "word": "upon",
            "start": 174.29,
            "probability": 1
          },
          {
            "end": 175.41,
            "word": "thine",
            "start": 174.67,
            "probability": 0.999267578125
          },
          {
            "end": 175.59,
            "word": "own",
            "start": 175.41,
            "probability": 1
          },
          {
            "end": 175.91,
            "word": "head.",
            "start": 175.59,
            "probability": 1
          },
          {
            "end": 176.95,
            "word": "For",
            "start": 176.43,
            "probability": 1
          },
          {
            "end": 177.15,
            "word": "as",
            "start": 176.95,
            "probability": 0.99951171875
          },
          {
            "end": 177.29,
            "word": "ye",
            "start": 177.15,
            "probability": 0.98583984375
          },
          {
            "end": 177.47,
            "word": "have",
            "start": 177.29,
            "probability": 0.99853515625
          },
          {
            "end": 177.73,
            "word": "struck",
            "start": 177.47,
            "probability": 0.5732421875
          },
          {
            "end": 178.05,
            "word": "upon",
            "start": 177.73,
            "probability": 1
          },
          {
            "end": 178.37,
            "word": "my",
            "start": 178.05,
            "probability": 0.9990234375
          },
          {
            "end": 178.63,
            "word": "holy",
            "start": 178.37,
            "probability": 1
          },
          {
            "end": 179.11,
            "word": "mountain,",
            "start": 178.63,
            "probability": 1
          },
          {
            "end": 179.75,
            "word": "so",
            "start": 179.61,
            "probability": 0.439453125
          },
          {
            "end": 180.01,
            "word": "shall",
            "start": 179.75,
            "probability": 0.99951171875
          },
          {
            "end": 180.25,
            "word": "all",
            "start": 180.01,
            "probability": 1
          },
          {
            "end": 180.43,
            "word": "the",
            "start": 180.25,
            "probability": 0.99951171875
          },
          {
            "end": 180.83,
            "word": "heathen",
            "start": 180.43,
            "probability": 0.9991861979166666
          },
          {
            "end": 180.97,
            "word": "drink",
            "start": 180.83,
            "probability": 0.9990234375
          },
          {
            "end": 181.59,
            "word": "continually.",
            "start": 180.97,
            "probability": 1
          },
          {
            "end": 182.37,
            "word": "Yea,",
            "start": 181.95,
            "probability": 0.9970703125
          },
          {
            "end": 182.63,
            "word": "they",
            "start": 182.47,
            "probability": 1
          },
          {
            "end": 182.83,
            "word": "shall",
            "start": 182.63,
            "probability": 1
          },
          {
            "end": 183.25,
            "word": "drink,",
            "start": 182.83,
            "probability": 1
          },
          {
            "end": 183.41,
            "word": "and",
            "start": 183.25,
            "probability": 1
          },
          {
            "end": 183.47,
            "word": "they",
            "start": 183.41,
            "probability": 0.99951171875
          },
          {
            "end": 183.67,
            "word": "shall",
            "start": 183.47,
            "probability": 1
          },
          {
            "end": 184.07,
            "word": "swallow",
            "start": 183.67,
            "probability": 0.99951171875
          },
          {
            "end": 184.43,
            "word": "down,",
            "start": 184.07,
            "probability": 1
          },
          {
            "end": 185.11,
            "word": "and",
            "start": 184.69,
            "probability": 0.9990234375
          },
          {
            "end": 185.21,
            "word": "they",
            "start": 185.11,
            "probability": 1
          },
          {
            "end": 185.39,
            "word": "shall",
            "start": 185.21,
            "probability": 1
          },
          {
            "end": 185.55,
            "word": "be",
            "start": 185.39,
            "probability": 1
          },
          {
            "end": 185.73,
            "word": "as",
            "start": 185.55,
            "probability": 1
          },
          {
            "end": 185.95,
            "word": "though",
            "start": 185.73,
            "probability": 1
          },
          {
            "end": 186.65,
            "word": "they",
            "start": 185.95,
            "probability": 0.9990234375
          },
          {
            "end": 186.79,
            "word": "had",
            "start": 186.65,
            "probability": 1
          },
          {
            "end": 187.03,
            "word": "not",
            "start": 186.79,
            "probability": 1
          },
          {
            "end": 187.39,
            "word": "been.",
            "start": 187.03,
            "probability": 1
          },
          {
            "end": 189.09,
            "word": "But",
            "start": 188.49,
            "probability": 0.99853515625
          },
          {
            "end": 189.37,
            "word": "upon",
            "start": 189.09,
            "probability": 1
          },
          {
            "end": 189.85,
            "word": "Mount",
            "start": 189.37,
            "probability": 0.9765625
          },
          {
            "end": 190.19,
            "word": "Zion",
            "start": 189.85,
            "probability": 0.99951171875
          },
          {
            "end": 190.73,
            "word": "shall",
            "start": 190.19,
            "probability": 1
          },
          {
            "end": 190.93,
            "word": "be",
            "start": 190.73,
            "probability": 1
          },
          {
            "end": 191.75,
            "word": "deliverance,",
            "start": 190.93,
            "probability": 0.999755859375
          },
          {
            "end": 192.25,
            "word": "and",
            "start": 191.81,
            "probability": 1
          },
          {
            "end": 192.53,
            "word": "there",
            "start": 192.25,
            "probability": 1
          },
          {
            "end": 192.97,
            "word": "shall",
            "start": 192.53,
            "probability": 1
          },
          {
            "end": 193.15,
            "word": "be",
            "start": 192.97,
            "probability": 1
          },
          {
            "end": 193.53,
            "word": "holiness.",
            "start": 193.15,
            "probability": 1
          },
          {
            "end": 194.41,
            "word": "And",
            "start": 193.89,
            "probability": 0.99951171875
          },
          {
            "end": 194.53,
            "word": "the",
            "start": 194.41,
            "probability": 1
          },
          {
            "end": 194.85,
            "word": "house",
            "start": 194.53,
            "probability": 1
          },
          {
            "end": 195.03,
            "word": "of",
            "start": 194.85,
            "probability": 1
          },
          {
            "end": 195.39,
            "word": "Jacob",
            "start": 195.03,
            "probability": 1
          },
          {
            "end": 196.05,
            "word": "shall",
            "start": 195.39,
            "probability": 0.99951171875
          },
          {
            "end": 196.43,
            "word": "possess",
            "start": 196.05,
            "probability": 0.9990234375
          },
          {
            "end": 197.31,
            "word": "their",
            "start": 196.43,
            "probability": 0.998046875
          },
          {
            "end": 197.75,
            "word": "possessions.",
            "start": 197.31,
            "probability": 1
          },
          {
            "end": 199.5,
            "word": "And",
            "start": 198.9,
            "probability": 1
          },
          {
            "end": 199.62,
            "word": "the",
            "start": 199.5,
            "probability": 1
          },
          {
            "end": 199.9,
            "word": "house",
            "start": 199.62,
            "probability": 1
          },
          {
            "end": 200.16,
            "word": "of",
            "start": 199.9,
            "probability": 1
          },
          {
            "end": 200.5,
            "word": "Jacob",
            "start": 200.16,
            "probability": 1
          },
          {
            "end": 201.02,
            "word": "shall",
            "start": 200.5,
            "probability": 1
          },
          {
            "end": 201.24,
            "word": "be",
            "start": 201.02,
            "probability": 1
          },
          {
            "end": 201.36,
            "word": "a",
            "start": 201.24,
            "probability": 0.8896484375
          },
          {
            "end": 201.74,
            "word": "fire,",
            "start": 201.36,
            "probability": 0.99951171875
          },
          {
            "end": 202.38,
            "word": "and",
            "start": 201.9,
            "probability": 1
          },
          {
            "end": 202.5,
            "word": "the",
            "start": 202.38,
            "probability": 1
          },
          {
            "end": 202.76,
            "word": "house",
            "start": 202.5,
            "probability": 1
          },
          {
            "end": 202.98,
            "word": "of",
            "start": 202.76,
            "probability": 1
          },
          {
            "end": 203.42,
            "word": "Joseph",
            "start": 202.98,
            "probability": 0.99853515625
          },
          {
            "end": 203.64,
            "word": "a",
            "start": 203.42,
            "probability": 0.99853515625
          },
          {
            "end": 203.98,
            "word": "flame,",
            "start": 203.64,
            "probability": 1
          },
          {
            "end": 204.72,
            "word": "and",
            "start": 204.2,
            "probability": 1
          },
          {
            "end": 204.82,
            "word": "the",
            "start": 204.72,
            "probability": 1
          },
          {
            "end": 205.12,
            "word": "house",
            "start": 204.82,
            "probability": 1
          },
          {
            "end": 205.34,
            "word": "of",
            "start": 205.12,
            "probability": 1
          },
          {
            "end": 205.8,
            "word": "Esau",
            "start": 205.34,
            "probability": 0.99951171875
          },
          {
            "end": 206.26,
            "word": "for",
            "start": 205.8,
            "probability": 0.9912109375
          },
          {
            "end": 206.8,
            "word": "stubble.",
            "start": 206.26,
            "probability": 0.99755859375
          },
          {
            "end": 207.42,
            "word": "And",
            "start": 206.9,
            "probability": 1
          },
          {
            "end": 207.52,
            "word": "they",
            "start": 207.42,
            "probability": 1
          },
          {
            "end": 207.72,
            "word": "shall",
            "start": 207.52,
            "probability": 1
          },
          {
            "end": 208.08,
            "word": "kindle",
            "start": 207.72,
            "probability": 0.998779296875
          },
          {
            "end": 208.22,
            "word": "in",
            "start": 208.08,
            "probability": 0.990234375
          },
          {
            "end": 208.54,
            "word": "them,",
            "start": 208.22,
            "probability": 1
          },
          {
            "end": 209.16,
            "word": "and",
            "start": 208.68,
            "probability": 1
          },
          {
            "end": 209.52,
            "word": "devour",
            "start": 209.16,
            "probability": 0.999755859375
          },
          {
            "end": 209.84,
            "word": "them,",
            "start": 209.52,
            "probability": 1
          },
          {
            "end": 210.5,
            "word": "and",
            "start": 210.38,
            "probability": 0.32763671875
          },
          {
            "end": 210.58,
            "word": "there",
            "start": 210.5,
            "probability": 0.98974609375
          },
          {
            "end": 210.74,
            "word": "shall",
            "start": 210.58,
            "probability": 0.99951171875
          },
          {
            "end": 210.96,
            "word": "not",
            "start": 210.74,
            "probability": 0.99951171875
          },
          {
            "end": 211.1,
            "word": "be",
            "start": 210.96,
            "probability": 1
          },
          {
            "end": 211.38,
            "word": "any",
            "start": 211.1,
            "probability": 1
          },
          {
            "end": 211.94,
            "word": "remaining",
            "start": 211.38,
            "probability": 0.99951171875
          },
          {
            "end": 212.18,
            "word": "of",
            "start": 211.94,
            "probability": 0.99951171875
          },
          {
            "end": 212.26,
            "word": "the",
            "start": 212.18,
            "probability": 1
          },
          {
            "end": 212.52,
            "word": "house",
            "start": 212.26,
            "probability": 0.99951171875
          },
          {
            "end": 212.72,
            "word": "of",
            "start": 212.52,
            "probability": 1
          },
          {
            "end": 213.1,
            "word": "Esau.",
            "start": 212.72,
            "probability": 0.99951171875
          },
          {
            "end": 214.1,
            "word": "For",
            "start": 213.82,
            "probability": 0.9951171875
          },
          {
            "end": 214.26,
            "word": "the",
            "start": 214.1,
            "probability": 0.99951171875
          },
          {
            "end": 214.58,
            "word": "Lord",
            "start": 214.26,
            "probability": 0.95703125
          },
          {
            "end": 215.22,
            "word": "hath",
            "start": 214.58,
            "probability": 0.99365234375
          },
          {
            "end": 215.54,
            "word": "spoken",
            "start": 215.22,
            "probability": 1
          },
          {
            "end": 215.86,
            "word": "it.",
            "start": 215.54,
            "probability": 1
          },
          {
            "end": 217.32,
            "word": "And",
            "start": 216.76,
            "probability": 0.99462890625
          },
          {
            "end": 217.46,
            "word": "they",
            "start": 217.32,
            "probability": 0.99951171875
          },
          {
            "end": 217.58,
            "word": "of",
            "start": 217.46,
            "probability": 1
          },
          {
            "end": 217.7,
            "word": "the",
            "start": 217.58,
            "probability": 1
          },
          {
            "end": 218.14,
            "word": "south",
            "start": 217.7,
            "probability": 0.9853515625
          },
          {
            "end": 218.46,
            "word": "shall",
            "start": 218.14,
            "probability": 0.99560546875
          },
          {
            "end": 218.72,
            "word": "possess",
            "start": 218.46,
            "probability": 0.9990234375
          },
          {
            "end": 219.1,
            "word": "the",
            "start": 218.72,
            "probability": 1
          },
          {
            "end": 219.3,
            "word": "mount",
            "start": 219.1,
            "probability": 0.9814453125
          },
          {
            "end": 219.48,
            "word": "of",
            "start": 219.3,
            "probability": 1
          },
          {
            "end": 219.88,
            "word": "Esau,",
            "start": 219.48,
            "probability": 1
          },
          {
            "end": 220.56,
            "word": "and",
            "start": 220.06,
            "probability": 0.9990234375
          },
          {
            "end": 220.7,
            "word": "they",
            "start": 220.56,
            "probability": 1
          },
          {
            "end": 220.84,
            "word": "of",
            "start": 220.7,
            "probability": 1
          },
          {
            "end": 220.98,
            "word": "the",
            "start": 220.84,
            "probability": 1
          },
          {
            "end": 221.28,
            "word": "plain",
            "start": 220.98,
            "probability": 0.998046875
          },
          {
            "end": 221.68,
            "word": "the",
            "start": 221.28,
            "probability": 0.68896484375
          },
          {
            "end": 222.46,
            "word": "Philistines,",
            "start": 221.68,
            "probability": 0.9998372395833334
          },
          {
            "end": 223.06,
            "word": "and",
            "start": 222.6,
            "probability": 0.99951171875
          },
          {
            "end": 223.2,
            "word": "they",
            "start": 223.06,
            "probability": 1
          },
          {
            "end": 223.34,
            "word": "shall",
            "start": 223.2,
            "probability": 1
          },
          {
            "end": 223.6,
            "word": "possess",
            "start": 223.34,
            "probability": 0.99951171875
          },
          {
            "end": 223.94,
            "word": "the",
            "start": 223.6,
            "probability": 1
          },
          {
            "end": 224.22,
            "word": "fields",
            "start": 223.94,
            "probability": 0.99951171875
          },
          {
            "end": 224.4,
            "word": "of",
            "start": 224.22,
            "probability": 1
          },
          {
            "end": 224.98,
            "word": "Ephraim,",
            "start": 224.4,
            "probability": 0.9998372395833334
          },
          {
            "end": 225.34,
            "word": "and",
            "start": 224.98,
            "probability": 0.99951171875
          },
          {
            "end": 225.46,
            "word": "the",
            "start": 225.34,
            "probability": 1
          },
          {
            "end": 225.78,
            "word": "fields",
            "start": 225.46,
            "probability": 1
          },
          {
            "end": 225.96,
            "word": "of",
            "start": 225.78,
            "probability": 1
          },
          {
            "end": 226.46,
            "word": "Samaria,",
            "start": 225.96,
            "probability": 1
          },
          {
            "end": 227.28,
            "word": "and",
            "start": 227,
            "probability": 1
          },
          {
            "end": 227.66,
            "word": "Benjamin",
            "start": 227.28,
            "probability": 0.99267578125
          },
          {
            "end": 228.04,
            "word": "shall",
            "start": 227.66,
            "probability": 0.99951171875
          },
          {
            "end": 228.32,
            "word": "possess",
            "start": 228.04,
            "probability": 1
          },
          {
            "end": 229.4,
            "word": "Gilead.",
            "start": 228.32,
            "probability": 0.9998372395833334
          },
          {
            "end": 230.18,
            "word": "And",
            "start": 229.9,
            "probability": 0.98974609375
          },
          {
            "end": 230.3,
            "word": "the",
            "start": 230.18,
            "probability": 1
          },
          {
            "end": 230.66,
            "word": "captivity",
            "start": 230.3,
            "probability": 0.99951171875
          },
          {
            "end": 231,
            "word": "of",
            "start": 230.66,
            "probability": 1
          },
          {
            "end": 231.2,
            "word": "this",
            "start": 231,
            "probability": 1
          },
          {
            "end": 231.54,
            "word": "host",
            "start": 231.2,
            "probability": 0.99951171875
          },
          {
            "end": 231.86,
            "word": "of",
            "start": 231.54,
            "probability": 0.79296875
          },
          {
            "end": 232,
            "word": "the",
            "start": 231.86,
            "probability": 1
          },
          {
            "end": 232.26,
            "word": "children",
            "start": 232,
            "probability": 0.99951171875
          },
          {
            "end": 232.48,
            "word": "of",
            "start": 232.26,
            "probability": 1
          },
          {
            "end": 232.86,
            "word": "Israel",
            "start": 232.48,
            "probability": 1
          },
          {
            "end": 233.44,
            "word": "shall",
            "start": 232.86,
            "probability": 0.9560546875
          },
          {
            "end": 233.7,
            "word": "possess",
            "start": 233.44,
            "probability": 0.99951171875
          },
          {
            "end": 234.1,
            "word": "that",
            "start": 233.7,
            "probability": 1
          },
          {
            "end": 234.42,
            "word": "of",
            "start": 234.1,
            "probability": 1
          },
          {
            "end": 234.56,
            "word": "the",
            "start": 234.42,
            "probability": 1
          },
          {
            "end": 235.28,
            "word": "Canaanites,",
            "start": 234.56,
            "probability": 0.9998372395833334
          },
          {
            "end": 235.74,
            "word": "even",
            "start": 235.32,
            "probability": 0.99951171875
          },
          {
            "end": 236,
            "word": "unto",
            "start": 235.74,
            "probability": 0.99951171875
          },
          {
            "end": 236.7,
            "word": "Zarephath.",
            "start": 236,
            "probability": 0.9931640625
          },
          {
            "end": 237.44,
            "word": "And",
            "start": 237,
            "probability": 1
          },
          {
            "end": 237.54,
            "word": "the",
            "start": 237.44,
            "probability": 1
          },
          {
            "end": 237.92,
            "word": "captivity",
            "start": 237.54,
            "probability": 0.99951171875
          },
          {
            "end": 238.22,
            "word": "of",
            "start": 237.92,
            "probability": 1
          },
          {
            "end": 238.5,
            "word": "Jerusalem,",
            "start": 238.22,
            "probability": 1
          },
          {
            "end": 239.28,
            "word": "which",
            "start": 238.78,
            "probability": 1
          },
          {
            "end": 239.42,
            "word": "is",
            "start": 239.28,
            "probability": 0.99951171875
          },
          {
            "end": 239.58,
            "word": "in",
            "start": 239.42,
            "probability": 0.9150390625
          },
          {
            "end": 240.16,
            "word": "Zepharad,",
            "start": 239.58,
            "probability": 0.7799072265625
          },
          {
            "end": 240.58,
            "word": "shall",
            "start": 240.16,
            "probability": 0.52197265625
          },
          {
            "end": 240.94,
            "word": "possess",
            "start": 240.58,
            "probability": 0.9853515625
          },
          {
            "end": 241.34,
            "word": "the",
            "start": 240.94,
            "probability": 0.99853515625
          },
          {
            "end": 241.72,
            "word": "cities",
            "start": 241.34,
            "probability": 0.9970703125
          },
          {
            "end": 241.88,
            "word": "of",
            "start": 241.72,
            "probability": 0.9990234375
          },
          {
            "end": 241.98,
            "word": "the",
            "start": 241.88,
            "probability": 0.99951171875
          },
          {
            "end": 242.34,
            "word": "south.",
            "start": 241.98,
            "probability": 0.8125
          },
          {
            "end": 243.28,
            "word": "And",
            "start": 242.93,
            "probability": 0.97412109375
          },
          {
            "end": 243.92,
            "word": "saviors",
            "start": 243.28,
            "probability": 0.9765625
          },
          {
            "end": 244.26,
            "word": "shall",
            "start": 243.92,
            "probability": 0.99853515625
          },
          {
            "end": 244.5,
            "word": "come",
            "start": 244.26,
            "probability": 0.99951171875
          },
          {
            "end": 244.72,
            "word": "up",
            "start": 244.5,
            "probability": 0.998046875
          },
          {
            "end": 244.86,
            "word": "on",
            "start": 244.72,
            "probability": 0.99853515625
          },
          {
            "end": 245.04,
            "word": "Mount",
            "start": 244.86,
            "probability": 0.97607421875
          },
          {
            "end": 245.34,
            "word": "Zion",
            "start": 245.04,
            "probability": 1
          },
          {
            "end": 245.88,
            "word": "to",
            "start": 245.34,
            "probability": 0.99267578125
          },
          {
            "end": 246.28,
            "word": "judge",
            "start": 245.88,
            "probability": 1
          },
          {
            "end": 246.64,
            "word": "the",
            "start": 246.28,
            "probability": 0.99951171875
          },
          {
            "end": 246.86,
            "word": "mount",
            "start": 246.64,
            "probability": 0.4873046875
          },
          {
            "end": 247.08,
            "word": "of",
            "start": 246.86,
            "probability": 0.998046875
          },
          {
            "end": 247.52,
            "word": "Esau,",
            "start": 247.08,
            "probability": 0.994384765625
          },
          {
            "end": 248.18,
            "word": "and",
            "start": 247.66,
            "probability": 0.99609375
          },
          {
            "end": 248.3,
            "word": "the",
            "start": 248.18,
            "probability": 0.9990234375
          },
          {
            "end": 248.6,
            "word": "kingdom",
            "start": 248.3,
            "probability": 0.99853515625
          },
          {
            "end": 249.26,
            "word": "shall",
            "start": 248.6,
            "probability": 0.99951171875
          },
          {
            "end": 249.48,
            "word": "be",
            "start": 249.26,
            "probability": 1
          },
          {
            "end": 249.64,
            "word": "the",
            "start": 249.48,
            "probability": 0.99951171875
          },
          {
            "end": 250.12,
            "word": "Lord's.",
            "start": 249.64,
            "probability": 0.986083984375
          },
          {
            "end": 252.21,
            "word": "The",
            "start": 251.86,
            "probability": 0.982421875
          },
          {
            "end": 252.65,
            "word": "end",
            "start": 252.21,
            "probability": 0.876953125
          },
          {
            "end": 253.03,
            "word": "of",
            "start": 252.65,
            "probability": 0.9990234375
          },
          {
            "end": 253.81,
            "word": "Obadiah,",
            "start": 253.03,
            "probability": 0.9993489583333334
          },
          {
            "end": 254.43,
            "word": "King",
            "start": 253.81,
            "probability": 0.9970703125
          },
          {
            "end": 254.77,
            "word": "James",
            "start": 254.43,
            "probability": 1
          },
          {
            "end": 255.17,
            "word": "Version,",
            "start": 254.77,
            "probability": 0.9619140625
          },
          {
            "end": 256.21,
            "word": "read",
            "start": 255.51,
            "probability": 0.98193359375
          },
          {
            "end": 256.97,
            "word": "by",
            "start": 256.21,
            "probability": 0.90576171875
          },
          {
            "end": 257.37,
            "word": "Justin",
            "start": 256.97,
            "probability": 0.99853515625
          },
          {
            "end": 257.91,
            "word": "Bible.",
            "start": 257.37,
            "probability": 0.974609375
          },
          {
            "end": 258.79,
            "word": "May",
            "start": 258.44,
            "probability": 0.998046875
          },
          {
            "end": 258.99,
            "word": "God",
            "start": 258.79,
            "probability": 0.99951171875
          },
          {
            "end": 259.27,
            "word": "bless",
            "start": 258.99,
            "probability": 1
          },
          {
            "end": 259.53,
            "word": "you",
            "start": 259.27,
            "probability": 1
          },
          {
            "end": 260.11,
            "word": "with",
            "start": 259.53,
            "probability": 0.9990234375
          },
          {
            "end": 260.29,
            "word": "an",
            "start": 260.11,
            "probability": 0.9990234375
          },
          {
            "end": 261.03,
            "word": "unquenchable",
            "start": 260.29,
            "probability": 0.999755859375
          },
          {
            "end": 261.37,
            "word": "thirst",
            "start": 261.03,
            "probability": 1
          },
          {
            "end": 262.13,
            "word": "for",
            "start": 261.78,
            "probability": 0.99951171875
          },
          {
            "end": 262.29,
            "word": "his",
            "start": 262.13,
            "probability": 0.68896484375
          },
          {
            "end": 262.55,
            "word": "holy",
            "start": 262.29,
            "probability": 0.97802734375
          },
          {
            "end": 262.91,
            "word": "word,",
            "start": 262.55,
            "probability": 0.99853515625
          },
          {
            "end": 263.45,
            "word": "the",
            "start": 263.05,
            "probability": 0.99951171875
          },
          {
            "end": 263.77,
            "word": "Bible.",
            "start": 263.45,
            "probability": 0.99951171875
          }
        ],
        "speaker": "SPEAKER_01",
        "avg_logprob": -0.16728670351088992
      }
    ],
    "num_speakers": 2
  },
  "started_at": "2024-03-12T16:52:47.586139Z",
  "status": "succeeded",
  "urls": {
    "get": "https://api.replicate.com/v1/predictions/3bu5hm3b3zenvypmunr777hiom",
    "cancel": "https://api.replicate.com/v1/predictions/3bu5hm3b3zenvypmunr777hiom/cancel"
  },
  "version": "3ff22700b10e9c888e72235131e10c0a8427cd79e750bc42e4c035be2121796b"
}
"""

@app.post('/extract_words')
async def extract_words(text_query: TextQuery):
  # Validate request body
  if not text_query.text_query:
    raise HTTPException(status_code=400, detail="Missing text_query parameter")

  # Get data (replace with your actual data fetching logic)
  data = get_data()

  # Initialization
  start_time = None
  end_time = None

  # Loop through segments
  for segment in data['segments']:
    words = segment['words']
    for word in words:
      if word['word'] == text_query.text_query:
        if start_time is None:
          start_time = word['start']
        end_time = word['end']

  # Return result
  if start_time is None:
    return {"message": f"Text '{text_query.text_query}' not found"}
  else:
    return {"start": start_time, "end": end_time}
