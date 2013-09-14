from random import randrange, choice

phrasings = ['You should totally build ', 'You gotta make ', 'The world really needs ',
        'You cannot go wrong with ', 'Hack on ', 'Work on making ',
        'You absolutely have to build ', 'My life is incomplete until you build ',
        'Seriously, just work on ']

types_of_apps = ['a social network', 'a dating website', 'a video game', 'a productivity app',
    'a funding platform', 'a blogging platform', 'a knowledge sharing resource',
    'a sperm donation platform', 'a crowd polling resource', 'a news resource',
    'a communication tool', 'an advice giving resource', 'a wiki', 'a self motivation tool',
    'a version control system', 'an idea generator', 'a prank app', 'a note sharing resource',
    'a message board', 'an educational app', 'an email tool', 'a browser extension',
    'a search engine', 'a crowd sourced ranking system', 'a social media platform',
    'a pornographic website', 'a pirating website', 'a gambling app', 'a web based taxi service',
    'a directory listing', 'a notification system', 'an alert system', 'a reminder app',
    'a vim plugin', 'an emacs extension', 'an IDE text editor',
    'a command line utility', 'dotfiles', 'an irc chat client', 'a navigation app',
    'a specialized web browser', 'a new operating system', 'a calendar app', 'a banking utility',
    'a black market', 'an advertisement system', 'a content management system',
    'ad tracking', 'AB testing', 'a marketplace']

companies = ['Facebook', 'YouTube', 'OK Cupid', 'Twitter', 'Tumblr', 'Google',
        'Stumble Upon', 'PayPal', 'Dropbox', 'LinkedIn', 'SoundCloud', 'eBay',
        'Kickstarter', 'Craigslist', 'Wikipedia', 'Github', 'Gmail', 'Instagram',
        'Vine', 'Klout', 'Bang With Friends', 'Last.fm', 'Code Academy', 'Snapchat',
        'Foursquare', 'Yelp', 'Pandora', 'Grub Hub', 'Groupon', 'Airbnb', 'Spotify',
        'Tinder', 'Google Maps', 'Groupme', 'Nextbus', 'Trip Advisor', 'Siri',
       'IMDB', 'Reddit', '4chan']

groups = ['old people', 'college students', 'musicians', 'pirates', 'ninjas', 'sex offenders',
        'metalheads', 'punks', 'neighborhoods', 'hipsters', 'hackers',
        'sports fans', 'women', 'animals', 'animal lovers', 'monks',
        'some arbitrary religious group', 'bands', 'samurai', 'anime fans',
        'old school video game enthusiasts', 'businessmen', 'scam artists',
        'escaped convicts', 'sea captains', 'assasins', 'ideas',
        'organized crime syndicates', 'alcoholics', 'artists', 'scientists',
        'military officers', 'CEOs', 'rich people', 'poor people', 'the homeless',
        'startup companies', 'writers', 'poets', 'storytelling', 'truck drivers', 'bus drivers'
        'public transit', 'travelers', 'fortune tellers', 'hikers', 'bikers', 'skateboarders',
        'MMORPG players', 'insomniacs', 'lumberjacks', 'foreign immigrants',
        'left handed people', 'the obese', 'people with terminal illnesses',
        'people who are lactose intolerant', 'potheads',
        'hackathons', 'parents', 'jazz lovers', 'frat parties',
        'parties', 'events', 'vikings']

def generate_idea():
    option = randrange(0, 2, 1)
    if option == 0:
        return choice(phrasings) + choice(types_of_apps) + ' for ' + choice(groups)
    elif option == 1:
        return choice(phrasings) + choice(companies) + ' for ' + choice(groups)
    elif option == 2:
        return choice(phrasings) + choice(companies) + ' for ' + choice(companies)
print generate_idea()
