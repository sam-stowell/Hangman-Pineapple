# Define a dictionary to store words for each category
categories = {
    "Fruit": ["apple", "banana", "orange", "grape", "strawberry", "pineapple", "watermelon", "kiwi", "mango", "peach",
              "pear", "blueberry", "raspberry", "blackberry", "cherry", "lemon", "lime", "coconut", "avocado",
              "pomegranate", "fig", "plum", "apricot", "guava", "papaya", "passionfruit", "dragonfruit", "cranberry",
              "cantaloupe", "honeydew", "nectarine", "tangerine", "lychee", "grapefruit", "kiwifruit", "persimmon",
              "starfruit", "mulberry", "rhubarb", "gooseberry", "kumquat", "boysenberry", "loganberry", "elderberry",
              "quince", "soursop", "plantain", "durian"],
    "Cities": ["London", "Paris", "New York", "Tokyo", "Sydney", "Rome", "Los Angeles", "Beijing", "Berlin", "Moscow",
               "Istanbul", "Bangkok", "Mexico City", "Cairo", "Dubai", "Madrid", "Toronto", "Seoul", "Singapore",
               "Mumbai", "Shanghai", "Rio de Janeiro", "Chicago", "Hong Kong", "Buenos Aires", "Kolkata", "Delhi",
               "Osaka", "San Francisco", "Washington D.C.", "Amsterdam", "Vienna", "Stockholm", "Athens", "Prague",
               "Brussels", "Budapest", "Lisbon", "Warsaw", "Dublin", "Copenhagen", "Helsinki", "Wellington",
               "Canberra", "Ottawa", "Nairobi", "Zurich", "Geneva", "Auckland", "Brasília", "Panama City"],
    "Books": ["Dune", "Sherlock", "Harry Potter", "Lord of the Rings", "The Great Gatsby", "To Kill a Mockingbird",
              "1984", "Pride and Prejudice", "The Catcher in the Rye", "The Hobbit", "The Bible", "The Alchemist",
              "Moby-Dick", "War and Peace", "Anna Karenina", "Crime and Punishment", "Great Expectations", "The Odyssey",
              "Don Quixote", "One Hundred Years of Solitude", "The Lord of the Flies", "The Picture of Dorian Gray",
              "Frankenstein", "Wuthering Heights", "Les Misérables", "The Count of Monte Cristo", "Dracula",
              "Gulliver's Travels", "A Tale of Two Cities", "The Scarlet Letter", "Alice's Adventures in Wonderland",
              "The Adventures of Tom Sawyer", "Robinson Crusoe", "Treasure Island", "Little Women", "Gone with the Wind",
              "The Chronicles of Narnia", "The Three Musketeers", "Emma", "Jane Eyre", "The Sound and the Fury",
              "The Brothers Karamazov", "Sense and Sensibility", "Oliver Twist", "The War of the Worlds",
              "The Canterbury Tales", "Walden", "Around the World in Eighty Days", "Grimm's Fairy Tales"],
    "Famous People": ["Albert Einstein", "Leonardo da Vinci", "Nelson Mandela", "William Shakespeare", "Mother Teresa",
                      "Michael Jordan", "Abraham Lincoln", "Mahatma Gandhi", "Martin Luther King Jr.", "Winston Churchill",
                      "Adolf Hitler", "George Washington", "Steve Jobs", "Pablo Picasso", "Vincent van Gogh",
                      "Cleopatra", "Marie Curie", "Charles Darwin", "Galileo Galilei", "Isaac Newton", "Marilyn Monroe",
                      "Elvis Presley", "John F. Kennedy", "Queen Elizabeth II", "Napoleon Bonaparte", "Christopher Columbus",
                      "Alexander the Great", "Leon Trotsky", "Frida Kahlo", "Amelia Earhart", "Thomas Edison",
                      "Charles Dickens", "Walt Disney", "Stephen Hawking", "Sigmund Freud", "John Lennon", "Rosa Parks",
                      "Muhammad Ali", "Neil Armstrong", "Albert Schweitzer", "Benjamin Franklin", "Marlon Brando",
                      "Bob Dylan", "J.K. Rowling", "David Bowie", "Oprah Winfrey", "Pope Francis", "Dalai Lama"],
    "Countries": ["United States", "China", "India", "Brazil", "Russia", "Australia", "Canada", "Argentina", "Mexico",
                  "Indonesia", "Pakistan", "Nigeria", "Bangladesh", "Japan", "Ethiopia", "Philippines", "Egypt",
                  "Vietnam", "DR Congo", "Turkey", "Iran", "Germany", "Thailand", "United Kingdom", "France", "Italy",
                  "South Africa", "Tanzania", "Myanmar", "South Korea", "Colombia", "Kenya", "Spain", "Ukraine",
                  "Argentina", "Algeria", "Poland", "Sudan", "Uganda", "Morocco", "Saudi Arabia", "Uzbekistan",
                  "Peru", "Malaysia", "Angola", "Ghana", "Yemen", "Nepal", "Venezuela"]
}
'''
# Print the number of words in each category
for category, words in categories.items():
    print(f"{category}: {len(words)} words")
'''