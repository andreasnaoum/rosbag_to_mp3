import argparse
from ros import rosbag

def extract_audio(bag_path, topic_name, mp3_path):
    # Open the ROS bag file
    print('Opening bag')
    bag = rosbag.Bag(bag_path)

    # Open the MP3 file in binary write mode
    with open(mp3_path, 'wb') as mp3_file:
        print('Reading audio messages and saving to mp3 file')
        msg_count = 0

        # Iterate through messages in the specified topic
        for topic, msg, stamp in bag.read_messages(topics=[topic_name]):
            # Check if the message type is 'audio_common_msgs/AudioData'
            if msg._type == 'audio_common_msgs/AudioData':
                msg_count += 1
                # Write the audio data to the MP3 file
                mp3_file.write(bytes(msg.data))

    # Close the ROS bag file
    bag.close()
    # Print a summary message
    print('Done. %d audio messages written to %s' % (msg_count, mp3_path))

if __name__ == '__main__':
    # Set up the command line argument parser
    parser = argparse.ArgumentParser(description='Convert ROS audio bag file to MP3')
    parser.add_argument('-source', dest='bag_path', required=True, help='ROS bag file path')
    parser.add_argument('-topic', dest='topic_name', required=True, help='Audio topic name')
    parser.add_argument('-output', dest='mp3_path', required=True, help='Output MP3 file path')

    # Parse the command line arguments
    args = parser.parse_args()

    # Call the function to extract audio and save as MP3
    extract_audio(args.bag_path, args.topic_name, args.mp3_path)

