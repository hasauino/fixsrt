import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfixsrt",
    version="0.0.1",
    author="Hassan Umari",
    author_email="oh91@windowslive.com",
    description="A python script to fix srt file exported from sonix ai with double lines encoded with a special string",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hasauino/fixsrt",
    scripts=['bin/fixsrt.py'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
