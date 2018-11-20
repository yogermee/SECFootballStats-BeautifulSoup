from bs4 import BeautifulSoup
import mysql.connector
import urllib
import re

class Scraper():
	def __init__(self):
		pass

	sec_teams_dict = {u'Arkansas Razorbacks': 31, u'Vanderbilt Commodores': 736,
	u'Alabama Crimson Tide': 8, u'South Carolina Gamecocks': 648, u'Kentucky Wildcats': 334,
	u'Auburn Tigers': 37, u'Tennessee Volunteers': 694, u'Florida Gators': 235,
	u'Mississippi Rebels': 433, u'Georgia Bulldogs': 257, u'LSU Tigers': 365,
	u'Missouri Tigers': 434, u'Mississippi State Bulldogs': 430, u'Texas A&M Aggies': 697}

	def convertHeight(self, height):
		height = height.replace("'", "")
		height = height.split('-')
		feet = int(height[0])
		inches = int(height[1])

		return "'" + str((feet * 12) + inches) + "'"

	def buildAllURLs(self):
		print "Initiating URL build process..."

		base_url_front = 'http://www.cfbstats.com/'
		base_url_middle = '/team/'
		base_url_back = ['/roster.html', '/rushing/index.html', '/passing/index.html', '/receiving/index.html',
		'/puntreturn/index.html', '/kickreturn/index.html', '/punting/index.html', '/kickoff/index.html',
		'/scoring/index.html', '/total/index.html', '/allpurpose/index.html', '/interception/index.html',
		'/fumblereturn/index.html', '/tackle/index.html', '/tackleforloss/index.html', '/sack/index.html',
		'/miscdefense/index.html']

		team_numbers = []
		all_urls = []

		for key, value in self.sec_teams_dict.iteritems():
			team_numbers.append(str(value))

		for team in team_numbers:
			for season in range(2012, 2018):
				for url in base_url_back:
					all_urls.append(base_url_front + str(season) + base_url_middle + team + url)

			print "All URLs constructed for team number: " + team

		"URL build process completed."

		return all_urls

	def scrapeURL(self, url):
		print "Initiating URL scraping process for " + url

		html = urllib.urlopen(url)
		bsObj = BeautifulSoup(html, 'lxml')

		# Extracting year, team, and stat type

		year = re.findall(r'\d+', bsObj.title.getText())[0]
		team = ''
		stat = ''

		for team_name, number in self.sec_teams_dict.iteritems():
			if str(number) in re.findall(r'team/[\d]+', url)[0]:
				team = team_name

		if "index" in url:
			stat = re.findall(r'\w+/index', url)[0][:-6]
		else:
			stat = "roster"

		# Building data columns

		raw_columns = bsObj.find_all('th')
		final_columns = []

		for column in raw_columns:
			if column.getText() == "":
				column = "Rank_On_Team"
				final_columns.append(column)
			else:
				column = column.getText().replace(".", "")
				column = column.replace("/", "_")
				column = column.replace("%", "pct")
				column = column.replace("-", "_")
				column = column.replace(" ", "_")
				
				if column == "Int":
					column = "Ints"

				final_columns.append(column)

		# Building data rows

		raw_rows = bsObj.find_all('td')
		final_rows = []

		for item in raw_rows:
			item = item.getText()

			if item == "-":
				final_rows.append("0")
			else:
				final_rows.append(item)

		print "URL scraping process successfully compelted for " + url

		return (year, team, stat, final_columns, final_rows)

	def buildData(self, data):
		print "Initiating build process for all scraped data..."		

		year = data[0]
		team = data[1]
		stat = data[2]
		final_columns = data[3]
		final_rows = data[4]
		column_prefix = ["Season", "Team"]

		player_data = []

		for number in range(0, len(final_rows), len(final_columns)):
			player_prefix = [year, team]
			player = final_rows[number:number + len(final_columns)]

			player[1] = player[1].replace("'", "")
			player[-1] = player[-1].replace("'", "")			
			player[-2] = player[-2].replace("'", "")

			if player[1] == " Team":
				pass
			elif player[1] == "Total":
				pass
			elif player[1] == "Opponents":
				pass
			else:		
				player_data.append(player_prefix + player)

		final_columns = column_prefix + final_columns

		print "All scraped data successfully compiled."

		return (stat, final_columns, player_data)

	def postToDB(self, data):
		print "Initiating process to commit data to database..."
		cnx = mysql.connector.connect(user ='root', password = 'INSERT PASSWORD HERE',
			host = 'localhost', database = 'secstats', auth_plugin = 'mysql_native_password')
		cursor = cnx.cursor()

		table = data[0]
		columns = data[1]
		rows = data[2]

		for item in rows:
			if table == "roster":
				if len(item[6]) == 1:
					item[6] = "0"					
				else:
					item[6] = self.convertHeight(item[6])[1:-1]
			else:
				pass

			column = ', '.join(columns)
			row = ', '.join("'" + item + "'" for item in item)

			cursor.execute("INSERT INTO %s (%s) VALUES (%s);" % (table, column, row))
			cnx.commit()

			print "Successfully committed to database:"
			print "Table: " + table
			print column
			print row

scraper = Scraper()
urls = scraper.buildAllURLs()

for url in urls:
	scrape_url = scraper.scrapeURL(url)
	data = scraper.buildData(scrape_url)

	scraper.postToDB(data)
