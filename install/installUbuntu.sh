#!/bin/bash

sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-tk
#python3 -m pip install git+https://github.com/RedFantom/ttkthemes
pip install ttkthemes
pip install tkcalendar

echo "#!/bin/bash" > ../launch.sh
echo python3 ./src/app.py > ../launch.sh

chmod +x ../launch.sh
