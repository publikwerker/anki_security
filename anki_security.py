"""Security system for Vector

This is an example of using Python to direct Vector's behavior. When awakened by a loud noise, he should announce 'Documenting disturbance' and then take 10 seconds of video."""

import sys
import anki_vector
import io
import time

def main():
  args = anki_vector.util.parse_command_args()
  with anki_vector.Robot(args.serial, 
    show_viewer=True, 
    enable_camera_feed=True,) as robot:
    print("Say 'Documenting Disturbance'...")
    print("Starting video viewer. Use Ctrl+C to quit.")
    robot.say_text("Documenting disturbance")

    try:
      while True:
        time.sleep(10)
    except KeyboardInterrupt:
      pass

if __name__ == "__main__":
  main()

