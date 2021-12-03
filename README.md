# Qtile Config 🔧
![Preview of what this config looks like on my pc](https://imgur.com/A5uXyj9.jpg)
## About
This is my own Qtile config, clone it and customize it in your own way. This config was forked and modified from DistroTube. 

Make sure to set your preferred mod key in config.py in there you will also find a set of variables to set your default applications.

For easy access to the Qtile config you can add the following line of code to your `.bashrc / .zshrc`

    alias qtile-config=<your editor> ~/config/qtile/config.py


## Keybinds
**MOD + Shift + R:** Reload Qtile config  
**MOD + Shift + Q:** Quit Qtile  
**MOD + \<Number>:** Switch between workspaces  

**MOD + X:** Close focused window  
**MOD + Ctrl + \<Arrow Keys>:** Resize focused window  
**MOD + Shift + \<Arrow Keys>:** Move focused window  
**MOD + Shift + \<Number>:** Move focused window to different workspace.  
**MOD + Tab:** Toggle fullscreen on focused window. ( Actually this switches layouts but we only have 2 so this toggles it )  

**MOD + R:** Opens run prompt at the right side of topbar.   
**MOD + Enter:** Open terminal ( Define terminal in config.py )  
**MOD + W:** Open webbrowser ( Define browser in config.py )  
**MOD + F:** Open filemanager ( Define filemanager in config.py )  
**MOD +  V:** Open VirutalBox ( Disabled by default )

**MOD + \<Drag with your mouse>:** Turn dragged window into floating instead of collumn.



## Dependencies  

 - Alsa-Utils  
 - Pulsemixer  

## Known bugs
- Volume control jumps arround a lot, should add 5% per click but adds random values.
- Brightness control does not work yet.
- When you drag a windows into floating there is no way to set it back to column mode other then to reload the config.
