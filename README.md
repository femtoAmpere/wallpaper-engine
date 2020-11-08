**E621 WALLPAPER ENGINE**  
Wallpaper slideshow based on e621.net tags

## Requirements
Python3  
_tested on Python3.6_

## Usage
EZ Startup: Make sure `%PATH%` is set correctly and run `pythonw.exe .\main.py`.   
_You can also use `run_in_background.cmd`_

- Adjust `wallengine/config.py` as you like. 
- If you want soft image transition/animation on change:  (Un)Comment the marked lines in `main.py` to use Windows slideshow. Use same setting for `slideshow_minutes` as in Windows settings.  

## Known Issues
If you allow Windows to `Automatically pick an accent colour from my background` there might be lags on wallpaper change. This is not an issue caused by this engine.
