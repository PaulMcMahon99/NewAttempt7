# To call the programme, navigate to the OnlineShop directory, and
# type:
# python app.py.

# Note to self, the commands to get the app going are:
# source activate myflask
# pip install ###
# export FLASH_APP=app.py - locks onto the right file
# Do the three below in order:
# flask.db init - makes the db
# flask.db migrate -m "description" - links to the app.
# flask db upgrade - finalises any changes.

from onlineshop import app

if __name__ == '__main__':
    app.run(debug=True)

# debug is still active here for building the app purposes.  When it is running
# it shall be given as app.run() as the default is false.
# This is as per the usual requirements for publishing.
