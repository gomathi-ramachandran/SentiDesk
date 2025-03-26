import os
import shutil
import random

# Define source and destination folders
source_folder = r"C:\Users\Sri Devi\Downloads\customer_feedback_audio"  # Change to your actual source folder
main_audio_folder = "audio/"
train_folder = os.path.join(main_audio_folder, "train/")
test_folder = os.path.join(main_audio_folder, "test/")

# Ensure the destination folders exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Allowed audio formats
audio_extensions = (".wav", ".mp3")

# Get all audio files from the source folder
audio_files = [file for file in os.listdir(source_folder) if file.endswith(audio_extensions)]

if not audio_files:
    print("No audio files found in the source folder!")
else:
    # Shuffle the list for randomness
    random.shuffle(audio_files)

    # Split 80% train, 20% test
    split_ratio = 0.8
    split_index = int(len(audio_files) * split_ratio)

    train_files = audio_files[:split_index]  # First 80% for training
    test_files = audio_files[split_index:]  # Last 20% for testing

    # Move files to the respective folders
    for file in train_files:
        shutil.move(os.path.join(source_folder, file), os.path.join(train_folder, file))
        print(f"Moved to train: {file}")

    for file in test_files:
        shutil.move(os.path.join(source_folder, file), os.path.join(test_folder, file))
        print(f"Moved to test: {file}")

    print(f"\nSplit Complete! {len(train_files)} train files, {len(test_files)} test files.")
