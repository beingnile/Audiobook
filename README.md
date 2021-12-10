# Audiobook.

A simple CLI tool  that converts your PDF files into an mp3 audiobook. I use the google text-to-speech `gtts` module for the conversion. I chose `gtts` based on the argument that google is a giant company that utilises large data sets and therefore better audio. Not perfect but good enough.

## Prerequisites.

* [Python](https://www.python.org/downloads/)

> Preferrably python3+, git is for cloning the program to your system

* [git](https://git-scm.com/)

### Required packages.

* pip
* gTTS
* pdfplumber

> You don't have to worry about installing the python packages, the repository includes a bash script file that will install the required packages for you.
## Getting Started.

First things first, clone the repository into your system. You can clone it into any directory you want.

```sh

$ git clone https://github.com/beingnile/Audiobook

```

Give all the files executable permissions. All the file except the README file ofcourse.

```sh

$ chmod u+x audiobook
$ chmod u+x req.sh

```
If you don't have the packages installed, you can install it with the following command.

```sh

$ ./req.sh

```

## Running the program.

Once you have all the required packages, you can run the program.
The pdf file will be automatically saved as `book.mp3` in the same directory as the program. They both have to be in the same folder. You can change the name of the file if you want. I suggest you do so as it will make it easier to find the file.

> I will soon update a permanent solution for this where you can run the program from anywhere.

To run the program, type the following command in the terminal.

```sh

$ ./audiobook book.pdf

```

## Author.

This Project was made and is maintained by [Nile](https://github.com/beingnile)