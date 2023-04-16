import json
import spammer
import splitter

with open('config.json','r') as f:
    config = json.load(f)
    
FILE_PATH = config["file_path"]
DELAY = config["delay"]

spam = spammer.Spammer(DELAY,FILE_PATH)
split = splitter.Splitter(FILE_PATH)

split.rewrite()

spam.countdown(3)
spam.spam()