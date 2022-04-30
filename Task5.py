def sort_str(s):
    split_arr = [i.upper().split(':') for i in s.split(';')]
    sorted_arr = sorted(split_arr, key=lambda x:(x[1], x[0]))
    return ''.join([f"({i[1]}, {i[0]})" for i in sorted_arr])


print(sort_str("Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))
