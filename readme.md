# Password-manager
## Usage
```
python3 main.py
```
## Features
1. This is a command line program so that you can execute it without any obstacle.
2. Save your information on google sheet, which is a very stable and secure platform. On top of that, you can modify files manually.
3. Encrypt your password with hash.
4. Auto-copy password you are looking for.
5. [Demonstration video](https://youtu.be/SfdZxzV8e0g)

## Pip setup
```
pip install gspread
pip install clipboard
pip install bcrypt
```
## Google cloud setup
1. Create a project on [Google cloud](https://cloud.google.com/)
2. Register a account as an editor(Google drive api).
3. Download authtication.json ,rename it to "credential.json" ,and move it to the same folder as main.py.
```
structure:
.
├── credential.json
├── main.py
└── readme.md
```

4. Create a google sheet and share it to your editor account.
5. Modify line 7 in main.py
```
sh=gc.open_by_key("YOUR_KEY")
```
change `YOUR_KEY` into the string after https://docs.google.com/spreadsheets/d/ (your Google sheet url).
In my case, my google sheet url is https://docs.google.com/spreadsheets/d/1DHI3k0KYCeTFyj_JwDnTWu8fGvAmwGZXkQvxN_xw9t4/edit#gid=628264246
so `YOUR_KEY` should be `1DHI3k0KYCeTFyj_JwDnTWu8fGvAmwGZXkQvxN_xw9t4`.

6. That's it, check out this [video](https://www.youtube.com/watch?v=T1vqS1NL89E&t=307s) for more detail about Google cloud api.
