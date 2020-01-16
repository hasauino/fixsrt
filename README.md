# fixsrt
A python script to fix srt file exported from sonix ai with double lines encoded with a special string


# Install

```
pip install -i https://test.pypi.org/simple/ pyfixsrt
```

# Usage

- Basic:

```
fixsrt.py file.srt
```
- Change output file name, default "output":

```
fixsrt.py file.srt --output file_out
```

- Chnage line end flag characters, default "###":

```
fixsrt.py file.srt --eol "****"
```
