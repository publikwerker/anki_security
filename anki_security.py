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

#Create an event listener for audio cue
#In this instantce, it's upon hearing the
#words "Hey, Vector"
def wait_for_cue()

def main():
  args = anki_vector.util.parse_command_args()
  with anki_vector.Robot(args.serial,
    show_viewer=True, 
    enable_camera_feed=True,) as robot:
    robot.anim.play_animation("anim_observing_far_subtle_01")
    robot.anim.play_animation("anim_referencing_curious_01_head_angle_20")
    print("Starting video viewer. Use Ctrl+C to quit.")
    robot.say_text("Quietly observing from the shadows.")

    try:
      while True:
        time.sleep(10)
    except KeyboardInterrupt:
      pass

if __name__ == "__main__":
  main()

