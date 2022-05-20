import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# pierwsza zmienna wejsciowa = zgodnosc z opisem
compliance_with_the_description = ctrl.Antecedent(np.arange(0, 6), 'compliance_with_the_description (rate 0-5)')

# druga zmienna wejsciowa = czas wysylki (maksymalne 30 dni, ustalamy ze osoba sprzedaje produkt w tym samym kraju)
shipping_time = ctrl.Antecedent(np.arange(0, 31), 'shipping_time (days 0-30)')

# trzecia zmienna wejsciowa = koszty wysylki
shipping_cost = ctrl.Antecedent(np.arange(0, 101), 'shipping_cost (cost 0-100)')

# czwarta zmienna wyjsciowa = kontakt ze sprzedawca
contact_with_the_seller = ctrl.Antecedent(np.arange(0, 6), 'contact_with_the_seller (rate 0-5)')

# zmienna wyjsciowa = ocena zamowienia
evaluation_of_the_order = ctrl.Consequent(np.arange(0, 11), 'evaluation_of_the_order (rate 0-10)')

# funkcje przynaleznosci do pierwszej zmiennej wejsciowej (zgodnosc z opisem)
compliance_with_the_description['LOW'] = fuzz.trapmf(compliance_with_the_description.universe, [0, 0, 1, 2])
compliance_with_the_description['MEDIUM'] = fuzz.trimf(compliance_with_the_description.universe, [1, 2, 4])
compliance_with_the_description['HIGH'] = fuzz.trapmf(compliance_with_the_description.universe, [2, 4, 5, 5])
compliance_with_the_description.view()

# funkcje przynaleznosci do drugiej zmiennej wejsciowej (czas wysylki)
shipping_time['FAST'] = fuzz.trapmf(shipping_time.universe, [0, 0, 1, 2])
shipping_time['MEDIUM'] = fuzz.trimf(shipping_time.universe, [1, 3, 5])
shipping_time['LONG'] = fuzz.trapmf(shipping_time.universe, [3, 5, 15, 30])
shipping_time.view()

# funkcje przynaleznosci do trzeciej zmiennej wejsciowej (cena wysylki)
shipping_cost['LOW'] = fuzz.trapmf(shipping_cost.universe, [0, 0, 6, 12])
shipping_cost['MEDIUM'] = fuzz.trimf(shipping_cost.universe, [6, 12, 20])
shipping_cost['HIGH'] = fuzz.trapmf(shipping_cost.universe, [20, 50, 75, 100])
shipping_cost.view()

# funkcje przynaleznosci do czwartej zmiennej wejsciowej (kontakt ze sprzedawca)
contact_with_the_seller['POOR'] = fuzz.trapmf(contact_with_the_seller.universe, [0, 0, 1, 2])
contact_with_the_seller['MEDIUM'] = fuzz.trimf(contact_with_the_seller.universe, [1, 2, 3])
contact_with_the_seller['GOOD'] = fuzz.trapmf(contact_with_the_seller.universe, [2, 3, 5, 5])
contact_with_the_seller.view()

# funkcje przynaleznosci do zmiennej wyjsciowej
evaluation_of_the_order['UNACCEPTABLE'] = fuzz.trapmf(evaluation_of_the_order.universe, [0, 0, 2, 4])
evaluation_of_the_order['ACCEPTABLE'] = fuzz.trimf(evaluation_of_the_order.universe, [2, 4, 6])
evaluation_of_the_order['GOOD'] = fuzz.trimf(evaluation_of_the_order.universe, [4, 6, 8])
evaluation_of_the_order['VERY_GOOD'] = fuzz.trapmf(evaluation_of_the_order.universe, [7, 8, 10, 10])
evaluation_of_the_order.view()

# lista regul przynaleznosci
list_of_affiliation_rules = []
"Compliance_with_the_description"

# compliance_with_the_description['LOW']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))

# compliance_with_the_description['MEDIUM']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['ACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['ACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['ACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['ACCEPTABLE']))

# compliance_with_the_description['HIGH']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['ACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['ACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['ACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['ACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['ACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['ACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['GOOD']))

"shipping time"
# shipping_time['LONG']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['ACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['ACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))

# shipping_time['MEDIUM']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['ACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))

# shipping_time['FAST']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))
"shipping_cost"
# shipping_cost['HIGH']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['ACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))

# shipping_cost['MEDIUM']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['ACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))

# shipping_cost['LOW']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))
"contact_with_the_seller"
# contact_with_the_seller['MEDIUM']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))

# contact_with_the_seller['GOOD']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['VERY_GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))
"double medium"
# compliance_with_the_description'MEDIUM'] & shipping_time['MEDIUM']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['GOOD']))

# compliance_with_the_description['MEDIUM'] & shipping_cost['MEDIUM']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['FAST'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['GOOD']))

# compliance_with_the_description['MEDIUM'] & contact_with_the_seller['MEDIUM']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))

# contact_with_the_seller['MEDIUM'] & shipping_time['MEDIUM']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))

# contact_with_the_seller['MEDIUM'] & shipping_cost['MEDIUM']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))

# shipping_cost['MEDIUM'] & shipping_time['MEDIUM']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))



"double high"
# compliance_with_the_description'HIGH'] & shipping_time['FAST']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['VERY_GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['VERY_GOOD']))

# compliance_with_the_description['HIGH'] & shipping_cost['LOW']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['VERY_GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['VERY_GOOD']))

# compliance_with_the_description['HIGH'] & contact_with_the_seller['GOOD']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['VERY_GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['VERY_GOOD']))

# contact_with_the_seller['GOOD'] & shipping_time['MEDIUM']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['VERY_GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))

# contact_with_the_seller['GOOD'] & shipping_cost['LOW']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['VERY_GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))

# shipping_cost['LOW'] & shipping_time['FAST']
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['VERY_GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))

"triple medium"
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['MEDIUM'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['LONG'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['FAST'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['UNACCEPTABLE']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['MEDIUM'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['VERY_GOOD']))

"triple high"
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['POOR'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['MEDIUM'], evaluation_of_the_order['VERY_GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['VERY_GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['HIGH'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['VERY_GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['FAST'] & shipping_cost['MEDIUM'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['VERY_GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['LONG'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['HIGH'] & shipping_time['MEDIUM'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['VERY_GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['MEDIUM'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['GOOD']))
list_of_affiliation_rules.append(ctrl.Rule(compliance_with_the_description['LOW'] & shipping_time['FAST'] & shipping_cost['LOW'] &
                                           contact_with_the_seller['GOOD'], evaluation_of_the_order['UNACCEPTABLE']))

# definiujemy sterownik rozmyty
order_ev_ctrl = ctrl.ControlSystem(list_of_affiliation_rules)
# symulacja działania sterownika
order_ev_simulation = ctrl.ControlSystemSimulation(order_ev_ctrl)
# ustalamy wejście ostre (crisp)
order_ev_simulation.input['compliance_with_the_description (rate 0-5)'] = 5
order_ev_simulation.input['shipping_time (days 0-30)'] = 1
order_ev_simulation.input['shipping_cost (cost 0-100)'] = 5
order_ev_simulation.input['contact_with_the_seller (rate 0-5)'] = 5

order_ev_simulation.compute()
evaluation_of_the_order.view(sim=order_ev_simulation)
print(order_ev_simulation.output['evaluation_of_the_order (rate 0-10)'])
order_ev_ctrl.view()
plt.show()



