import os

import click
import requests
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("API_TOKEN", "")
CHAT_ID = os.getenv("CHAT_ID", "")
THREAD_ID = os.getenv("THREAD_ID", "")
if not TOKEN or not CHAT_ID:
    raise ValueError("Missing API_TOKEN.")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"


@click.group()
def cli():
    pass


@click.command(name="merry-xmas", help="Send a Merry Christmas message.")
def merry_xmas():
    text_message = r'''
    Merry Christmas!
```
                                 |
                               \ ' /
                             -- (*) --
                                >*<
                               >0<@<
                              >>>@<<*
                             >@>*<0<<<
                            >*>>@<<<@<<
                           >@>>0<<<*<<@<
                          >*>>0<<@<<<@<<<
                         >@>>*<<@<>*<<0<*<
           \*/          >0>>*<<@<>0><<*<@<<
       ___\\U//___     >*>>@><0<<*>>@><*<0<<
       |\\ | | \\|    >@>>0<*<0>>@<<0<<<*<@<<  
       | \\| | _(UU)_ >((*))_>0><*<0><@<<<0<*<
       |\ \| || / //||.*.*.*.|>>@<<*<<@>><0<<<
  jgs  |\\_|_|&&_// ||*.*.*.*|_\\db//_               
       """"|'.'.'.|~~|.*.*.*|     ____|_
           |'.'.'.|   ^^^^^^|____|>>>>>>|
           ~~~~~~~~         '""""`------'
    ```
    '''
    data = {
        "chat_id": CHAT_ID,
        "parse_mode": "Markdown",
        "message_thread_id": THREAD_ID,
        "text": text_message,
    }
    res = requests.post(url=URL, data=data)
    if res.status_code != 200:
        exit(1)


@click.command(name="happy-new-year", help="Send a Happy New Year message.")
def happy_new_year():
    text_message = r"""
```
?̮̑●̮̑?★⋰⋱☆⋰⋱★⋰⋱☆⋰⋱★⋰⋱☆⋰⋱★?̮̑●̮̑?
──────█─█ █▀█ █▀█ █▀█ █─█─────
──────█▀█ █▀█ █▀▀ █▀▀ ▀█▀─────
──────▀─▀ ▀─▀ ▀── ▀── ─▀──────
█▄─█ █▀▀ █─█─█──█─█ █▀▀ █▀█ █▀█
█─██ █▀▀ █─█─█──▀█▀ █▀▀ █▀█ ██▀
▀──▀ ▀▀▀ ─▀▀▀────▀─ ▀▀▀ ▀─▀ ▀─▀
?̮̑●̮̑?★⋰⋱☆⋰⋱★⋰⋱☆⋰⋱★⋰⋱☆⋰⋱★?̮̑●̮̑?
```
    """
    data = {
        "chat_id": CHAT_ID,
        "parse_mode": "Markdown",
        "message_thread_id": THREAD_ID,
        "text": text_message,
    }
    res = requests.post(url=URL, data=data)
    if res.status_code != 200:
        exit(1)
    pass


@click.command(name="message", help="Send a custom text.")
@click.option("-t", "--text", help="Custom text to send.")
@click.option("-pm", "--parse_mode", help="Message parse mode", default="Markdown")
def message(text, parse_mode):
    data = {
        "chat_id": CHAT_ID,
        "parse_mode": parse_mode,
        "message_thread_id": THREAD_ID,
        "text": text,
    }
    res = requests.post(url=URL, data=data)
    if res.status_code != 200:
        exit(1)


cli.add_command(merry_xmas)
cli.add_command(happy_new_year)
cli.add_command(message)


if __name__ == "__main__":
    cli()
