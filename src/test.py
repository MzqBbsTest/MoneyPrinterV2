import schedule
import subprocess

from art import *
from cache import *
from utils import *
from config import *
from status import *
from uuid import uuid4
from constants import *
from classes.Tts import TTS
from termcolor import colored
from classes.Twitter import Twitter
from classes.YouTube import YouTube
from prettytable import PrettyTable
from classes.Outreach import Outreach
from classes.AFM import AffiliateMarketing


def main():
    # Show user options
    info("\n============ OPTIONS ============", False)

    while True:
        info("\n============ OPTIONS ============", False)

        for idx, youtube_option in enumerate(YOUTUBE_OPTIONS):
            print(colored(f" {idx + 1}. {youtube_option}", "cyan"))

        info("=================================\n", False)
        # Get user input
        tts = TTS()
        youtube = YouTube(
            "1",
            "2",
            "4",
            "3",
            "en"
        )
        youtube.generate_video(tts)
        rem_temp_files()




if __name__ == "__main__":
    # Print ASCII Banner
    print_banner()

    first_time = get_first_time_running()

    if first_time:
        print(
            colored("Hey! It looks like you're running MoneyPrinter V2 for the first time. Let's get you setup first!",
                    "yellow"))

    # Setup file tree
    assert_folder_structure()

    # Remove temporary files
    # rem_temp_files()

    # Fetch MP3 Files
    fetch_songs()

    while True:
        main()
