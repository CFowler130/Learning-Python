# Defining Score variables
x = 0
score = x

# Question One
print("What does HTML stand for?")
answer_1 = input("a)Hyper Techno Meteor Lounge\nb)Hippies Took My Lunch\nc)Hypertext Markup Language\nd)How To Make "
                 "Lasagna\n:")
if answer_1.lower() == "c":
    print("Correct")
    x = x + 1
else:
    print("InCoRrEcT, YoU ShOuLd kNoW BeTtEr")

# Question Two
print("What does RAM stand for?")
answer_2 = input("a)Retro Audio Module\nb)Random Access Memory\nc)Root Anchor Match\nd)Return Amongst Many\n:")
if answer_2.lower() == "b":
    print("Correct")
    x = x + 1
else:
    print("InCoRrEcT, YoU ShOuLd kNoW BeTtEr")

# Question Three
print("What does CPU stand for?")
answer_2 = input("a)Computer Programs Unlimited\nb)Central Processing Unit\nc)Charlie Papa Uniform\nd)Crypto Pirate "
                 "Umbrella\n:")
if answer_2.lower() == "b":
    print("Correct")
    x = x + 1
else:
    print("InCoRrEcT, YoU ShOuLd kNoW BeTtEr")

# Question Four
print("What does GPU stand for?")
answer_2 = input("a)Graphics Processing Unit\nb)Geek Program Unit\nc)Gremlins Push Under\nd)Gear Processing Unit\n:")
if answer_2.lower() == "a":
    print("Correct")
    x = x + 1
else:
    print("InCoRrEcT, YoU ShOuLd kNoW BeTtEr")

# Question Five
print("What does HDD stand for?")
answer_2 = input("a)Happy Dogs Dance\nb)Hurry Don't Dwell\nc)Hard Disk Drive\nd)Heavy Duty Delete\n:")
if answer_2.lower() == "c":
    print("Correct")
    x = x + 1
else:
    print("InCoRrEcT, YoU ShOuLd kNoW BeTtEr")

# Question Six
print("What does SSD stand for?")
answer_2 = input("a)Secret Squirrel Dance\nb)Solid State Drive\nc)Super Serial Damage\nd)Simple Syntax Document\n:")
if answer_2.lower() == "b":
    print("Correct")
    x = x + 1
else:
    print("InCoRrEcT, YoU ShOuLd kNoW BeTtEr")

# Question Seven
print("What does HDMI stand for?")
answer_2 = input("a)How Dummies Make Inventions\nb)Hubble Dark Movement Illustration\nc)Hacking Dox Malicious "
                 "Incident\nd)High-Definition Multimedia Interface\n:")
if answer_2.lower() == "d":
    print("Correct")
    x = x + 1
else:
    print("InCoRrEcT, YoU ShOuLd kNoW BeTtEr")

# Question Eight
print("What does DDR stand for?")
answer_2 = input("a)Double Data Rate\nb)Diffracted Duty Retention \nc)Dance Dance Revolution\nd)Defense Department "
                 "Revisions\n:")
if answer_2.lower() == "a":
    print("Correct")
    x = x + 1
else:
    print("InCoRrEcT, YoU ShOuLd kNoW BeTtEr")

# Question Nine
print("What does BIOS stand for?")
answer_2 = input("a)Beer Is Obviously Superior\nb)Basic Input-Output Services\nc)Bit Icon Option System\nd)Backup "
                 "Internet Online System\n:")
if answer_2.lower() == "b":
    print("Correct")
    x = x + 1
else:
    print("InCoRrEcT, YoU ShOuLd kNoW BeTtEr")

# Question Ten
print("What does DVI stand for?")
answer_2 = input("a)Double Viral Integer\nb)Desktop Virtual Interface\nc)Development Version Icon\nd)Digital Video "
                 "Interface\n:")
if answer_2.lower() == "d":
    print("Correct")
    x = x + 1
else:
    print("InCoRrEcT, YoU ShOuLd kNoW BeTtEr")

#Total Score
score = float(x / 10) * 100
print(x,"out of 10, that is",score, "%")
