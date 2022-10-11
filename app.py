from flask import Flask
from housing.exception import HousingException
from housing.logger import logging 
import sys
app = Flask(__name__)

@app.route("/" , methods=["GET","POST"])
def index():
    try:
        raise Exception("We are testing exception module")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return "Ci/CD pipeline has been created"

if(__name__=="__main__"):
    app.run(debug=True)