Create and activate the virtual environment:

```console
python3 -m venv env
source env/bin/activate
```

Install all the required dependencies:

```console
pip install -r requirements.txt
```

Open the project directory in a text editor:

```console
code .
```

Run the live-reload Sphinx server:

```console
sphinx-autobuild . _build/html/
```

Make changes as needed and push the code.