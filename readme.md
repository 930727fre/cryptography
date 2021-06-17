# password-manager
## usage
```
python3 main,py
```
## feature
1. Command line program so that you can execute it without any obstacle.
2. Saving your information on google sheet, which is a very stable and hands-on platform.
3. Auto-copy password you are looking for.
3. [Demonstration video](https://youtu.be/g_DK2DOiSII)

## set up pip
```
pip install gspread
pip install clipboard
```
## set up google cloud
1. Create a project on [google cloud](https://cloud.google.com/)
2. Register a account as a editor(google drive).
3. Download authtication.json ,rename it to "certification.json" ,and move it to the same folder as main.py.
4. Create a google sheet and share it to your editor account.
4. Modify a line in main.py
```
sh=gc.open_by_key("1DHI3k0KYCeTFyj_JwDnTWu8fGvAmwGZXkQvxN_xw9t4")
```
change the key into the code in your google sheet url.
In my case, my google sheet url is https://docs.google.com/spreadsheets/d/1DHI3k0KYCeTFyj_JwDnTWu8fGvAmwGZXkQvxN_xw9t4/edit#gid=628264246
5. That's it, check out this [video](https://www.youtube.com/watch?v=T1vqS1NL89E&t=307s) for more detail about google cloud api.
