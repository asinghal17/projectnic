import os
import logging
from flask import Flask,request,render_template
from flask_cache import Cache
from flask_compress import Compress
from lib import gscrape
from time import time

chap = "1blZPkNxrw3ovfLvqD76eUzTuME34N2bl1fSTdaMjX2c"
marq = "1wFK2aPJmXjAQAx3rT2vF7H-8NvveWQ7tuXdEoemhZ1M"
board = "1JbaMwsPHbN3og_igSOJfJEzf2IJimAIqzrbf_ra6Pp0"
osuexec = "1RVdYx88BnZ7IEWP1Kidk00-K80V96cCWOMCIrqfpw9U"
uclaexec = "11GzqdZtLeu2tlfwQ4Mk0sy387Hh9H2l_fDg6-at_EG0"

logging.basicConfig(filename='log/app.log',format="%(asctime)s, log_level=%(levelname)s, %(message)s",level=logging.DEBUG)
logger_app = logging.getLogger("app")
logger_perf = logging.getLogger("app.perf")
logger_perf.setLevel(logging.ERROR)

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300
app.cache=Cache(app)
Compress(app)

@app.cache.cached(key_prefix="marquee")
def get_marquee():
	return gscrape.getMarqueeFeed(marq)

@app.cache.cached(key_prefix="appfeed")
def get_appfeed():
	return gscrape.getAppFeed(chap)

@app.cache.cached(key_prefix="board")
def get_board_members():
	return gscrape.getMemberFeed(board)

@app.cache.cached(key_prefix="memberfeed")
def get_member_feed():
	return map(gscrape.getMemberFeed,(uclaexec,osuexec))

@app.route('/')
def index():
	marquee=get_marquee()
	chap=get_appfeed()
	return render_template("index.html", title="Home",marquee=marquee,chapters=chap)

@app.route('/about')
def about():
	nat_mem=get_board_members()
	return render_template("about.html", title="About", board=nat_mem)

@app.route('/projects')
def projects():
	return render_template("projects.html", title="Projects")

@app.route('/chapters')
def chapters():
	chap=get_appfeed()
	memfeed = get_member_feed()
	return render_template("chapters.html", title="Chapters",chapter=chap,osue=memfeed[1])

@app.route('/donate')
def donate():
	chap=get_appfeed()
	return render_template("donate.html",title="Donate",chapters=chap)

@app.route('/locations')
def locations():
	return render_template("locations.html",title="Locations")

@app.route('/privacy-policy')
def privacy():
	return render_template("privacy-policy.html",title="Privacy Policy")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html',title="Error"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', title="Error"), 500

if __name__=="__main__":
    app.run(debug=False)

