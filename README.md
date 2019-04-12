# instagram-scraper

It is a cmd application written in Python and it scrapes and downloads an instagram user's photos.


For running program, follow below steps
-------
>> Clone the repository and create a virtualenv 

```bash
$ virtualenv venv
$ source venv/bin/activate
```

>> After activating virtual environment, Install all dependencies / packages

```bash
$ pip install -r requirements.txt
```

>> After Installing required dependencies , open credentials.py and change it to your account details 

## Parameters
| Parameter            | Type|                Description                           |
|:--------------------:|:---:|:----------------------------------------------------:|
| Username             | str | Your instagram username                              |
| password             | str | Your instagram password                              |
| target_username      | str | instagram account you want to target                 |
| Path                 | str | Directory path where you want to download images     |
| Driver_path          | str | Path of your chrome driver                           |

>> To run program:

```bash
$ python insta_scrapper.py
```


Usage
-----

To scrape a user's images:
To scrape a private user's media you must be an approved follower.*

