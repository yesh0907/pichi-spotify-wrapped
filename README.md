Pichi Spotify Wrapped
=============

Set up
------------

1. Install [Homebrew](https://brew.sh/)
2. Install Python 3.8 and virtualenv

        $ brew install python@3.8
        $ pip3 install virtualenv
3. Make virtual environment (you can change backend to any name, e.g: pichi-spotify-wrapped)

        $ virtualenv -p python3.8 pichi-spotify-wrapped && cd pichi-spotify-wrapped
4. Activate virtual environment

        $ source bin/activate
5. Clone Github repo

        $ git clone https://github.com/yesh0907/pichi-spotify-wrapped src
6. Install python dependencies

        $ cd src
        $ pip install -r requirements.txt

7. Open the project up in VSCode (if you have the command line tool installed)

        $ code .

8. Click `main.ipynb` in the side panel; if the prompt to install the jupyter extension pops up, please go ahead and install it

9. On the top right select the python interpreter that has the virtual environment python executable path.

10. Happy coding!