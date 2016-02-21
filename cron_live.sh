#! /bin/bash

export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

workon btcprices
cd /var/www/btcprices/lib
python get_prices.py

