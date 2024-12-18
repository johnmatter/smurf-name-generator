class SmurfNameGenerator:
    def __init__(self):
        self.smurf_num = 0  # Equivalent to SmurfNum in the original code
        self.total = 0      # Equivalent to x in the original code
        self.smurf_names = [
            "Macaroni", "Dr.", "Lil'", "Goodie Goodie Gumdrop", "Pinky", "Friendly", "Lovable", 
            "Sweet", "Count Smurfula", "Naughty", "Soggy Froggy", "Cookie", "Squeaky", "Chocolate", 
            "Vanilla", "Giggle", "Fuddy Duddy", "Coffee", "Chatty", "Boogie-Woogie", "Angelic", 
            "Devilish", "Happy", "Wise", "Curious", "Smelly", "Itty Bitty", "Late Night", "Ding-a-ling", 
            "Hocus Pocus", "Hacker", "Fancy Pants", "Ring-a-ding", "Gangsta", "Sir Smurfy", "Tickle", 
            "Rubber Ducky", "Summer", "Spooky", "Yum Yum", "Baby Cakes", "Phreaker", "Goofy", 
            "Sunshine", "Ol' Mac", "Sassafras", "Mr.", "Cupcake", "Wacky", "Sparkle", "Coconut", 
            "Smarty-Pants", "Squishy", "Grumpy", "Jelly Bean", "Mojo", "King", "Sneak-a-peek", 
            "Willy Wonka", "Clever", "Fluffer-Nutter", "Zippy", "Splendiferous", "Pizza", "Bubba", 
            "Sauve", "Snickers", "Wack-a-doo", "Jokester", "Munchy", "Bubble", "Trustworthy", 
            "Sticky", "Crunchy", "Root Beer", "Peanut Butter", "Marshmellow", "Smoochie", "Strawberry", 
            "Lemon", "Cola", "Scrub-a-dub", "Outlaw", "Sniffy", "Bashful", "Daisy", "Fuzzy", "Cuddly", 
            "Dreamy", "Shy", "Wonder", "Snuggle", "Spiffy", "Doodle", "Stinky", "Danger", "Robot", 
            "Snotty", "Karaoke", "Lucky", "Santa", "Party", "Noodle", "Artsy", "Racer", "Cracker Crumb", 
            "Speedy", "Puddin'", "Wiggle", "Klingon", "Retro", "Romantic", "Chef", "Funny", "Cheesy", 
            "Ditzy", "Snooty", "Slow-Poke", "Silly", "Rootin' Tootin'", "True Blue", "Mischievous", 
            "Playful", "Special Agent", "Cheeky Monkey", "Adventurous", "Sporty", "Mysterious", 
            "Fluffy", "Fishy", "Twinkle Toes", "Sci-Fi", "Professor", "Sushi", "Nutty", "Scaredy-Cat", 
            "Kissy Face", "Spontaneous", "Rebel", "Mystic", "Video Game", "Jitter Bug"
        ]

    def match_ltr(self, smurf_char):
        """
        Takes a character and updates smurf_num and total.
        For alpha characters: sets smurf_num to position (1-26)
        For non-alpha characters: keeps and adds previous value
        Always adds smurf_num to total.
        White space in the first and last names counts!
        """
        if 'a' <= smurf_char.lower() <= 'z':
            self.smurf_num = ord(smurf_char.lower()) - ord('a') + 1
        self.total += self.smurf_num

    def smurf_the_name(self, first_name, last_name):
        self.smurf_num = 0
        self.total = 0
        full_name = first_name + last_name

        for char in full_name:
            self.match_ltr(char)

        index = self.total % 90
        suffix = " Smurfette" if index == 78 else " Smurf"
        return self.smurf_names[index] + suffix