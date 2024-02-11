# ROS Bag to MP3 Converter

Converts audio data from ROS bag files to MP3 format.

## Overview

This Python script extracts audio data from ROS bag files, specifically from messages of type `audio_common_msgs/AudioData`, and saves them into MP3 files. The script is designed to be a helpful tool for working with ROS bag files containing audio data.

## Features

- Extracts audio data from specified ROS bag file and topic.
- Converts the audio data to a valid MP3 file.
- Simple and easy to use.

## Requirements

- Python 3
- ROS (Robot Operating System)
- `rosbag` Python package

## Usage

```bash
python rosbag_to_mp3.py -source <bag_file_path> -topic <audio_topic_name> -output <output_mp3_file_path>
