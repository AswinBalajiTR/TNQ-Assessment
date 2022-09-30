## DEVELOPMENT

<hr>

### SETUP

(use python, pip for windows and python3, pip3 for linux or mac)

first create a virtual environment as:

```bash
python3 -m venv venv
```

then activate the environment (for linux and mac)

```bash
source venv/bin/activate
```

for windows

```bash
/venv/Scripts/activate.bat
```

Now use pip to install the requirements

```bash
pip3 install -r requirements.txt
```

### START THE SERVER

to start the dev server (without debug ON)

```bash
flask --app server run
```

with debug ON

```bash
flask --app server --debug run
```
