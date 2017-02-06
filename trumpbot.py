from TrumpMuslimBanData import *

props = ['First Name','Last Name','State','Political Party','Stance','Took office','Term Expires','Email/Contact Form','Local Office Number','District','Statement','Statement Link','Twitter Link','Twitter Handle','Address','Previous Statement','Last Updated','Notes','Phone Number','Local Office Address','Press/Campaign Handle','Picture','Label','Stance in short','Shape','Title']       
statesAcro = {'AL': 'Alabama','AK': 'Alaska','AZ' :	'Arizona','AR' :'Arkansas','CA' :'California','CO' :'Colorado','CT' :'Connecticut','DE' :	'Delaware','FL' :	'Florida','GA':	'Georgia','HI' :'Hawaii','ID' :	'Idaho','IL' :	'Illinois','IN' :'Indiana','IA' :'Iowa','KS' :	'Kansas','KY' :	'Kentucky','LA' :'Louisiana','ME' :	'Maine','MD' :	'Maryland','MA' :'Massachusetts','MI' :	'Michigan','MN' :'Minnesota','MS' :	'Mississippi','"MS"':'Mississippi','MO' :	'Missouri','MT' :'Montana','NE' :	'Nebraska','NV' :	'Nevada','NH' :	'New Hampshire','NJ' :'New Jersey','NM' :'New Mexico','NY' :'New York','NC' :'North Carolina','ND' :'North Dakota','OH' :'Ohio','OK' :'Oklahoma','OR' :	'Oregon','PA' :	'Pennsylvania','RI' :'Rhode Island','SC' :	'South Carolina','SD' :	'South Dakota','TN' :'Tennessee','TX' :	'Texas','UT' :	'Utah','VT' :'Vermont','VA' :'Virginia','WA':'Washington','WV' :	'West Virginia','WI' :'Wisconsin','WY' :'Wyoming','DC':'Washington D.C.','PR':'Puerto Rico','GU':'Guam','VI': 'Virgin Islands','AS':'American Samoa','MP': 'Northern Mariana Islands'}
AcroRev =  {v: k for k, v in statesAcro.iteritems()}


for n in range(len(men)):
	men[n]['Label']=men[n]['First Name']+' '+men[n]['Last Name']



allnodes = [(v, k,'State') for k, v in states.items()]
allnodes.extend([(v, k,'Political Party') for k, v in party.items()])
allnodes.extend([(v, k,'Title') for k, v in titles.items()])
allnodes.extend([(v, k,'Stance') for k, v in stance.items()])
allnodes.extend((x['id'],x['Label'],x['title'],x) for x in men)
allnodes.sort(key = lambda w:w[0])


avatar = dict(avatar)


### Post graph in padagraph

from reliure.schema import Doc, Schema
from reliure.types import Text, Numeric , Boolean, GenericType
from botapi import Botagraph, BotApiError


# graph attributes and schema

gid = "US Politicians on Immigration EO"
g_attrs = {
    'description': "stances and declarations for the senators, governors, attorneys general and representatives on Trum Muslim Ban",
    'tags': ['Trump','Muslim Ban', 'Immigration EO'],
    'image': "http://sharing.wxyz.com/sharescnn/photo/2017/01/28/GettyImages-632945624_1485656938867_54192778_ver1.0_900_675.jpg"
}



Senator = {
    'name' : "Senator",
    'description' : "Senator",
    'properties' : {'label' : Text(),
                    'shape' : Text(default=u"triangle"),
                    'Stance':Text(),
                    'Statement':Text(),
                    'Statement Link':Text(),
                    'Term Expires':Text(),
                    'Address':Text(),
                    'Phone Number':Text(),
                    'Local Office Number':Text(),
                    'Email/Contact Form':Text(),
                    'Twitter Link':Text(), 
                    'Twitter Handle':Text(),
                    'Press/Campaign Handle':Text(),
                    'Local Office Address':Text(),
                    'Previous Statement':Text(),
                    'image':Text()
                    }
}

