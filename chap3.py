#3.4
guest_list=["Sigmond Frued", "adolf hilter", "albert hoffman"]
print("welcome to my house party Mr.",guest_list[0])
print("welcome to my house party Mr.",guest_list[1])
print("welcome to my house party Mr.",guest_list[2])
print("\n")

#3.5
guest_list=["Sigmond Frued", "adolf hilter", "albert hoffman"]
print("Mr.",guest_list[1],"couldn't make it to the party")
guest_list[1]="Osama Bin Laden" #cancelled due to WW2
print("welcome to my house party Mr.",guest_list[0])
print("welcome to my house party Mr.",guest_list[1])
print("welcome to my house party Mr.",guest_list[2])
print("\n")

#3.6
print("we just found a bigger table hance we gonna have some more guests to join")
print(guest_list)
guest_list.insert(0,"Elon musk") #inserts in the beginning
print(guest_list)
guest_list.insert(1,"Mike tyson") #insert in the
print(guest_list)
guest_list.append("Bruce Lee")
print(guest_list)
print("welcome to my house party Mr.",guest_list[0])
print("welcome to my house party Mr.",guest_list[1])
print("welcome to my house party Mr.",guest_list[2])
print("welcome to my house party Mr.",guest_list[3])
print("welcome to my house party Mr.",guest_list[4])
print("welcome to my house party Mr.",guest_list[5])
print("\n")

#3.7
print("Unfortunately we are informed that we can only have 2 seats therefore we have to filter our guest list")
print(guest_list.pop())
print(guest_list.pop())
print(guest_list.pop())
print(guest_list.pop())
print("the updated guest list is", guest_list)
print("welcome to my house party Mr.",guest_list[0])
print("welcome to my house party Mr.",guest_list[1])
print(guest_list.clear()) #clearing the list
print("\n")

#3.8
travel= ["iceland","columbia","mexico"]
print("Original order:",travel)
print("Alphabetical:",sorted(travel))
print("Original order:",travel)
print("list in reverse alphabetical order without changing the order of the original list",sorted(travel, reverse=True))
print("original list",travel)
print("\n")
print("Reversed:")
travel.reverse()
print(travel)

print("\nOriginal order:")
travel.reverse()
print(travel)

print("\nAlphabetical")
travel.sort()
print(travel)

print("\nReverse alphabetical")
travel.sort(reverse=True)
print(travel)
print("\n")

#3.9
guest_list=["Sigmond Frued", "adolf hilter", "albert hoffman"]
print("the number of guest coming to the party is",len(guest_list))
print("\n")

#3.10
hello_list= ["hey", "hi", "bye"]
print("original list", hello_list)
hello_list.append("good")
print("appended list", hello_list)
print("\n")

#insert - inserts value in the given indexes
hello_list.insert(0,"hate")
print("inserted list",hello_list)
print("\n")

#pop- removes the value from the list by giving it the index no and it also shows the item that has been removed by returning it
print(hello_list.pop(0))
print("\n")

#remove- just removes the value by providing the item/value to be deleted
hello_list.remove("hi")
print("after removing hi", hello_list)
print("\n")

#sort the lsit
print("without sort",hello_list)
hello_list.sort()
print("after sort",hello_list)
print("\n")

#reverse
print("without reverse",hello_list)
hello_list.reverse()
print("after reverse",hello_list)
print("\n")

#count
n=hello_list.count("hey")
print("count command tells hey is present",n)
print("\n")

#index
print(hello_list)
print("index of 'good' is ",hello_list.index("good"))
print("\n")

# clear command
print("before clearing the list",hello_list)
print("after clear command",hello_list.clear())




