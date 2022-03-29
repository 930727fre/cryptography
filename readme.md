# Password-manager
## Usage
```
python3 main.py
```
## Features
1. This command line help you manage your password on google sheets elegantly.
2. Encrypt your password with hash.
3. Copy password to clipboard automatically.
4. [Demonstration video](https://youtu.be/SfdZxzV8e0g)

## Pip setup
```
pip install -r requirements.txt
```
## Google cloud setup
1. Create a project on [Google cloud](https://cloud.google.com/)
2. Register a account as an editor(Google drive api).
3. Download authtication.json and move it to the same folder as main.py.
```
structure:
.
├── authentication.json
├── main.py
├── rsa-encryption.py
└── readme.md
```

4. Create a google sheet and share it to your editor account.
5. Modify line 2 in main.py
```
YOUR_KEY=""
```
fill `YOUR_KEY` with the string after https://docs.google.com/spreadsheets/d/ (your Google sheet url).
In my case, my google sheet url is https://docs.google.com/spreadsheets/d/1DHI3k0KYCeTFyj_JwDnTWu8fGvAmwGZXkQvxN_xw9t4/edit#gid=628264246
so `YOUR_KEY` should be `1DHI3k0KYCeTFyj_JwDnTWu8fGvAmwGZXkQvxN_xw9t4`.

6. That's it, check out this [video](https://www.youtube.com/watch?v=T1vqS1NL89E&t=307s) for more detail about Google cloud api.