Governor = {
    'name' : "Governor",
    'description' : "Governor",
    'properties' : {'label' : Text(),
    				'shape' : Text(default=u"circle"),
    				'Took office': Text(), 
    				'Term Expires': Text(), 
    				'Stance': Text(),
    				'Statement': Text(),
    				'Statement Link': Text(),
    				'Phone Number': Text(),
    				'Email/Contact Form': Text(),
    				'Twitter Link': Text(), 
    				'Local Office Address': Text(),
    				'Notes': Text(),
					'image':Text()
    				}
}

AG = {
    'name':"Attorney General",
    'description':"Attorney General",
    'properties': {'label' : Text(),
    				'shape' : Text(default=u"circle"),
    				'Stance': Text(), 
    				'Statement': Text(),
    				'Statement Link': Text(),
    				'Term Expires': Text(),
    				'Address': Text(), 
    				'Phone Number': Text(),
    				'Email/Contact Form': Text(),
    				'Twitter Link': Text(),
    				'Twitter Handle': Text(),
    				'Press/Campaign Handle': Text(),
    				'Notes': Text(),
    				'image':Text()        			
    				}
}


Rep = {
    'name':"Representative",
    'description':"Representative",
    'properties': {'label' : Text(),
    				'shape' : Text(default=u"circle"),
    				'District': Text(),
    				'Stance': Text(), 
    				'Notes': Text(),
    				'Last Updated': Text(),
    				'Statement': Text(),
    				'Statement Link': Text(),
    				'Address': Text(), 
    				'Phone Number': Text(), 
    				'Email/Contact Form': Text(),
    				'Twitter Handle': Text(),
    				'Previous Statement': Text(),
    				'image':Text()       
    				}
}

State = {
    'name':"State",
    'description':"State of the U.S.",
    'properties': {'label' : Text(),
    				'shape' : Text(default=u"circle"),
    				'image':Text()     
    				}
}

Stance = {
    'name':"Stance",
    'description':"Stance: opposed, supportive, skeptical, silent",
    'properties':{'label' : Text(),
    				'shape' : Text(default=u"circle"),
    				'image':Text()     
    				}
}

Title = {
    'name':"Title",
    'description':"Job: senator, governor, ag, rep",
    'properties': {'label' : Text(),
    				'shape' : Text(default=u"circle")}
}


Party = {
    'name':"Political Party",
    'description':"Political Party: democrat, republican, independent",
    'properties': {'label' : Text(),
    				'shape' : Text(default=u"circle"),
    				'image':Text()     
    				}
}


PartyEdge = {
'name':"political party",
    'description':"belong to political party",
    'properties': {}
}


StanceEdge = {
'name':"Stance",
    'description':"Stance on the immigration EO",
    'properties': {}
}


StateEdge = {
'name':"State",
    'description':"Elected in State",
    'properties': {}
}

TitleEdge = {
'name':"Title",
    'description':"job",
    'properties': {}
}


# Bot initialisation

host = "http://public.padagraph.io"
key  = "WyJqb2FubmUuYm9pc3NvbkBnbWFpbC5jb20iLCIkMmIkMTIkdHo2T1NIYkxLaUtJNmw0ZFc3TDlnZVZxVFFhMFJjZnlsdGVyOGNQOWZSUzJ2ZmRqR1ZtZGEiXQ.C3eVNQ.A7DKEdBQwTz5WhFcF2WZtq5arAU"

#key  = "WyJqb2FubmUuYm9pc3NvbkBnbWFpbC5jb20iLCIkMmIkMTIkdHo2T1NIYkxLaUtJNmw0ZFc3TDlnZVZxVFFhMFJjZnlsdGVyOGNQOWZSUzJ2ZmRqR1ZtZGEiXQ.Cuvqeg.VO0vLWQnjFvPEg1_ZzeghVWcN1Q"
bot = Botagraph(host, key)


# Post schema

