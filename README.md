# mouse-spam

## About 
This is a small script to randomly move your mouse and click mouse buttons. It uses *xdotool* package to simulate mouse input. You can use it for any purpose, but you have to understand this can be harmful (for example accidentally delete files or send a message).

## System requierments
Almoust any Linux OS. Hardware doesn't matter

## Installation
1) Download .sh or .py

   **main.py** has an infinite loop, which moves mouse randomly, then clicks random mouse buttons (left, middle, right, wheel up, wheel down).
   
   **main.sh** script is using `python3 -c` to run the same thing as main.py
   
2) Install dependencies
 
   Necessary packages: *coreutils* , *xdotool* 3.1 or later, *python3.5* or later
     
3) Run main.py with python3.5 or later

   Run main.sh with **sh**. Alternatively use `chmod +x main.sh` to make it executable, and tun using `./main.sh`.
   
4) How do I stop it?

   Better read this before statring the script) Switch to non-gui tty, usually **ctrl+alt+f3/f2** can help you (f7 is gui). Than type `killall python3`, and use *sudo* if there are some permission errors. WARNING! This will kill ALL pythno3 processes. It can be harmful for system or other running programs.
