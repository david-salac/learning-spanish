# Simple scripts to help you learn the Spanish language
The simple set of scripts to help you learn foreign (Spanish) language.

## Module for numbers (file numbers.html)
Module for training ordinal and cardinal numbers in Spanish.

## Module for regular and irregular verbs (file verbs.html)
Module for training of the verb conjugation using all the options.

For making this module working you need to make the file `verb.json` available
on some server and set-up this address to variable `remote_url` (down at
the file with proper comment).

### Verb server
The simplest way how to run the server that provides verbs to the script is
to use Python application in script `verb_server.py`. In order to do so:
1. Install Python in the latest version.
2. Install requirements, in this cases using:
`pip install flask`
3. Run the server using:
`python verb_server.py` 
You should see in your console something like:
`* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
which symbolise that your server is running correctly.