if not bot.has_graph(gid) :     
	print "\n * Creating graph %s" % gid
	bot.create_graph(gid, g_attrs)
	print "\n * Creating Schema"
	bot.post_nodetype(gid, Senator['name'], Senator['description'], Senator['properties'])
	bot.post_nodetype(gid, Governor['name'], Governor['description'], Governor['properties'])
	bot.post_nodetype(gid, Rep['name'], Rep['description'], Rep['properties'])
	bot.post_nodetype(gid, AG['name'], AG['description'], AG['properties'])
	bot.post_nodetype(gid, State['name'], State['description'], State['properties'])
	bot.post_nodetype(gid, Stance['name'], Stance['description'], Stance['properties'])
	bot.post_nodetype(gid, Party['name'], Party['description'], Party['properties'])
	bot.post_nodetype(gid, Title['name'], Title['description'], Title['properties'])
	bot.post_edgetype(gid, PartyEdge['name'],  PartyEdge['description'],  PartyEdge['properties'] )
	bot.post_edgetype(gid, StanceEdge['name'],  StanceEdge['description'],  StanceEdge['properties'] )
	bot.post_edgetype(gid, StateEdge['name'],  StateEdge['description'],  StateEdge['properties'] )
 	bot.post_edgetype(gid, TitleEdge['name'],  TitleEdge['description'],  TitleEdge['properties'] )
 

# get schema from db

schema = bot.get_schema(gid)['schema']
nodetypes = { n['name']:n for n in schema['nodetypes'] }
edgetypes = { e['name']:e for e in schema['edgetypes'] }
print schema

# Index vertex label: uuid

idx = {}

# vertex generator for bulk inserts

#allnodes.extend([(v, k,'Stance') for k, v in stance.items()])
#allnodes.extend((x['id'],x['Label'],x['title'],x) for x in men)


def Prop(t,d):
	p = {}
	if t=='Senator':
		pr = Senator['properties'].keys()	
	elif t=='Governor':
		pr = Governor['properties'].keys()
	elif t=='Attorney General':
		pr = AG['properties'].keys()
	elif t=='Representative':
		pr = Rep['properties'].keys()
	pr.remove('shape')
	pr.remove('image')
	for x in pr:
		try:
			p[x]=d[x]
		except:
			pass
	try:
		p['image']=avatar[d['id']]
	except:
		pass
	return p
		
		
def gen_nodes():
	for elt in allnodes:
		t = elt[2]
		p = {}
		if t=='Political Party' :
			s = 'triangle'
			try:
				p['image']=images[elt[1]]
			except:
				pass
		elif t=='State'or t=='Title':
			s = 'square'
		elif t=='Stance':
			s = 'circle'
			try:
				p['image']=images[elt[1]]
			except:
				pass
		else:
			s = elt[3]['Shape']
			p = Prop(t,elt[3])
		p['shape'],p['label']=s,elt[1]
		if t=='State':
			try:
				p['image']=images[elt[1]]
			except:
				pass
			p['label']=p['label']+' ('+AcroRev[p['label']]+')'
			p['label']=p['label'].upper()
		if t=='Title' or t=='Stance' or t=='Political Party':
			p['label']=p['label'].upper()
		yield {
			'nodetype': nodetypes[t]['uuid'],
			'properties': p
			}
       
# edges generator for bulk inserts

def gen_edges():
    for x in edges:
    	src = idx[x[0]]
    	tgt = idx[x[1]]
    	if x[1] in stance.values():
    		t = 'Stance'
    		l = 'stance'
    	elif x[1] in party.values():
    		t = 'political party'
    		l = t
    	elif x[1] in states.values():
    		t = 'State'
    		l = 'state'
    	elif x[1] in titles.values():
    		t = 'Title'
    		l = 'elected as'
        yield {
            'edgetype': edgetypes[t]['uuid'],
            'source': src,
            'label' : l,
            'target': tgt,
            'properties': {}
        }


print "posting nodes"
count = fail = 0
idd = 0
for node, uuid in bot.post_nodes( gid, gen_nodes() ):
    if not uuid:
        fail += 1
    else :
        count += 1
        # get uuid for edges
        idx[idd] = uuid
        idd+=1    
    print "%s(%s)/%s nodes inserted " % (count, fail, len(allnodes) )

