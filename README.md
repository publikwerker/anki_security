# anki_security

![](https://www.jbhifi.co.nz/FileLibrary/ProductResources/Images/111696-L-LO.jpg)
_Vector_

The basic premise for this app was formed from observing the Vector robot I bought my daughter for a "pet" for the holidays.
When Vector charges, it assumes a "relaxed" posture and its display portrays mostly-closed eyes.
Vector uses Alexa technology, so if there is a loud noise, Vector "wakes up" and looks startled.
My goal is to build an app that reacts to these sudden noises by taking a short video or by taking several still images in sequence.
After which, Vector would return to "sleep".


![](https://www.theawesomedick.com/wp-content/uploads/2018/10/IMG_20181026_185208-264x300.jpg)
_Vector in Sleep Mode_

The manufacturers of Vector, Anki, have provided some solid documentation for developers to use. They provide a SDK (Software Development Kit), example files, and tutorials.
One major hurdle I have encountered is that the SDK provides access to events like face recognition, object recognition, but no access to any event triggered by noises other than a pre-set `wake-word`, "Hey, Vector". 
Access to the `raw_audio` stream has been promised, but has not yet been released.
In the meantime, I will still build the app, and simply switch the event handler to trigger when Vector hears the `wake_word`.
It should be easy to move the event handler to the `sudden_noise` event once we have access to the audio stream.

Now, the challenge is to limit the video stream to ten seconds, and then save the video stream to memory.

My alternate idea was to design animated behavior to trigger when someone asks, "What time is it?"
Unfortunately, the SDK doesn't provide access to word recognition, either.

Two days into my Python education, and things are going well.
I'm able to use what I know of ES6 and extrapolate it to Python.
The learning curve doesn't seem as sharp.
This time, though, I am teaching myself, so it feels like more "work" to learn it.
I'm able to watch tutorials and apply little bits to my programs.
Learning Python is definitely easier than learning JavaScript.
My learning style of reading and implementing seems to be working: I'm building a solid knowledge base, but I'm stuck on the implementation.
I spent the first day doing exercises and reading the basics.
The second day was researching the Anki API and doing more basic exercises.
Today, I'll be fleshing out my Anki app. I'm to have a MVP by the end of the day.
Definitely doable.
