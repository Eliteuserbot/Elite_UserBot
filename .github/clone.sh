#!/bin/bash

# eliteuserbot file 
# if you want to use 
# use with credits 

echo "
'||''''| '||     |''||''| |''||''| '||''''| 
 ||   .   ||        ||       ||     ||   .  
 ||'''|   ||        ||       ||     ||'''|  
 ||       ||        ||       ||     ||      
.||....| .||...| |..||..|   .||.   .||....|                                                                                       
"

echo " 
  _    _  _____ ______ _____  ____   ____ _______ 
 | |  | |/ ____|  ____|  __ \|  _ \ / __ \__   __|
 | |  | | (___ | |__  | |__) | |_) | |  | | | |   
 | |  | |\___ \|  __| |  _  /|  _ <| |  | | | |   
 | |__| |____) | |____| | \ \| |_) | |__| | | |   
  \____/|_____/|______|_|  \_\____/ \____/  |_|   
"

FILE=/app/.git

if [ -d "$FILE" ] ; then
    echo "$FILE directory exists already."
else
    rm -rf userbot
    rm -rf .github
    rm -rf sample_config.py
    git clone https://github.com/xHOPExINFINTY/Elite_UserBot Elite_UserBot
    mv Elite_UserBot/userbot .
    mv Elite_UserBot/.github . 
    mv Elite_UserBot/.git .
    mv Elite_UserBot/sample_config.py .
    python ./.github/update.py
    rm -rf requirements.txt
    mv Elite_UserBot/requirements.txt .
    rm -rf cat_ub
fi

FILE=/app/bin/
if [ -d "$FILE" ] ; then
    echo "$FILE directory exists already."
else
    bash ./.github/bins.sh
fi

python -m userbot
