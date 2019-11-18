from operator import attrgetter, itemgetter
from random import choices
from unicodedata import normalize
from collections import defaultdict
import re

dig = re.compile('\d+')

class Rider:
    def __init__(self, name, nation, code, strength):
        self.name = name
        self.nation = nation
        self.code = code
        self.strength = strength
        self.points = 0
        self.palmares = []

    def __repr__(self):
        return f"Code: {self.code:<7}| Name: {self.name:<22} | Nat: {self.nation}  | Strength: {self.strength:<2} | Points: {self.points}"
 
    def __str__(self):
        return f"{self.name} is a rider from {self.nation}. He has accrued {self.points} points this year; is rated {self.strength}/10 in strength.\n\tHis Palmares:\n{chr(10).join(sorted(self.palmares, key = lambda x: int(dig.search(x).group())))}"
    
class Race:

    race_list = []
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.results = {}
        Race.race_list.append(self)

        if self.rating == 'HC':
            self.points_table = [250, 200, 160, 130, 110, 100, 90, 80, 70, 60, 50, 45, 40, 35, 30, 25, 20]
        elif self.rating == 'GT':
            self.points_table = [200, 160, 130, 110, 95, 85, 75, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
        elif self.rating == '2.2' or self.rating == 'HC.2':
            self.points_table = [150, 110, 90, 80, 70, 60, 50, 45, 40, 35, 30, 25, 20, 15, 10]
        elif self.rating == '2.1':
            self.points_table = [100, 80, 65, 55, 40, 30, 25, 20, 15, 12, 10, 7, 5]
        else:
            self.points_table = [75, 55, 40, 30, 25, 18, 13, 10, 8, 6, 4, 2]

    def __repr__(self):
        if self.results:
            return f"{self.name} is a class {self.rating} race. The winner was {riders[self.results[1]].name}. Also podiuming were {riders[self.results[2]].name} and {riders[self.results[3]].name}."
        else:
            return f"{self.name} is a class {self.rating} race. Has not been raced yet."


    def get_winner(self):
        "Function to run that actually simulates the race. It returns a dictionary {self.results} with keys starting from 1 and values as the riders' names in each place."
        
        if self.results:
            print(f'Already done {self.name}!')
            return
        
        winners = get_randy(len(self.points_table))
        
        self.results = {i: f for i, f in enumerate(winners, 1)}
        
        for index in range(len(winners)):
            riders[winners[index]].points += self.points_table[index]
        
        for placing, code in self.results.items():
            riders[code].palmares.append(f'Placed {placing} in {self.name} (worth {self.points_table[placing-1]} points)')

        print(f"Successfully simulated the {self.name}. Congratulations to {riders[self.results[1]].name} who won and added {self.points_table[0]} to his points total!")
        return winners

class StageRace(Race):

    def __init__(self, name, rating, length):
        super().__init__(name, rating)
        self.length = length
        self.stage_winners = {}
        self.gc_points = defaultdict(int)
        
        if self.rating == 'GT':
            self.stage_points_table = [150, 110, 90, 70, 60, 50, 40, 30, 25, 20, 15, 10, 5]
        elif self.rating == "HC.2":
            self.stage_points_table = [100, 85, 75, 65, 55, 45, 35, 25, 20, 15, 10]
        else:
            self.stage_points_table = [90, 70, 55, 40, 30, 20, 15, 10, 7, 3]

    def __repr__(self):
        if self.results:
            return f"{self.name} is a class {self.rating} race with {self.length} stages. The winner was {riders[self.results[1]].name}. Also podiuming were {riders[self.results[2]].name} and {riders[self.results[3]].name}. Stage winners were: {[riders[names[0]].name for names in self.stage_winners.values()]}"
        else:
            return f"{self.name} is a class {self.rating} race. Has not been raced yet."


    def get_winner(self):
        "Special version for StageRaces that runs {get_randy} on each stage separately. Then returns {results} dictionary with the overall placings"

        if self.results:
            print(f"Eh, lame. That's already been done before. {self.name}")
            return
        
        for stage_num in range(1, self.length + 1):
            self.stage_winners[stage_num] = randy2(len(self.stage_points_table))
            
            for i in range(len(self.stage_points_table)):
                riders[self.stage_winners[stage_num][i]].points += self.stage_points_table[i]
                self.gc_points[self.stage_winners[stage_num][i]] += self.stage_points_table[i]
                riders[self.stage_winners[stage_num][i]].palmares.append(f"Came in {i +1} place in stage {stage_num} of the {self.name}.")
            #print(f"Congragultations to {riders[self.stage_winners[stage_num][0]].name} for winning stage {stage_num} of the {self.name}!")

        self.results = {i: rider for i, rider in enumerate(sorted(self.gc_points, key = self.gc_points.get, reverse = True)[:len(self.points_table)], 1)}

        for i in range(len(self.points_table)):
            riders[sorted(self.gc_points, key = self.gc_points.get, reverse = True)[i]].points += self.points_table[i]
        
        for placing, code in self.results.items():
            riders[code].palmares.append(f'Placed {placing} in the overall GC in the {self.name} (worth {self.points_table[placing - 1]} points).')

        print(f"Successfully simulated the {self.name}. Congratulations to {riders[self.results[1]].name} who won and added {self.points_table[0]} to his points total!")            


def get_randy(n_places):
    "Helper function to be called by {get_winner}function. Output is a list of riders' codes same length as the {n_places} argument which should be an integer."

    winners = []
    while len(winners) < n_places:
        w = choices(list(riders), weights = [dude.strength for dude in riders.values()], k = 1).pop()
        if w not in winners:
            winners.append(w)

    return winners

def randy2(n):
    winners = choices(list(riders), weights = [dude.strength for dude in riders.values()], k = n)
    while len(set(winners)) != len(winners):
        winners = choices(list(riders), weights = [dude.strength for dude in riders.values()], k = n)
    return winners

def strip_accents(text):
    "Helper function for {populate_riders_dict}function to make riders codes ascii."
    text = normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode('utf-8')
    return str(text)

pcs_list = [('Peter Sagan', 'SK'), ('Elia Viviani', 'IT'), ('Julian Alaphilippe', 'FR'), ('Simon Yates', 'GB'), ('Tom Dumoulin', 'NL'), ('Thibaut Pinot', 'FR'), ('Primož Roglič', 'SI'), ('Geraint Thomas', 'GB'), ('Romain Bardet', 'FR'), ('Greg Van Avermaet', 'BE'), ('Miguel Ángel López', 'CO'), ('Tim Wellens', 'BE'), ('Michal Kwiatkowski', 'PL'), ('Michael Matthews', 'AU'), ('Arnaud Démare', 'FR'), ('Alexander Kristoff', 'NO'), ('Chris Froome', 'GB'), ('Nairo Quintana', 'CO'), ('Sonny Colbrelli', 'IT'), ('Ion Izagirre', 'ES'), ('Jasper Stuyven', 'BE'), ('Domenico Pozzovivo', 'IT'), ('Niki Terpstra', 'NL'), ('Pascal Ackermann', 'DE'), ('Alejandro Valverde', 'ES'), ('Bauke Mollema', 'NL'), ('Michael Valgren', 'DK'), ('Steven Kruijswijk', 'NL'), ('Egan Bernal', 'CO'), ('Jakob Fuglsang', 'DK'), ('Rohan Dennis', 'AU'), ('Oliver Naesen', 'BE'), ('Bob Jungels', 'LU'), ('Daniel Martin', 'IE'), ('Dylan Teuns', 'BE'), ('John Degenkolb', 'DE'), ('Rigoberto Urán', 'CO'), ('Gianni Moscon', 'IT'), ('Philippe Gilbert', 'BE'), ('Matej Mohorič', 'SI'), ('Vincenzo Nibali', 'IT'), ('Daryl Impey', 'ZA'), ('Tiesj Benoot', 'BE'), ('George Bennett', 'NZ'), ('Dylan Groenewegen', 'NL'), ('Adam Yates', 'GB'), ('Michael Woods', 'CA'), ('Christophe Laporte', 'FR'), ('Rafal Majka', 'PL'), ('Enric Mas', 'ES'), ('Mikel Landa', 'ES'), ('Pierre Latour', 'FR'), ('Richard Carapaz', 'EC'), ('Sam Bennett', 'IE'), ('Timothy Dupont', 'BE'), ('Diego Ulissi', 'IT'), ('Andrea Pasqualon', 'IT'), ('Eduard Prades', 'ES'), ('Maximilian Schachmann', 'DE'), ('Patrick Konrad', 'AT'), ('Emanuel Buchmann', 'DE'), ('Davide Formolo', 'IT'), ('Luis Leon-Sanchez', 'ES'), ('Richie Porte', 'AU'), ('Andre Greipel', 'DE'),  ('Danny Van-Poppel', 'NL'), ('Yves Lampaert', 'BE'), ('Gorka Izagirre', 'ES'), ('Wilco Kelderman', 'NL'), ('Edvald Boasson-Hagen', 'NO'), ('Sam Oomen', 'NL'), ('Damiano Caruso', 'IT'), ('Marc Soler', 'ES'), ('Zdeněk Štybar', 'CZ'), ('Caleb Ewan', 'AU'), ('Fabio Jakobsen', 'NL'), ('Mads Pedersen', 'DK'), ('Aleksey Lutsenko', 'KZ'), ('Fernando Gaviria', 'CO'), ('Søren Kragh-Andersen', 'DK'), ('Magnus Cort-Nielsen', 'DK'), ('Hugo Hofstetter', 'FR'), ('Roman Kreuziger', 'CZ'), ('Manuel Belletti', 'IT'), ('Rui Costa', 'PT'), ('Pello Bilbao', 'ES'), ('Sep Vanmarcke', 'BE'), ('Ilnur Zakarin', 'RU'), ('Wout Van-Aert', 'BE'), ('Matteo Trentin', 'IT'), ('Wout Poels', 'NL'), ('Ivan Ramiro-Sosa', 'CO'), ('David De-La-Cruz', 'ES'), ('Giacomo Nizzolo', 'IT'), ('Lilian Calmejane', 'FR'), ('Tejay Van-Garderen', 'US'), ('Guillaume Martin', 'FR'), ('Tony Gallopin', 'FR'), ('Álvaro-José Hodeg', 'CO'), ('Ben Hermans', 'BE')]

riders = {}

def populate_riders_dict(pcs_list):
    "'Pcs_List' is a list of tuples containing ({First-name Last-name}, {COUNTRY-CODE}) scraped from procyclingstats.com. Function populates 'riders' dictionary with a code as key, and creates a Rider class instance for each cyclist."
    added = 0
    
    for item in pcs_list:
        code = ''.join([item[0].split()[0][:2], item[0].split()[-1][:3]])
        if not code.isascii():
            code = strip_accents(code)
        try:
            assert(code not in riders.keys())
        except AssertionError:
            print(f"There is already a rider with '{code}' code in the peloton. {item} was not added.")
            continue

        if pcs_list.index(item) < 3:
            riders[code] = Rider(item[0], item[1], code, 11)
        elif pcs_list.index(item) <= len(pcs_list) * 0.1:
            riders[code] = Rider(item[0], item[1], code, 9)
        elif pcs_list.index(item) <= len(pcs_list) * 0.2:
            riders[code] = Rider(item[0], item[1], code, 8)
        elif pcs_list.index(item) <= len(pcs_list) * 0.33 :
            riders[code] = Rider(item[0], item[1], code, 7)
        elif pcs_list.index(item) <= len(pcs_list) * 0.5:
            riders[code] = Rider(item[0], item[1], code, 6)
        elif pcs_list.index(item) <= len(pcs_list) * 0.65:
            riders[code] = Rider(item[0], item[1], code, 5)
        elif pcs_list.index(item) <= len(pcs_list) * 0.8:
            riders[code] = Rider(item[0], item[1], code, 4)
        else:
            riders[code] = Rider(item[0], item[1], code, 3)
        
        added += 1
    return f"Successfully added {added} riders to the peloton. Current size is now {len(riders)}."

def current_ranking(number = 20):
    "Print top {number} riders ranked by total points. Number defaults to 20. 'None' argument will print the whole list."
    for r, rider in enumerate(sorted(riders.values(), key = attrgetter('points'), reverse = True)[:number], 1):
        print(f'{r:<3}| {repr(rider)[15:]}')


populate_riders_dict(pcs_list)

flanders = Race("Tour of Flanders", 'HC')
lomba = Race('Il Lombardia', '2.1')
p_r = Race('Paris-Roubaix', 'HC')
tds = Race('Tour de Suisse', 'PCT')
msr = Race('Milan-San Remo', 'HC')
sb = Race('Strade Bianche', '2.1')
vuelta = StageRace("La Vuelta a Espana", 'GT', 21)
tdf = StageRace('Le Tour de France', 'GT', 21)
giro = StageRace("Giro d'Italia", 'HC', 20)
ta = StageRace("Tirreno-Adriatico", 'HC.2', 7)
cali = StageRace('Tour of California', '2.2', 7)

def simulate_races():
    "Runs the function {self.get_winner} on each Race in {Race.race_list}."

    for race in Race.race_list:
        race.get_winner()

simulate_races()
current_ranking()