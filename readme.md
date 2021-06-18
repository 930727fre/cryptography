# Password-manager
## Usage
```
python3 main.py
```
## Feature
1. Command line program so that you can execute it without any obstacle.
2. Save your information on google sheet, which is a very stable and hands-on platform.On top of that, you can modify file manually.
3. Auto-copy password you are looking for.
3. [Demonstration video](https://youtu.be/g_DK2DOiSII)

## pip setup
```
pip install gspread
pip install clipboard
```
## Google cloud setup
1. Create a project on [google cloud](https://cloud.google.com/)
2. Register a account as a editor(google drive api).
3. Download authtication.json ,rename it to "credential.json" ,and move it to the same folder as main.py.
4. Create a google sheet and share it to your editor account.
4. Modify line 6 in main.py
```
sh=gc.open_by_key("1DHI3k0KYCeTFyj_JwDnTWu8fGvAmwGZXkQvxN_xw9t4")
```
change the key into the code in your google sheet url.
In my case, my google sheet url is https://docs.google.com/spreadsheets/d/1DHI3k0KYCeTFyj_JwDnTWu8fGvAmwGZXkQvxN_xw9t4/edit#gid=628264246

and the code is 1DHI3k0KYCeTFyj_JwDnTWu8fGvAmwGZXkQvxN_xw9t4


5. That's it, check out this [video](https://www.youtube.com/watch?v=T1vqS1NL89E&t=307s) for more detail about google cloud api.
