
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from pathlib import Path

def match_video_to_audio(video_name, audio_name):
    input_video = Path("input/mp4") / video_name
    input_audio = Path("input/mp3") / audio_name
    output_video = Path("output/mp4") / f"matched_{video_name}"

    if not input_video.exists() or not input_audio.exists():
        print("❌ Missing video or audio file in input folder.")
        return

    audio = AudioFileClip(str(input_audio))
    video = VideoFileClip(str(input_video)).without_audio()

    target_duration = audio.duration
    video_duration = video.duration

    print(f"🎬 Video duration: {video_duration:.2f}s | 🎧 Audio duration: {target_duration:.2f}s")

    if video_duration < target_duration:
        loops = int(target_duration // video_duration) + 1
        video = concatenate_videoclips([video] * loops)
        print(f"🔁 Video looped {loops} times to match duration.")
        video = video.subclip(0, target_duration)
    else:
        video = video.subclip(0, target_duration)
        print("✂️ Video trimmed to match audio length.")

    final = video.set_audio(audio)
    output_video.parent.mkdir(parents=True, exist_ok=True)
    final.write_videofile(str(output_video), codec="libx264", audio_codec="aac")

    print(f"✅ Exported: {output_video}")

if __name__ == "__main__":
    match_video_to_audio("video.mp4", "audio.mp3")
