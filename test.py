from flask import *
import requests

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('sitechoice.html')

@app.route('/results',methods=['post'])
def results():
	site=request.form['site']
	user=request.form['user']
	
	if site!="Codeforces":
		return 'API for %s under-construction'%site

	if site=="Codeforces":
		url='http://codeforces.com/api/user.info?handles='+user
		info=requests.get(url)
		info=info.json()
		chk=info['status']
		if chk=="FAILED":
			return 'Request FAILED because %s '%info['comment']
		else:
			info=info['result']
			pic=info[0]['titlePhoto']
			email="-"
			if 'email' in info[0].keys():
				email=info[0]['email']

			handle=info[0]['handle']
			rating=info[0]['rating']
			level=info[0]['rank']
			mxrating=info[0]['maxRating']
			mxlevel=info[0]['maxRank']
			ct="-"
			if 'country' in info[0].keys():
				ct=info[0]['country']
			fr=info[0]['friendOfCount']
			org="-"
			if 'organization' in info[0].keys():
				org=info[0]['organization']
			contri=info[0]['contribution']

        url2='http://codeforces.com/api/user.rating?handle='+user
        conts=requests.get(url2)
        conts=conts.json()
        chk=conts['status']
        if chk=="FAILED":
        	return 'Request FAILED because %s '%conts['comment']
        else:
        	conts=conts['result']
        	contsct=len(conts)

        url3='http://codeforces.com/api/user.status?handle='+user+'&from=1&count=1000000'
        solved=requests.get(url3)
        solved=solved.json()
        chk=solved['status']
        if chk=="FAILED":
        	return 'Request FAILED because %s '%solved['comment']
        else:
        	ac=0
        	solved=solved['result']
        	l=len(solved)
        	for i in range(0,l,1):
        		if solved[i]['verdict']=="OK":
        			ac+=1

		return render_template('codeforcesres.html',ac=ac,pic=pic,email=email,username=handle,rating=rating,level=level,maxrating=mxrating,maxlevel=mxlevel,country=ct,friends=fr,org=org,contri=contri,contests=contsct)

if __name__ == '__main__':
	app.debug = True
	app.run()