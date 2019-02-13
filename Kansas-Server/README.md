# Kansas Server

### Difficulty: beginner 

### Type: stenanography

### Hint: Kansas Server

### Flag: localhost

### Solution:

    #Play it backwards you'll hear "There's no place like 127.0.0.7"
    #reverse the audio:
    ~$ sudo apt install sox
    ~$ sox hint.wav solution.wav

    #Listen
    ~$ vlc solution.wav
