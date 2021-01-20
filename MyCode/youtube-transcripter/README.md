1. First install _pipenv_

  $ `pip install pipenv`

2. go to the directory of this project

  $ `cd youtube-transcriber-doraemon`

3. install the necessary libraries

  $ `pipenv install`

4. Libav also needs to be installed

  $ `brew install libav`

5. Run the program

  $ `pipenv run python transcriber.py --youtube-url [URL]`
  * you can also specify the speech recognition library to use:

    $ `pipenv run python transcriber.py --youtube-url [URL] --speech-recognizer [RECOGNIZER]`

    * recognizer can be "sphinx" (default) or "wit"
