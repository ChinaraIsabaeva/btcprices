#! /bin/bash

export WORKON_HOME=/home/chinara/Envs
source /usr/local/bin/virtualenvwrapper.sh
workon btc-trading
cd /home/chinara/dev/my_projects/btc-trading/lib
python get_prices.py
