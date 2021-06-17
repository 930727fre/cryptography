# password-manager
## usage
```
python3 main,py
```
## feature
1. command line programe so that you can execute it without any obstabcle.
2. saving your information on google sheet, which is a very stable and hands-on platform.
3. auto-copy password you'r looking for
3. [demonstation video](https://youtu.be/g_DK2DOiSII)

## set up pip
```
pip install gspread
pip install clipboard
```
## set up google cloud
1. create a project on [google cloud](https://cloud.google.com/)
2. register a account as a editor(google drive).
3. download authtication.json ,rename it to "certification.json" ,and move it to the same folder as main.py.
4. create a google sheet and share it to your editor account.
4. modify a line in main.py
```
sh=gc.open_by_key("1DHI3k0KYCeTFyj_JwDnTWu8fGvAmwGZXkQvxN_xw9t4")
```
change the key into the code in your google sheet url.
In my case, my google sheet url is https://docs.google.com/spreadsheets/d/1DHI3k0KYCeTFyj_JwDnTWu8fGvAmwGZXkQvxN_xw9t4/edit#gid=628264246
5. That's it, check out this [video](https://www.youtube.com/watch?v=T1vqS1NL89E&t=307s) for more detail about google cloud api.
