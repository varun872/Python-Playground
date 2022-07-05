from pygame import mixer
import datetime

def eye():
    mixer.init()
    mixer.music.load("eye.mp3")
    mixer.music.set_volume(2)
    mixer.music.play()

def water():
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.set_volume(2)
    mixer.music.play()

def physical():
    mixer.init()
    mixer.music.load("physical.mp3")
    mixer.music.set_volume(30)
    mixer.music.play()

def gettime():
    return datetime.datetime.now()

start_time=(9,0,0)
end_time=(17,0,0)

