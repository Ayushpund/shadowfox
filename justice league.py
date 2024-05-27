justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

num_members = len(justice_league)
print("Number of members in the Justice League:", num_members)

justice_league.extend(["Batgirl", "Nightwing"])
print("Justice League after adding Batgirl and Nightwing:", justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Justice League after moving Wonder Woman to the beginning:", justice_league)

justice_league.remove("Superman")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Superman")
print("Justice League after moving Superman between Aquaman and Flash:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("Justice League after replacing with new members:", justice_league)

justice_league.sort()
print("Justice League after sorting alphabetically:", justice_league)

print("The new leader is:", justice_league[0])
