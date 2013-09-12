from random import randrange, choice

phrasings = ['You should totally build ', 'You gotta make ', 'The world really needs ',
        'You cannot go wrong with ', 'Hack on ', 'Work on making ',
        'You absolutely have to build', 'My life is incomplete until you build ',
        'Seriously, just work on ']

types_of_apps = ['a social network', 'a dating website', 'a video game', 'a productivity app', 'a funding platform', 'a blogging platform', 'a knowledge sharing resource', 'a sperm bank']

companies = ['Facebook', 'YouTube', 'OK Cupid', 'Twitter', 'Tumblr', 'Google',
        'Stumble Upon', 'PayPal', 'Dropbox', 'LinkedIn', 'SoundCloud', 'eBay',
        'Kickstarter']

groups = ['old people', 'college students', 'musicians', 'pirates', 'ninjas', 'sex offenders',
        'metalheads', 'punks', 'neighborhoods', 'hipsters', 'hackers', 'teenagers',
        'sports fans', 'women', 'men', 'animals', 'animal lovers']

def generate_idea():
    option = randrange(0, 2, 1)
    if option == 0:
        return choice(phrasings) + choice(types_of_apps) + ' for ' + choice(groups)
    elif option == 1:
        return choice(phrasings) + choice(companies) + ' for ' + choice(groups)
    elif option == 2:
        return choice(phrasings) + choice(companies) + ' for ' + choice(companies)

print generate_idea()
