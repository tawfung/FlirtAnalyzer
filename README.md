# FlirtAnalyzer
This project is my senior project and I build it for my best friend because her flirting skill became an instinct.

Version 1: Focus on detect emotion from text. 

Version 2: Analyse deep text. (When I start? I don't know. :D) 

## Libraries and tools:

##### nltk

##### django

##### keras

##### tensorflow

##### numpy

## Installation:

* #### Ubuntu:

    + Install virtual environment:
        ```
        pip install virtualenv
         
        virtualenv venv
        ```

    + Activating virtual environment:
        ```
        source venv/bin/activate
        ```

* #### Windows:
    + Install virtualenv:
        ```
        pip install virtualenvwrapper-win
        
        mkvirtualenv venv
        ```
    + Activating virtualenv:
        ```
        workon venv
        ```
    + Recommended IDE:
        - PyCharm Jetbrain
        
    
* #### Run:
    + Install libs: You can update libraries version inside requirements.txt.
        ```
        pip install -r requirements.txt
        ```
    + Run:
        - Switch to app folder: ```cd EDfT```
        - Run app: ```python manager.py runserver```
        
        => Open browser(firefox/chrome/...) and type this address to enjoy: [localhost:8000/](http://localhost:8000/).
        
        => Train model: [localhost:8000/train/](http://localhost:8000/train/).
         