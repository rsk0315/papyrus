# papyrus
Enhanced IDLE (IDE for Python)

## Requirements
- `Python 2.7` (Not compatible with 3.x yet)
- [`regex`](https://pypi.python.org/pypi/regex)

## Installation
Back up `idlelib` directory just in case
  (found in `/usr/lib64/python2.7/` or `C:\Python27\Lib`)

Replace `idlelib/*.*` by `papyrus-master/*.*`

Copy `papyrus-master/*/` to `idlelib/`

Download and install `regex` module

```
$ pip install regex
```


## What differs from original IDLE
- Enhanced syntax highlight  
  `Menu bar > Highlight > (FavoriteLanguage)`  

  * colorize special characters in string and numeric literals
  * compatible with C, C++, Python, Markdown, and Brainf*ck
  * Github-like theme
  `Menu bar > Options > Configure IDLE > Highlighting Theme > _Github`

- Show line number
  `Menu bar > Options > Line Number`
  (but not good enough, especially in UNIX)

## Naming
- 'papyrys' suggests paper, or editor
- 'papyrus' contains substring 'PY', since written in `Python`


## Trouble shooting
- highlighted improperly
  * Recolorize from `Menu bar > Highlight > (FavoriteLanguage)`

- displayed font improperly (like proportional fonts)
  * Relaunch
  * Change font from `Menu bar > Options > Configure IDLE > Fonts/Tabs > Font Face`

## To do
- Correct line number on UNIX
- Retouch parenmatch for C and C++
- Make compatible with other languages


## Contact me
- Twitter:
  `@rsk0315_h4x`
