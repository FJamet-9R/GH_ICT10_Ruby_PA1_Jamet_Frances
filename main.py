from pyscript import display

#summary
clubs = {"Guy1", "Guy2", "Guy3", "Guy4", "Guy5"}
clubs2 = {"Guy2", "Guy5"}
oneclub = {"Guy1", "Guy3"}
clubtwo = {"Guy4"}
oneclub = {"Guy1", "Guy3", "Guy4"}

All_Clubs = {"Theresa", "Aimi", "BirthdayGuy", "Yuri", "Sylvia", "Monika"}
Art_Club = {"Theresa", "Aimi", "BirthdayGuy"}
Glee_Club = {"Yuri", "Sylvia", "Monika"}
Both_Clubs = {"Sylvia", "Monika", "BirthdayGuy"}

display(f'Students who are in clubs:', Art_Club.union(Glee_Club), target="display")
display(f'Students who are in the Art Club:', Art_Club.union(Both_Clubs), target="display")
display(f'Students who are in the Glee Club:', Glee_Club.union(Both_Clubs), target="display")
display(f'Students who are in one club:', All_Clubs.difference(Both_Clubs), target="display" )
display(f'Students who are in both clubs:', Both_Clubs, target="display")