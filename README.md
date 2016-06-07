# xidle
Enhanced IDLE (IDE for Python)

## Requirments
- `Python 2.7` (Not compatible with 3.x yet)
- [`regex`](https://pypi.python.org/pypi/regex)

## Installation
Back up `idlelib` directory just in case
  (found in `/usr/lib64/python2.7/` or `C:\Python27\Lib`)

Replace `idlelib/*.*` by `xidle/*.*`

Copy `xidle/*/` to `idlelib/`


## What differs from original IDLE
- Enhanced syntax highlight
  * colorize special characters in string and numeric literals
  * compatible with C, C++, Python, and Brainf*ck
  `Menu bar > Highlight > ${each of languages}`
  * Github-like theme
  `Menu bar > Options > Configure IDLE > Highlighting Theme > _Github`

- Show line number
  `Menu bar > Options > Line Number`
  (but not good enough)


## Trouble shooting
- highlighted improperly
  * Try to recolorize from `Menu bar > Highlight > ${certain language}`

- displayed font improperly (like proportional fonts)
  * Try to relaunch
  * Try to change font from `Menu bar > Options > Configure IDLE > Fonts/Tabs > Font Face`

## To do
- Correct line number on UNIX
- Enhance auto completion for C and C++
- Retouch parenmatch for C and C++
- Make compatible with other languages


## Contact me
- Twitter:
  `@rsk0315_h4x`
