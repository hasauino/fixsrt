# fixsrt
A python script to fix srt file exported from sonix ai with double lines encoded with a special string

Input file:
```
1
00:00:01,640 --> 00:00:02,720
السلام عليكم ورحمة الله

2
00:00:02,750 --> 00:00:03,810
حيّاكم الله يا كرام

3
00:00:03,830 --> 00:00:06,350
سامحوني على التأخر لظرف طارئ

4
00:00:07,370 --> 00:00:11,000
كما تعلمون إخواننا وأحبابنا بدانا معكم###

5
00:00:11,000 --> 00:00:14,540
قبل أكثر من سنتين مشوار سلسلة رحلة اليقين

```

output file:
```

00:00:01,640 --> 00:00:02,720
السلام عليكم ورحمة الله

2
00:00:02,750 --> 00:00:03,810
حيّاكم الله يا كرام

3
00:00:03,830 --> 00:00:06,350
سامحوني على التأخر لظرف طارئ

4
00:00:07,370 --> 00:00:14,540
كما تعلمون إخواننا وأحبابنا بدانا معكم
قبل أكثر من سنتين مشوار سلسلة رحلة اليقين

```
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