# Bulk insert egdes

print "posting edges"
count = fail = 0
for obj, uuid in bot.post_edges( gid, gen_edges() ):
    if not uuid:
        fail += 1
    else :
        count += 1
    print "%s(%s)/%s edges inserted " % (count, fail, len(edges))

		


		
		
#stars = ['Senator', 'Attorney General', 'Governor', 'Representative','Neutral or Skeptical', 'Supportive', 'Silent', 'Opposed','Independent', 'Republican', 'Democrat']
#rien = ['California','Texas', 'Iowa', 'Alabama','South Carolina', 'Vermont','Colorado', 'New Jersey','Washington', 'New York', 'Nevada','Bob Ferguson','Robert Bentley','Jerry Brown','John Hickenlooper','Terry Branstad','Brian Sandoval','Chris Christie','Andrew Cuomo','Henry McMaster','Phil Scott','Jeff Sessions', 'Dianne Feinstein','Kamala Harris','Cory Gardner', 'Joni Ernst','Chuck Grassley','Cory Booker','Chuck Schumer','Lindsey Graham','Tim Scott','John Cornyn','Ted Cruz','Pat Leahy', 'Bernie Sanders', 'Maria Cantwell','Patty Murray', 'Terri Sewell','Bradley Byrne','Martha Roby','Robert Aderholt', 'Ted Lieu','Norma Torres','Raul Ruiz','Karen Bass','Linda S\xc3\xa1nchez','Lucille Roybal-Allard','Maxine Waters','Lou Correa','Kevin McCarthy','Mimi Walters','Duncan Hunter','Jim Costa','Jeff Denham','David Valadao','Edward "Ed" Royce','Mark DeSaulnier','Nancy Pelosi','Jackie Speier','Eric Swalwell','Ro Khanna','Dana Rohrabacher','Darrell Issa','Ed Perlmutter','Mike Coffman', 'Ken Buck','Doug Lamborn', 'David Loebsack', 'Steve King', 'Rod Blum','Donald Norcross', 'Bonnie Watson Coleman', 'Rodney Frelinghuysen','Christopher Smith', 'Leonard Lance','Frank LoBiondo','Thomas MacArthur','Jacky Rosen','Dina Titus','Jos\xc3\xa9 Serrano','Eliot Engel','Nita Lowey','Sean Maloney','Paul Tonko','Louise Slaughter','Brian Higgins','John Faso','Elise Stefanik','John Katko','Lee Zeldin','Peter King','Daniel Donovan','Claudia Tenney','James Clyburn','Mick Mulvaney','Mark Sanford','Trey Gowdy','Joe Wilson','Jeff Duncan', 'Pete Olson','Lloyd Doggett','Will Hurd','Vicente Gonzalez','Sam Johnson','Jeb Hensarling','Mike Conaway','Mac Thornberry','Kenny Marchant','Pete Sessions','Marc Veasey','Louie Gohmert','Ted Poe','John Ratcliffe','Joe Barton','John Carter','Brian Babin','Peter Welch', 'Rick Larsen','Derek Kilmer','Pramila Jayapal','Adam Smith', 'Denny Heck', 'David Reichert','Luther Strange','Xavier Becerra','Cynthia Coffman','Tom Miller','Adam Laxalt','Christopher Porrino','Eric Schneiderman','Alan Wilson','Ken Paxton','T.J. Donovan']
#stars.extend(gover)

senator = set()
for x in men:
	if x['title']=='Senator':
		senator.add(x['Label'])
		senator.add(x['State'])
		
stars = list(senator)
stars.extend(['Neutral or Skeptical', 'Supportive', 'Silent', 'Opposed','Independent', 'Republican', 'Democrat'])
stars.append('Senator')		

# Star most prox vertices
rev = {}
for x in allnodes:
	rev[x[1]]=x[0]
print "Starring %s nodes" % len(stars)
if len(stars):
    stars = [ idx[rev[e]] for e in stars ]
    bot.star_nodes(gid, stars)