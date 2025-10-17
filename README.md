
# 🧠 Taotie Sync & TTS — Open Source v0

Simple python tool to get started on automated content creation!

## ⚙️ Folder Setup
```
/input/
├── /txts/   → text inputs
├── /mp3/    → imported audio (for matching)
├── /mp4/    → background videos

/output/
├── /mp3/    → generated TTS files
├── /mp4/    → final videos
└── logs.txt (optional)
```

## 🧩 Usage

### 1. Convert Text → MP3
```bash
python tts_limited.py
```

### 2. Match Video → Audio
```bash
python match_duration.py
```

### 3. Use the Interactive Menu
```bash
python main.py
```

## 💡 Example Workflow
1. Place `input/txts/sample.txt`.
2. Run `tts_limited.py` → outputs `output/mp3/sample.mp3`.
3. Place a video in `input/mp4/video.mp4`.
4. Run `match_duration.py` → outputs `output/mp4/matched_video.mp4`.

## 🪪 License
MIT License – Free to use, modify, and share.
