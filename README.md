# Rosehip
Reliable Operating System by Elisha Hollander Implemented Python

```diff
- this only works on Ubuntu, Debian and Mint
```
there is also a [version for windows](https://github.com/donno2048/Rosehip).

There is also a [version for web](https://github.com/donno2048/Rosehip-repl), which is not recommended

There is no version for Android but you can install [Pydroid](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) and download the source code, open _os.py_ in Pydroid, then by running in the Pydroid terminal `pip install pygame pyttsx3 pygame-gui Js2Py html2text markdown2` and pressing the play button on landscape mode you will enter Rosehip, from the programming apps only python, JavaScript and html are working on Android, and from the utilities only the Chrome app and the Camera app won't..

## How to install:

download the project from the releases section or [go there directly](https://github.com/donno2048/Rosehip-L/releases), extract the folder then:

Open command line in the folder

###### To install python: (skip it if you already have python)
```bash
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
```
###### To install pip for python: (skip it if you already have pip)
```bash
sudo apt install python3-pip
```
###### To install requirements:
```bash
pip3 install -r rose
```
## How to use it:

Open commad line in the folder then:
```bash
python3 os.py
```
## What can you do with it:

* press HOME button to open the menu bar
* press INSERT button to open the painter
  * scroll up and down to change the size of the brush
  * scroll up and down while holding ALT button to change the color of the brush
  * scroll up and down while holding CTRL button to change the shape of the brush


## To do:
- [x] ~~[animations](https://en.wikipedia.org/wiki/Stop_motion)~~
- [x] ~~[pong](https://en.wikipedia.org/wiki/Pong)~~
- [x] ~~variety of compilers ([python](https://www.python.org/), [html](https://en.wikipedia.org/wiki/HTML), [javascript](https://www.javascript.com/), [perl](https://www.perl.org/), [java](https://www.java.com/en/), [bash](https://www.gnu.org/software/bash/), [c](https://en.wikipedia.org/wiki/C_(programming_language)), [ruby](https://www.ruby-lang.org/en/), [c++](https://en.wikipedia.org/wiki/C%2B%2B), and [lua](http://www.lua.org/)~~)
- [x] ~~[chrome](https://en.wikipedia.org/wiki/Google_Chrome)~~
- [x] ~~[text based web-browser](https://en.wikipedia.org/wiki/Text-based_web_browser)~~
- [x] ~~[ogg music player](https://en.wikipedia.org/wiki/Ogg)~~
- [x] ~~[calculator](https://en.wikipedia.org/wiki/Calculator)~~
- [x] ~~[clock](https://en.wikipedia.org/wiki/Clock)~~
- [x] ~~[background color picker](https://en.wikipedia.org/wiki/Wallpaper_(computing))~~
- [x] ~~[background image picker](https://en.wikipedia.org/wiki/Wallpaper_(computing))~~
- [x] ~~[camera](https://en.wikipedia.org/wiki/Camera)~~
- [x] ~~[mp4 viewer](https://en.wikipedia.org/wiki/MPEG-4_Part_14)~~
- [x] ~~[maze](https://en.wikipedia.org/wiki/Maze)~~
- [ ] [CLI](https://en.wikipedia.org/wiki/Command-line_interface)

## For developers:

if you want to use it as an .iso you can run [another code I wrote](https://github.com/donno2048/CITUR-L)

or you can either use the [.iso builder](https://github.com/donno2048/CITUR) for the [windows version of Rosehip](https://github.com/donno2048/Rosehip)  but it's currently having some issues, as specified is the [README](https://github.com/donno2048/CITUR/blob/master/README.md)...

## For extreme developers:

I recently added auto-support for any pygame app, open the master branch, the blade-runner in the util folder is an example for this method, run the patch file using:

```sh
patch blade_runner/__init__.py blade.patch
```

In the blade-runner folder to make the blade_runner app compatible.

(This was never tested...)
