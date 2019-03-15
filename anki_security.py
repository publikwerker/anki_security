"""Copyright 2019 Publikwerks, LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Security system for Anki Vector

This is an example of using Python to direct Vector's behavior. When awakened by a loud noise, he should announce 'Documenting disturbance' and then take 10 seconds of video."""

import sys
import anki_vector
import io
import time
import cv2

#Create an event listener for audio cue
#In this instance, it's upon hearing the
#words "Hey, Vector"

def on_wake_word(robot):
  #give him sceptical eye display
  robot.anim.play_animation("anim_observing_far_subtle_01")
  #tilt his head up for better view of room
  robot.anim.play_animation("anim_referencing_curious_01_head_angle_20")
  print("Starting video viewer. Use Ctrl+C to quit.")

  #voice notification
  robot.say_text("Quietly observing from the shadows.")
  #img = cv2.VideoCapture.read(robot.viewer.show_video())
  #cv2.imwrite('surveill.avi', img)
  time.sleep(20)
  robot.viewer.stop_video

def main():
  args = anki_vector.util.parse_command_args()
  with anki_vector.Robot(args.serial,
    show_viewer=True, #opens view portal
    #enable_audio_feed=True, #need to initialize first
    enable_camera_feed=True, #accesses video
    ) as robot:
    on_wake_word(robot)

    try:
      while True:
        time.sleep(20)
    except KeyboardInterrupt:
      pass

if __name__ == "__main__":
  main()

