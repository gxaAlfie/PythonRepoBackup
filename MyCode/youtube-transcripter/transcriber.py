import speech_recognition as sr
import argparse
import subprocess
import os

def download_video(url):
    FNULL = open(os.devnull, 'w')
    ydl = subprocess.Popen('youtube-dl {url} -o "youtube_audio.%(ext)s" '
                           '--audio-format wav --extract-audio'.format(url=url), stdout=FNULL, shell=True,
                           stderr=subprocess.STDOUT)
    print "Downloading youtube video..."
    ydl.wait()
    print "Download complete!\n"
    return open("youtube_audio.wav")

def read_video(file_name, recognizer):
    print 'Processing youtube video...'
    try:
        r = sr.Recognizer()
        with sr.AudioFile(file_name) as source:
            audio = r.record(source)

        if recognizer == "wit":
            output = r.recognize_wit(audio, "AY4J4V2G2MNKE2PUNP7ACEL5CTKPUTKI")
        else:
            output = r.recognize_sphinx(audio)
    except IOError as exc:
        output = 'Unable to find the audio file.'
    except sr.UnknownValueError:
        output = 'Error reading audio'
    return output

def main(args=None):
    print("Welcome!")
    if args.youtube_url:
        file_name = download_video(args.youtube_url)

    if args.speech_recognizer:
        speech_recognizer = args.speech_recognizer
    else:
        speech_recognizer = "sphinx"

    transcription = read_video(file_name, speech_recognizer)

    print 'Finished reading wav file! \n\nTranscription:'
    print transcription

    os.remove("youtube_audio.wav")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--youtube-url", help="Enter the full url of the youtube video to read from.")
    parser.add_argument("--speech-recognizer", help="Enter the speech recognizer you want to use (sphinx, wit) (default: sphinx)")
    args = parser.parse_args()
    main(args)
