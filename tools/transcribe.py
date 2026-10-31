import glob, json, os, subprocess
from faster_whisper import WhisperModel
m = WhisperModel("small", device="cpu", compute_type="int8")
out = {}
for f in sorted(glob.glob("video/tiktok_best/*.mp4")):
    n = os.path.basename(f)[:-4]
    dur = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip()
    try:
        segs, info = m.transcribe(f, vad_filter=True)
        out[n] = {"duration": dur, "lang": info.language, "text": " ".join(s.text.strip() for s in segs)}
    except Exception as e:
        out[n] = {"duration": dur, "error": str(e)}
    print(n, out[n], flush=True)
    json.dump(out, open("video/tiktok_best/transcripts.json","w"), ensure_ascii=False, indent=1)
