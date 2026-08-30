import cv2
import os

video_path = "portfolio_animation.mp4"
output_dir = "frames"

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"Video: {width}x{height} @ {fps}fps")
print(f"Total frames: {total_frames}")
print(f"Duration: {total_frames/fps:.2f}s")
print(f"Extracting all {total_frames} frames...")

frame_idx = 0
extracted = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    output_path = os.path.join(output_dir, f"frame_{frame_idx:04d}.jpg")
    # Save as JPEG with quality 85 for good balance of quality vs file size
    cv2.imwrite(output_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
    
    frame_idx += 1
    extracted += 1
    
    if extracted % 24 == 0:
        print(f"  Progress: {extracted}/{total_frames} frames ({extracted/total_frames*100:.1f}%)")

cap.release()
print(f"\nDone! Extracted {extracted} frames to '{output_dir}/' folder")
print(f"Files: frame_0000.jpg to frame_{extracted-1:04d}.jpg")
