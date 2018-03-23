# Adbot-Nobo

Simple bot to post/delete/refresh ads

### Dependencies

- python 3.6
- lxml
- selenium
- dateparser
- chromium
- pandas
- re
- from datetime import datetime, timedelta
- sys

### Usage

:warning: **Do not rename the repository after cloning it**<br/>
:warning: **launch the script at the root of the repository**
```
cd adbot-nobo
```
then
```
./bin/adbot.sh
```
or
```
python3.6 source/adbot.py
```

### Source

##### adbot.py :

This file is used to generate the call the methods needed for post ad
main python script that calls modules in websites_ads/

##### websites_ads directory :

- leboncoin.py :

module to post and delete ads(from excel file) on leboncoin.com

### Integration

You can add a module to integrate a website in the "websites_ads"
directory and call it in the main function in adbot.py

### Ressources

- img directory :

Directory where image used in ads are put
