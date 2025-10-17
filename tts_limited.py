
import pyttsx3
from pathlib import Path

def text_to_speech(txt_name, voice="default"):
    input_txt = Path("input/txts") / txt_name
    output_audio = Path("output/mp3") / f"{input_txt.stem}.mp3"

    if not input_txt.exists():
        print(f"❌ Text file not found: {input_txt}")
        return

    with open(input_txt, "r", encoding="utf-8") as f:
        text = f.read().strip()

    words = text.split()
    if len(words) > 1000:
        raise ValueError(f"⚠️ Input has {len(words)} words (max: 1000).")

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voice == "female" and len(voices) > 1:
        engine.setProperty('voice', voices[1].id)

    output_audio.parent.mkdir(parents=True, exist_ok=True)
    engine.save_to_file(text, str(output_audio))
    engine.runAndWait()

    print(f"✅ Audio created: {output_audio}")

if __name__ == "__main__":
    text_to_speech("sample.txt")
