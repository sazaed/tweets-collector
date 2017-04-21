import json
import argparse
import os

parser = argparse.ArgumentParser(description='extract tweet texts from json')
parser.add_argument('-i', '--json-dir', type=str,
help='tweets json directory', required=True)
parser.add_argument('-o', '--out-dir', type=str,
help='the output directory.', required=True)


def extract_tweets_from_json(json_reader, text_writer):
    json_tweets = json_reader.readlines()
    for json_tweet in json_tweets:
        try:
            if json_tweets:
                tweet = json.loads(json_tweet)  # load it as Python dict
                text = tweet['text']
                text = text.replace("\n", " ").strip()
                text_writer.write(text)
                text_writer.write("\n")
        except json.decoder.JSONDecodeError as error:
            pass


def extract_tweets_from_json_files(json_dir, text_dir):
    for json_file in os.listdir(json_dir):
        json_file = os.path.join(json_dir, json_file)
        filename, ext = os.path.splitext(json_file)
        text_file = os.path.join(text_dir, os.path.basename(filename) + '.txt')
        with open(json_file, mode='r', encoding='utf-8') as json_reader, open(text_file, mode='w', encoding='utf-8') as text_writer:
            print('extract tweets from {}'.format(json_file))
            extract_tweets_from_json(json_reader, text_writer)
            print('tweets extracted to {}'.format(text_file))
            print('--------------------')


if __name__ == '__main__':
    args = parser.parse_args()
    json_dir = args.json_dir
    out_dir = args.out_dir
    extract_tweets_from_json_files(json_dir, out_dir)