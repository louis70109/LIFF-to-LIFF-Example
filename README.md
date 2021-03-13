# LIFF to LIFF Example

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-%3E%3D%203.5-blue.svg)](https://badge.fury.io/py/lotify)


It builds by:

- flask/Python 3.7
- LINE v11.2.x

> You need Github, LINE, Heroku accounts to deploy this bot.

# Developer Side

## Environment property

These are properties which you need to import to environment.(see `.env.example`)

```
LIFF_SHARE_A=
LIFF_SHARE_B=
```

```
cp .env.example .env
```

## LINE account

- Got A LINE Bot API developer account
  Make sure you already registered, if you need use LINE Bot.

* Go to **LINE Developer Console**
  - Create a **LINE Login** channel.
  - Go to LIFF tab and create two LIFF page.
    - A Endpoint URL: `https://{YOUR_URL}/liff/a`
    - B Endpoint URL: `https://{YOUR_URL}/liff/b`
* You will get two **LIFF ID** (A & B), need fill back to `.env` file.

## Local testing

1. first terminal window

```
cp .env.example .env
pip install -r requirements.txt --user
python api.py
```

2. If you don't have own domain(e.g. https://nijialin.com), use ngrok tp create a temporary Https:

```
ngrok http 5000
```

or maybe you have npm environment:

```
npx ngrok http 5000
```

![](https://i.imgur.com/azVdG8j.png)

3. Copy url to LINE Login's LIFF pages(A & B endpoint).

4. Copy A LIFF url to any place where you could open it on mobile.

## Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

If you are not sure where are files in, use following up commands:

```
heroku run bash
heroku logs --tail
```

# License

MIT License
