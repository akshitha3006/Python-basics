import array
set_a = {"Chips","Apples","Juice"}
set_b = {"Chips","Banana","Juice"}
set_a.add("Cookies")
shared_snacks = set_a.intersection(set_b)
print("Shared Snacks are: ",shared_snacks)

snack_counts = array.array('i', [10,20,15])
snack_counts.append(25)
snack_counts.insert(1, 12)
print("Count of 20s in array:", snack_counts.count(20))
snack_counts.reverse()
print("Reversed snack counts:", snack_counts)