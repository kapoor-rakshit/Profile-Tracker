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
	
	if site=="Github":
		gurl='https://api.github.com/users/'+user
		ginfo=requests.get(gurl)
		ginfo=ginfo.json()
		handle=ginfo['login']
		pic=ginfo['avatar_url']
		prof=ginfo['html_url']
		name=ginfo['name']
		comp=ginfo['company']
		mail=ginfo['email']
		bio=ginfo['bio']
		repo=ginfo['public_repos']
		fol=ginfo['followers']

		gurl2='https://api.github.com/users/'+user+'/repos'
		rinfo=requests.get(gurl2)
		rinfo=rinfo.json()
		ll=len(rinfo)
        i=0
        reponames=[]
        stars=[]
        forks=[]
        langs=[]
        langset=set()
        langct=0
        tplist=[]
        perclist=[]
        langdata=[]
        langperc={}
        langval=[]

        while i<ll:
        	rp=rinfo[i]['name']
        	st=rinfo[i]['stargazers_count']
        	fr=rinfo[i]['forks_count']
        	reponames.append(rp)
        	stars.append(st)
        	forks.append(fr)
        	
        	langurl='https://api.github.com/repos/'+user+'/'+rp+'/languages'
        	langinfo=requests.get(langurl)
        	langinfo=langinfo.json()

        	langstr=""
        	for key in langinfo.keys():
        		langstr+=(str(key)+" .  ")
        		langset.add(key)
        		langval.append(key)
        		langct+=1
        	langs.append(langstr)
        	i+=1

        for i in langset:
        	langperc[i]=0
        for i in langval:
        	langperc[i]+=1
        for i in langperc.keys():
        	langperc[i]=((langperc[i]*100)/float(langct))
        tplist=sorted(langperc,key=langperc.__getitem__,reverse=True)
        for i in tplist:
        	perclist.append(format(langperc[i],'0.2f')+" %")

        data=zip(reponames,stars,forks,langs)
        langdata=zip(tplist,perclist)
        return render_template('github.html',langdata=langdata,repodetails=data,user=handle,pic=pic,profile=prof,name=name,org=comp,mail=mail,summary=bio,repo=repo,followers=fol)

	"""if site=="Codeforces":
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
"""
if __name__ == '__main__':
	app.debug = True
	app.run()