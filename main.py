from pyscript import display

Art_Club = {"Theresa", "Aimi", "BirthdayGuy", "Sylvia", "Monika"}
Glee_Club = {"Yuri", "Sylvia", "Monika", "BirthdayGuy"}

display(f'Students who are in clubs:', Art_Club.union(Glee_Club), target="display")
display(f'Students who are in the Art Club:', Art_Club, target="display")
display(f'Students who are in the Glee Club:', Glee_Club, target="display")
display(f'Students who are in one club:', Art_Club.difference(Glee_Club),Glee_Club.difference(Art_Club), target="display" )
display(f'Students who are in both clubs:', Art_Club.intersection(Glee_Club), target="display")
