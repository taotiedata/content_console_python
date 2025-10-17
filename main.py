
import os
from tts_limited import text_to_speech
from match_duration import match_video_to_audio

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue...")

def menu():
    while True:
        clear_screen()
        print("=== 🧠 Taotie Sync & TTS (v1) ===")
        print("[1] (.txt) → (.mp3")
        print("[2] Match (.mp4) duration to (.mp3)")
        print("[0] Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            run_tts()
        elif choice == "2":
            run_video_match()
        elif choice == "0":
            print("👋 Exiting. Have a great day!")
            break
        else:
            print("❌ Invalid option.")
            pause()

def run_tts():
    clear_screen()
    print("--- TTS(1000W) ---")
    txt_files = os.listdir("input/txts")
    if not txt_files:
        print("No .txt in input/txts/")
        pause()
        return

    print("Available text files:")
    for i, f in enumerate(txt_files, 1):
        print(f"[{i}] {f}")

    try:
        idx = int(input("\nSelect file number: ").strip()) - 1
        filename = txt_files[idx]
        voice = input("Choose voice (default/female): ").strip().lower() or "default"
        text_to_speech(filename, voice)
    except (ValueError, IndexError):
        print(" Invalid selection.")
    pause()

def run_video_match():
    clear_screen()
    print("--- Match mp4 Duration to mp3 ---")

    mp4_files = os.listdir("input/mp4")
    mp3_files = os.listdir("input/mp3")

    if not mp4_files or not mp3_files:
        print("⚠️ Missing input files in /input/mp4 or /input/mp3.")
        pause()
        return

    print("Available videos:")
    for i, f in enumerate(mp4_files, 1):
        print(f"[{i}] {f}")
    try:
        video_idx = int(input("\nSelect video: ").strip()) - 1
        video_name = mp4_files[video_idx]
    except (ValueError, IndexError):
        print("❌ Invalid video selection.")
        pause()
        return

    print("\nAvailable audios:")
    for i, f in enumerate(mp3_files, 1):
        print(f"[{i}] {f}")
    try:
        audio_idx = int(input("\nSelect audio: ").strip()) - 1
        audio_name = mp3_files[audio_idx]
    except (ValueError, IndexError):
        print("❌ Invalid audio selection.")
        pause()
        return

    match_video_to_audio(video_name, audio_name)
    pause()

if __name__ == "__main__":
    menu()
