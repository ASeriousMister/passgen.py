# passgen.py
Yet another random password generator
### Usage
To use it simply run
```
python3 passgen.py
```
and the generated password will be shown in your terminal window.

### GUI version
There is also a huy version available, showing a pop-up window containing the password and two bottons:
- one copies the password to the clipboard;
- one empties the clipboard and closes the pop-up window.
To use it install dependencies with
```
pip3 install -r requirements.txt
```
and run the tool with
```
python3 passgenguy.py
```

### Password specs
- Random lenght between 16 and 20 characters
- Includes uppercase and lowercase letters, digits and symbols
### Disclaimer
The tool does not log the genrated passwords, so make sure to store them safely by yourself.
There is no guarantee about passwords' quality, use them only if you think they fit your needs. 
