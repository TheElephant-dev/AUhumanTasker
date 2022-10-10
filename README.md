# AUhumanTasker
a python script to detect, and execute human-like actions of tasks in the corona-time popular game "Among Us"


* Note that the code was statically made for a "4K" screen with a non-dynamic monitor setup.
    As it "samples"(screenshot part of) the screen in order to both detect what task is currently open AND knows where to click&how long.
    Aswell as detect the custom made ingame font numbers for some tasks.
    
    Thus some changes will be required to run the code on a different setup in regard to
        1. where the screenshot of task detection is made
        2. the locations of where it should click
        3. the scale of images taken to detect "Random" tasks. (such as unlock manifolds number randomization.)
