# flet-tutorial
This repor is for all the Flet tutorials in order to learn this framework.

## Installation 

pip install flet

flet --version

## Create new project

flet create \<App Name\>

This creates a project with the following template:
```
\<App Name\>
|
|->tutorial
    |
    |->asset
        |
        |->icon.png
    .gitignore
    main.py //this is the main file for running the programm
    README.md
    requirements.txt
```

## Running the app

```
flet run //Runs the main.py at cerntain directory
```

If you need to provide a different path to the file, use the following command:

```
flet run [script]
```

To run as an app:
```
flet run --web [script]
```
or to run in a fixed port:
```
flet run --web --port 8000 app.py
```



