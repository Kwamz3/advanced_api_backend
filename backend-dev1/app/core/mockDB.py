from typing import List, Optional
from app.models.users import UserStatus, UserRole, GenderStatus, ServiceStatus,VerifyEmail, VerifyPhone


movies_db = [
  {
    "id": "001",
    "title": "The Shawshank Redemption",
    "category": "Drama",
    "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
    "poster_url": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
    "trailer_url": "https://youtube.com/watch?v=6hB3S9bIaco",
    "duration": 142,
    "release_year": 1994,
    "rating": 9.3,
    "cast": "Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler",
    "producer": "Frank Darabont",
    "views": 2847596,
    "created_at": "2025-11-06T19:41:56.895036",
    "updated_at": "2025-11-06T19:41:56.895043",
    "is_liked": True
  },
  {
    "id": "002",
    "title": "The Dark Knight",
    "category": "Action",
    "description": "When the menace known as the Joker wreaks havoc on Gotham, Batman must accept one of the greatest psychological and physical tests to fight injustice.",
    "poster_url": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
    "trailer_url": "https://youtube.com/watch?v=EXeTwQWrcwY",
    "duration": 152,
    "release_year": 2008,
    "rating": 9.0,
    "cast": "Christian Bale, Heath Ledger, Aaron Eckhart, Michael Caine",
    "producer": "Christopher Nolan",
    "views": 3204568,
    "created_at": "2025-11-06T19:41:56.895840",
    "updated_at": "2025-11-06T19:41:56.895844",
    "is_liked": True
  },
  {
    "id": "003",
    "title": "The Lord of the Rings: The Return of the King",
    "category": "Fantasy",
    "description": "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
    "poster_url": "https://image.tmdb.org/t/p/w500/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg",
    "trailer_url": "https://youtube.com/watch?v=r7EHCsJ0dEU",
    "duration": 201,
    "release_year": 2003,
    "rating": 8.9,
    "cast": "Elijah Wood, Viggo Mortensen, Ian McKellen, Orlando Bloom",
    "producer": "Peter Jackson",
    "views": 2863865,
    "created_at": "2025-11-06T19:41:56.896260",
    "updated_at": "2025-11-06T19:41:56.896264",
    "is_liked": True
  },
  {
    "id": "004",
    "title": "Inception",
    "category": "Sci-Fi",
    "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
    "poster_url": "https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg",
    "trailer_url": "https://youtube.com/watch?v=YoHD9XEInc0",
    "duration": 148,
    "release_year": 2010,
    "rating": 8.8,
    "cast": "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy",
    "producer": "Christopher Nolan",
    "views": 4175717,
    "created_at": "2025-11-06T19:41:56.896761",
    "updated_at": "2025-11-06T19:41:56.896764",
    "is_liked": True
  },
  {
    "id": "005",
    "title": "The Matrix",
    "category": "Sci-Fi",
    "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
    "poster_url": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
    "trailer_url": "https://youtube.com/watch?v=vKQi3bBA1y8",
    "duration": 136,
    "release_year": 1999,
    "rating": 8.7,
    "cast": "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving",
    "producer": "The Wachowskis",
    "views": 3987942,
    "created_at": "2025-11-06T19:41:56.897405",
    "updated_at": "2025-11-06T19:41:56.897408",
    "is_liked": True
  },
  {
    "id": "006",
    "title": "The Lord of the Rings: The Fellowship of the Ring",
    "category": "Fantasy",
    "description": "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.",
    "poster_url": "https://image.tmdb.org/t/p/w500/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg",
    "trailer_url": "https://youtube.com/watch?v=V75dMMIW2B4",
    "duration": 178,
    "release_year": 2001,
    "rating": 8.8,
    "cast": "Elijah Wood, Ian McKellen, Orlando Bloom, Sean Bean",
    "producer": "Peter Jackson",
    "views": 2813676,
    "created_at": "2025-11-06T19:41:56.898003",
    "updated_at": "2025-11-06T19:41:56.898006",
    "is_liked": True
  },
  {
    "id": "007",
    "title": "The Silence of the Lambs",
    "category": "Thriller",
    "description": "A young FBI cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer.",
    "poster_url": "https://image.tmdb.org/t/p/w500/uS9m8OBk1A8eM9I042bx8XXpqAq.jpg",
    "trailer_url": "https://youtube.com/watch?v=W6Mm8Sbe__o",
    "duration": 118,
    "release_year": 1991,
    "rating": 8.6,
    "cast": "Jodie Foster, Anthony Hopkins, Scott Glenn, Ted Levine",
    "producer": "Jonathan Demme",
    "views": 1891203,
    "created_at": "2025-11-06T19:41:56.898544",
    "updated_at": "2025-11-06T19:41:56.898550",
    "is_liked": True
  },
  {
    "id": "008",
    "title": "Interstellar",
    "category": "Sci-Fi",
    "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
    "poster_url": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
    "trailer_url": "https://youtube.com/watch?v=zSWdZVtXT7E",
    "duration": 169,
    "release_year": 2014,
    "rating": 8.6,
    "cast": "Matthew McConaughey, Anne Hathaway, Jessica Chastain, Michael Caine",
    "producer": "Christopher Nolan",
    "views": 3538318,
    "created_at": "2025-11-06T19:41:56.899574",
    "updated_at": "2025-11-06T19:41:56.899578",
    "is_liked": True
  },
  {
    "id": "009",
    "title": "Forrest Gump",
    "category": "Drama",
    "description": "The presidencies of Kennedy and Johnson, the Vietnam War, and other historical events unfold from the perspective of an Alabama man with an IQ of 75.",
    "poster_url": "https://image.tmdb.org/t/p/w500/saHP97rTPS5eLmrLQEcANmKrsFl.jpg",
    "trailer_url": "https://youtube.com/watch?v=bLvqoHBptjg",
    "duration": 142,
    "release_year": 1994,
    "rating": 8.8,
    "cast": "Tom Hanks, Robin Wright, Gary Sinise, Sally Field",
    "producer": "Robert Zemeckis",
    "views": 3932040,
    "created_at": "2025-11-06T19:41:56.900015",
    "updated_at": "2025-11-06T19:41:56.900018",
    "is_liked": True
  },
  {
    "id": "010",
    "title": "Gladiator",
    "category": "Action",
    "description": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
    "poster_url": "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg",
    "trailer_url": "https://youtube.com/watch?v=owK1qxDselE",
    "duration": 155,
    "release_year": 2000,
    "rating": 8.5,
    "cast": "Russell Crowe, Joaquin Phoenix, Connie Nielsen, Oliver Reed",
    "producer": "Ridley Scott",
    "views": 2744137,
    "created_at": "2025-11-06T19:41:56.900665",
    "updated_at": "2025-11-06T19:41:56.900668",
    "is_liked": True
  },
  {
    "id": "011",
    "title": "Spirited Away",
    "category": "Animation",
    "description": "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits where humans are changed into beasts.",
    "poster_url": "https://image.tmdb.org/t/p/w500/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
    "trailer_url": "https://youtube.com/watch?v=ByXuk9QqQkk",
    "duration": 125,
    "release_year": 2001,
    "rating": 8.6,
    "cast": "Rumi Hiiragi, Miyu Irino, Mari Natsuki, Takashi Naitō",
    "producer": "Hayao Miyazaki",
    "views": 1917624,
    "created_at": "2025-11-06T19:41:56.901099",
    "updated_at": "2025-11-06T19:41:56.901102",
    "is_liked": True
  },
  {
    "id": "012",
    "title": "Parasite",
    "category": "Thriller",
    "description": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
    "poster_url": "https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg",
    "trailer_url": "https://youtube.com/watch?v=5xH0HfJHsaY",
    "duration": 132,
    "release_year": 2019,
    "rating": 8.6,
    "cast": "Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong, Choi Woo-shik",
    "producer": "Bong Joon-ho",
    "views": 2872466,
    "created_at": "2025-11-06T19:41:56.902053",
    "updated_at": "2025-11-06T19:41:56.902056",
    "is_liked": True
  },
  {
    "id": "013",
    "title": "The Departed",
    "category": "Thriller",
    "description": "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.",
    "poster_url": "https://image.tmdb.org/t/p/w500/nT97ifVT2J1yMQmeq20Qblg61T.jpg",
    "trailer_url": "https://youtube.com/watch?v=iojhqm0JTW4",
    "duration": 151,
    "release_year": 2006,
    "rating": 8.5,
    "cast": "Leonardo DiCaprio, Matt Damon, Jack Nicholson, Mark Wahlberg",
    "producer": "Martin Scorsese",
    "views": 2583240,
    "created_at": "2025-11-06T19:41:56.902517",
    "updated_at": "2025-11-06T19:41:56.902520",
    "is_liked": True
  },
  {
    "id": "014",
    "title": "Pulp Fiction",
    "category": "Thriller",
    "description": "The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption.",
    "poster_url": "https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg",
    "trailer_url": "https://youtube.com/watch?v=s7EdQ4FqbhY",
    "duration": 154,
    "release_year": 1994,
    "rating": 8.9,
    "cast": "John Travolta, Uma Thurman, Samuel L. Jackson, Bruce Willis",
    "producer": "Quentin Tarantino",
    "views": 3316379,
    "created_at": "2025-11-06T19:41:56.903104",
    "updated_at": "2025-11-06T19:41:56.903107",
    "is_liked": True
  },
  {
    "id": "015",
    "title": "The Godfather",
    "category": "Drama",
    "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    "poster_url": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
    "trailer_url": "https://youtube.com/watch?v=sY1S34973zA",
    "duration": 175,
    "release_year": 1972,
    "rating": 9.2,
    "cast": "Marlon Brando, Al Pacino, James Caan, Diane Keaton",
    "producer": "Francis Ford Coppola",
    "views": 4282294,
    "created_at": "2025-11-06T19:41:56.903570",
    "updated_at": "2025-11-06T19:41:56.903573",
    "is_liked": True
  },
  {
    "id": "016",
    "title": "Schindler's List",
    "category": "Drama",
    "description": "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution.",
    "poster_url": "https://image.tmdb.org/t/p/w500/sF1U4EUQS8YHUYjNl3pMGNIQyr0.jpg",
    "trailer_url": "https://youtube.com/watch?v=gG22XNhtnoY",
    "duration": 195,
    "release_year": 1993,
    "rating": 8.9,
    "cast": "Liam Neeson, Ralph Fiennes, Ben Kingsley, Caroline Goodall",
    "producer": "Steven Spielberg",
    "views": 2231386,
    "created_at": "2025-11-06T19:41:56.904522",
    "updated_at": "2025-11-06T19:41:56.904525",
    "is_liked": True
  },
  {
    "id": "017",
    "title": "WALL-E",
    "category": "Animation",
    "description": "In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
    "poster_url": "https://image.tmdb.org/t/p/w500/hbhFnRzzg6ZDmm8YAmxBnQpQIPh.jpg",
    "trailer_url": "https://youtube.com/watch?v=CZ1CATNbXg0",
    "duration": 98,
    "release_year": 2008,
    "rating": 8.4,
    "cast": "Ben Burtt, Elissa Knight, Jeff Garlin, Fred Willard",
    "producer": "Andrew Stanton",
    "views": 2023335,
    "created_at": "2025-11-06T19:41:56.905118",
    "updated_at": "2025-11-06T19:41:56.905122",
    "is_liked": True
  },
  {
    "id": "018",
    "title": "The Green Mile",
    "category": "Drama",
    "description": "The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder who has a mysterious gift.",
    "poster_url": "https://image.tmdb.org/t/p/w500/velWPhVMQeQKcxggNEU8YmIo52R.jpg",
    "trailer_url": "https://youtube.com/watch?v=Ki4haFrqSrw",
    "duration": 189,
    "release_year": 1999,
    "rating": 8.6,
    "cast": "Tom Hanks, Michael Clarke Duncan, David Morse, Bonnie Hunt",
    "producer": "Frank Darabont",
    "views": 2175462,
    "created_at": "2025-11-06T19:41:56.906063",
    "updated_at": "2025-11-06T19:41:56.906066",
    "is_liked": True
  },
  {
    "id": "019",
    "title": "Django Unchained",
    "category": "Drama",
    "description": "With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.",
    "poster_url": "https://image.tmdb.org/t/p/w500/7oWY8VDWW7thTzWh3OKYRkWUlD5.jpg",
    "trailer_url": "https://youtube.com/watch?v=eUdM9vrCbow",
    "duration": 165,
    "release_year": 2012,
    "rating": 8.4,
    "cast": "Jamie Foxx, Christoph Waltz, Leonardo DiCaprio, Kerry Washington",
    "producer": "Quentin Tarantino",
    "views": 2910868,
    "created_at": "2025-11-06T19:41:56.907014",
    "updated_at": "2025-11-06T19:41:56.907017",
    "is_liked": True
  },
  {
    "id": "020",
    "title": "The Prestige",
    "category": "Drama",
    "description": "After a tragic accident, two stage magicians engage in a battle to create the ultimate illusion while sacrificing everything they have to outwit each other.",
    "poster_url": "https://image.tmdb.org/t/p/w500/tRNlZbgNCNOpLpbPEz5L8G8A0JN.jpg",
    "trailer_url": "https://youtube.com/watch?v=o4gHCmTQDVI",
    "duration": 130,
    "release_year": 2006,
    "rating": 8.5,
    "cast": "Christian Bale, Hugh Jackman, Scarlett Johansson, Michael Caine",
    "producer": "Christopher Nolan",
    "views": 1986523,
    "created_at": "2025-11-06T19:41:56.907801",
    "updated_at": "2025-11-06T19:41:56.907804",
    "is_liked": True
  }
]

user_db = [
  {
    "id": "001",
    "phone": "+233-24-682-3277",
    "email": "jessicasmall@example.com",
    "firstName": "Kimberly",
    "lastName": "Carson",
    "role": UserRole.CLIENT,
    "status": UserStatus.SUSPENDED,
    "service": ServiceStatus.PREMIUM,
    "profilePicture": "https://dummyimage.com/674x299",
    "dateOfbirth": "1989-04-15",
    "gender": GenderStatus.RATHER_NOT_SAY,
    "bio": "Choice fear heavy he travel language rather whom as early yourself.",
    "location": {
      "lat": "8.806164",
      "lng": "-110.508311"
    },
    "address": "51900 Monica Hill\nVaughnshire, VT 72276",
    "isEmailVerified": VerifyEmail.PENDING,
    "isPhoneVerified": VerifyPhone.REJECTED,
    "preferences": {
      "theme": "dark",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": True,
      "pushNotifications": True
    },
    "createdAt": "2025-11-05T16:40:54.569721",
    "updatedAt": "2025-11-05T16:40:54.569727"
  },
  {
    "id": "002",
    "phone": "+233-20-628-3360",
    "email": "danajones@example.com",
    "firstName": "Erin",
    "lastName": "Hernandez",
    "role": UserRole.ADMIN,
    "status": UserStatus.ACTIVE,
    "service": ServiceStatus.FREE,
    "profilePicture": "https://picsum.photos/137/248",
    "dateOfbirth": "1983-02-26",
    "gender": GenderStatus.NOT_SELECTED,
    "bio": "Even strong smile other others key herself economy rule apply poor need truth heart.",
    "location": {
      "lat": "61.184431",
      "lng": "-7.381318"
    },
    "address": "611 Jefferson Island\nPort Dominicmouth, LA 01799",
    "isEmailVerified": VerifyEmail.REJECTED,
    "isPhoneVerified": VerifyPhone.PENDING,
    "preferences": {
      "theme": "light",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": False,
      "pushNotifications": False
    },
    "createdAt": "2025-11-05T16:40:54.571410",
    "updatedAt": "2025-11-05T16:40:54.571417"
  },
  {
    "id": "003",
    "phone": "+233-20-103-4610",
    "email": "kparker@example.org",
    "firstName": "Carla",
    "lastName": "Torres",
    "role": UserRole.CLIENT,
    "status": UserStatus.ACTIVE,
    "service": ServiceStatus.PREMIUM,
    "profilePicture": "https://dummyimage.com/224x505",
    "dateOfbirth": "1966-01-06",
    "gender": GenderStatus.FEMALE,
    "bio": "Office quite agreement source business want ten most memory want pay I mission partner task head.",
    "location": {
      "lat": "21.414355",
      "lng": "51.814855"
    },
    "address": "PSC 5286, Box 8298\nAPO AE 31226",
    "isEmailVerified": VerifyEmail.APPROVED,
    "isPhoneVerified": VerifyPhone.PENDING,
    "preferences": {
      "theme": "light",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": True,
      "pushNotifications": False
    },
    "createdAt": "2025-11-05T16:40:54.572220",
    "updatedAt": "2025-11-05T16:40:54.572224"
  },
  {
    "id": "004",
    "phone": "+233-24-614-4288",
    "email": "ytate@example.com",
    "firstName": "Amanda",
    "lastName": "Davis",
    "role": UserRole.ADMIN,
    "status": UserStatus.SUSPENDED,
    "service": ServiceStatus.PREMIUM_PLUS,
    "profilePicture": "https://picsum.photos/370/138",
    "dateOfbirth": "1987-03-20",
    "gender": GenderStatus.NOT_SELECTED,
    "bio": "And office class themselves station argue western.",
    "location": {
      "lat": "-4.520859",
      "lng": "48.620901"
    },
    "address": "20655 Philip Inlet\nMarquezberg, OH 42133",
    "isEmailVerified": VerifyEmail.APPROVED,
    "isPhoneVerified": VerifyPhone.REJECTED,
    "preferences": {
      "theme": "light",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": False,
      "smsNotifications": True,
      "pushNotifications": False
    },
    "createdAt": "2025-11-05T16:40:54.573159",
    "updatedAt": "2025-11-05T16:40:54.573164"
  },
  {
    "id": "005",
    "phone": "+233-27-423-5345",
    "email": "brooksshaun@example.net",
    "firstName": "Jessica",
    "lastName": "Hamilton",
    "role": UserRole.TASKER,
    "status": UserStatus.INACTIVE,
    "service": ServiceStatus.PREMIUM_PLUS,
    "profilePicture": "https://picsum.photos/950/531",
    "dateOfbirth": "1960-08-05",
    "gender": GenderStatus.NOT_SELECTED,
    "bio": "Republican Mrs item example room good yourself skill fact.",
    "location": {
      "lat": "20.575970",
      "lng": "-156.863325"
    },
    "address": "64908 Christine Plaza Suite 096\nToddmouth, AS 94804",
    "isEmailVerified": VerifyEmail.PENDING,
    "isPhoneVerified": VerifyEmail.NOT_SUBMITTED,
    "preferences": {
      "theme": "light",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": False,
      "smsNotifications": True,
      "pushNotifications": False
    },
    "createdAt": "2025-11-05T16:40:54.574125",
    "updatedAt": "2025-11-05T16:40:54.574129"
  },
  {
    "id": "c10ab939-f4dc-4772-96b2-6e912f3d35c1",
    "phone": "+233-50-613-4725",
    "email": "todd41@example.org",
    "firstName": "Ashley",
    "lastName": "Santiago",
    "role": UserRole.ADMIN,
    "status": UserStatus.SUSPENDED,
    "service": ServiceStatus.PREMIUM,
    "profilePicture": "https://picsum.photos/914/488",
    "dateOfbirth": "1970-06-23",
    "gender": GenderStatus.FEMALE,
    "bio": "Three see main family make trade employee idea.",
    "location": {
      "lat": "85.8743775",
      "lng": "93.066492"
    },
    "address": "7106 Taylor Club Suite 104\nConleyshire, CA 59160",
    "isEmailVerified": VerifyEmail.NOT_SUBMITTED,
    "isPhoneVerified": VerifyEmail.PENDING,
    "preferences": {
      "theme": "dark",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": False,
      "smsNotifications": True,
      "pushNotifications": True
    },
    "createdAt": "2025-11-05T16:40:54.575061",
    "updatedAt": "2025-11-05T16:40:54.575066"
  },
  {
    "id": "70076334-3178-4f7a-a38b-7815b0bd2add",
    "phone": "+233-26-817-5910",
    "email": "rodriguezkevin@example.org",
    "firstName": "Tara",
    "lastName": "Delacruz",
    "role": UserRole.ADMIN,
    "status": UserStatus.SUSPENDED,
    "service": ServiceStatus.PREMIUM,
    "profilePicture": "https://dummyimage.com/364x780",
    "dateOfbirth": "1988-01-26",
    "gender": GenderStatus.NOT_SELECTED,
    "bio": "Peace recently east decision job north past nation force challenge.",
    "location": {
      "lat": "72.3807625",
      "lng": "59.395536"
    },
    "address": "35937 Jacqueline Meadow Suite 077\nNicholastown, VI 41689",
    "isEmailVerified": VerifyEmail.PENDING,
    "isPhoneVerified": VerifyEmail.APPROVED,
    "preferences": {
      "theme": "light",
      "language": "en"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": False,
      "pushNotifications": False
    },
    "createdAt": "2025-11-05T16:40:54.576042",
    "updatedAt": "2025-11-05T16:40:54.576046"
  },
  {
    "id": "fb95ce74-c8b9-4e59-9946-93c3ad903989",
    "phone": "+233-20-205-4995",
    "email": "alison74@example.com",
    "firstName": "Savannah",
    "lastName": "Shelton",
    "role": UserRole.TASKER,
    "status": UserStatus.INACTIVE,
    "service": ServiceStatus.PREMIUM,
    "profilePicture": "https://placekitten.com/4/647",
    "dateOfbirth": "1989-01-20",
    "gender": GenderStatus.FEMALE,
    "bio": "Onto election conference whole heart ok war according key me indicate audience product act.",
    "location": {
      "lat": "76.829261",
      "lng": "-153.792289"
    },
    "address": "527 Dunn Prairie\nWest Michaelmouth, WI 90797",
    "isEmailVerified": VerifyEmail.PENDING,
    "isPhoneVerified": VerifyPhone.REJECTED,
    "preferences": {
      "theme": "light",
      "language": "en"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": False,
      "pushNotifications": False
    },
    "createdAt": "2025-11-05T16:40:54.576892",
    "updatedAt": "2025-11-05T16:40:54.576896"
  },
  {
    "id": "009",
    "phone": "+233-57-717-2859",
    "email": "castroshelley@example.org",
    "firstName": "Kenneth",
    "lastName": "Baldwin",
    "role": UserRole.CLIENT,
    "status": UserStatus.INACTIVE,
    "service": ServiceStatus.FREE,
    "profilePicture": "https://dummyimage.com/389x738",
    "dateOfbirth": "1963-07-16",
    "gender": GenderStatus.MALE,
    "bio": "Few style need physical fly something page.",
    "location": {
      "lat": "-85.8401145",
      "lng": "-137.351158"
    },
    "address": "1886 Sarah Plains Suite 423\nEast Sheena, WI 81693",
    "isEmailVerified": VerifyEmail.PENDING,
    "isPhoneVerified": VerifyEmail.PENDING,
    "preferences": {
      "theme": "dark",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": False,
      "pushNotifications": True
    },
    "createdAt": "2025-11-05T16:40:54.577872",
    "updatedAt": "2025-11-05T16:40:54.577876"
  },
  {
    "id": "d8c63aaf-945d-43d6-9576-d1986023f217",
    "phone": "+233-59-319-1821",
    "email": "bbennett@example.net",
    "firstName": "Lindsey",
    "lastName": "Macdonald",
    "role": UserRole.ADMIN,
    "status": UserStatus.SUSPENDED,
    "service": ServiceStatus.FREE,
    "profilePicture": "https://dummyimage.com/311x851",
    "dateOfbirth": "1956-01-14",
    "gender": GenderStatus.RATHER_NOT_SAY,
    "bio": "Product attack attack standard while movie pretty reason Democrat news appear.",
    "location": {
      "lat": "79.911333",
      "lng": "-61.513735"
    },
    "address": "254 Austin Row Apt. 663\nSouth Michael, AZ 89056",
    "isEmailVerified": VerifyPhone.REJECTED,
    "isPhoneVerified": VerifyPhone.REJECTED,
    "preferences": {
      "theme": "light",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": False,
      "pushNotifications": True
    },
    "createdAt": "2025-11-05T16:40:54.578740",
    "updatedAt": "2025-11-05T16:40:54.578745"
  },
  {
    "id": "17c3cd40-ce34-4ed6-bd7e-c4166494b201",
    "phone": "+233-55-572-4485",
    "email": "andrescarpenter@example.com",
    "firstName": "Denise",
    "lastName": "Nelson",
    "role": UserRole.CLIENT,
    "status": UserStatus.SUSPENDED,
    "service": ServiceStatus.FREE,
    "profilePicture": "https://placekitten.com/535/663",
    "dateOfbirth": "1985-07-28",
    "gender": GenderStatus.NOT_SELECTED,
    "bio": "Write agency top skill or those place important.",
    "location": {
      "lat": "67.972944",
      "lng": "149.805184"
    },
    "address": "75654 Rice Canyon\nEast Nicole, OH 93937",
    "isEmailVerified": VerifyPhone.REJECTED,
    "isPhoneVerified": VerifyEmail.APPROVED,
    "preferences": {
      "theme": "dark",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": True,
      "pushNotifications": True
    },
    "createdAt": "2025-11-05T16:40:54.579759",
    "updatedAt": "2025-11-05T16:40:54.579763"
  },
  {
    "id": "b0632b50-15c7-40f5-9aec-5b603f4f00c3",
    "phone": "+233-20-310-6855",
    "email": "hmiller@example.org",
    "firstName": "Kim",
    "lastName": "White",
    "role": UserRole.TASKER,
    "status": UserStatus.SUSPENDED,
    "service": ServiceStatus.PREMIUM,
    "profilePicture": "https://placekitten.com/602/309",
    "dateOfbirth": "1966-01-11",
    "gender": GenderStatus.NOT_SELECTED,
    "bio": "Break skin whom rest country whom next act tell change.",
    "location": {
      "lat": "1.2000095",
      "lng": "114.965582"
    },
    "address": "33121 Rebecca Crest\nLake Christopherbury, ME 92069",
    "isEmailVerified": VerifyEmail.PENDING,
    "isPhoneVerified": VerifyEmail.APPROVED,
    "preferences": {
      "theme": "dark",
      "language": "en"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": False,
      "pushNotifications": False
    },
    "createdAt": "2025-11-05T16:40:54.582225",
    "updatedAt": "2025-11-05T16:40:54.582236"
  },
  {
    "id": "f43083d5-4f1e-47d9-a1ae-2587fe76aeaa",
    "phone": "+233-23-682-3397",
    "email": "patriciapalmer@example.org",
    "firstName": "Anna",
    "lastName": "Ford",
    "role": UserRole.TASKER,
    "status": UserStatus.ACTIVE,
    "service": ServiceStatus.PREMIUM,
    "profilePicture": "https://placekitten.com/831/387",
    "dateOfbirth": "1990-12-30",
    "gender": GenderStatus.NOT_SELECTED,
    "bio": "Whether pretty minute contain maintain series break three knowledge school but else player plant over.",
    "location": {
      "lat": "-7.1412385",
      "lng": "-59.609381"
    },
    "address": "95890 Ashley Estate Apt. 347\nJohnfurt, NH 97519",
    "isEmailVerified": VerifyPhone.REJECTED,
    "isPhoneVerified": VerifyEmail.APPROVED,
    "preferences": {
      "theme": "light",
      "language": "en"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": False,
      "pushNotifications": False
    },
    "createdAt": "2025-11-05T16:40:54.583778",
    "updatedAt": "2025-11-05T16:40:54.583784"
  },
  {
    "id": "014",
    "phone": "+233-20-626-2824",
    "email": "amanda42@example.com",
    "firstName": "Destiny",
    "lastName": "Liu",
    "role": UserRole.TASKER,
    "status": UserStatus.ACTIVE,
    "service": ServiceStatus.FREE,
    "profilePicture": "https://dummyimage.com/615x634",
    "dateOfbirth": "1980-02-28",
    "gender": GenderStatus.RATHER_NOT_SAY,
    "bio": "Difference citizen watch level only should cultural form this politics not college leader.",
    "location": {
      "lat": "55.1908235",
      "lng": "147.849630"
    },
    "address": "3899 Stephen Burg Apt. 196\nHensleybury, MO 77518",
    "isEmailVerified": VerifyEmail.APPROVED,
    "isPhoneVerified": VerifyPhone.REJECTED,
    "preferences": {
      "theme": "dark",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": False,
      "smsNotifications": True,
      "pushNotifications": False
    },
    "createdAt": "2025-11-05T16:40:54.584952",
    "updatedAt": "2025-11-05T16:40:54.584957"
  },
  {
    "id": "015",
    "phone": "+233-27-322-0206",
    "email": "ashleymartinez@example.com",
    "firstName": "Maria",
    "lastName": "Benson",
    "role": UserRole.ADMIN,
    "status": UserStatus.INACTIVE,
    "service": ServiceStatus.PREMIUM,
    "profilePicture": "https://placekitten.com/96/371",
    "dateOfbirth": "1978-08-11",
    "gender": GenderStatus.RATHER_NOT_SAY,
    "bio": "Home week occur know law actually party say or stop manage interview.",
    "location": {
      "lat": "13.9466605",
      "lng": "72.006275"
    },
    "address": "00149 Mejia Terrace Apt. 847\nPort Brent, CT 98540",
    "isEmailVerified": VerifyEmail.NOT_SUBMITTED,
    "isPhoneVerified": VerifyEmail.PENDING,
    "preferences": {
      "theme": "light",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": True,
      "pushNotifications": True
    },
    "createdAt": "2025-11-05T16:40:54.586035",
    "updatedAt": "2025-11-05T16:40:54.586039"
  },
  {
    "id": "4a4551a2-658f-407d-8d14-4690e924bf43",
    "phone": "+233-23-331-4044",
    "email": "walter93@example.org",
    "firstName": "Heather",
    "lastName": "Pope",
    "role": UserRole.ADMIN,
    "status": UserStatus.ACTIVE,
    "service": ServiceStatus.FREE,
    "profilePicture": "https://picsum.photos/401/995",
    "dateOfbirth": "1992-04-23",
    "gender": GenderStatus.NOT_SELECTED,
    "bio": "Pull world forward manager miss information matter every relate protect artist trial.",
    "location": {
      "lat": "58.803478",
      "lng": "165.043151"
    },
    "address": "5333 Williams Meadows Suite 812\nPort Richardton, CA 26596",
    "isEmailVerified": VerifyEmail.PENDING,
    "isPhoneVerified": VerifyPhone.REJECTED,
    "preferences": {
      "theme": "light",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": False,
      "smsNotifications": False,
      "pushNotifications": True
    },
    "createdAt": "2025-11-05T16:40:54.586891",
    "updatedAt": "2025-11-05T16:40:54.586895"
  },
  {
    "id": "ceabe13e-135e-4baa-9fb3-569cf891b503",
    "phone": "+233-23-36-3296",
    "email": "shawnellis@example.com",
    "firstName": "Martha",
    "lastName": "Smith",
    "role": UserRole.CLIENT,
    "status": UserStatus.SUSPENDED,
    "service": ServiceStatus.FREE,
    "profilePicture": "https://picsum.photos/815/957",
    "dateOfbirth": "1983-11-29",
    "gender": GenderStatus.FEMALE,
    "bio": "Including speak face throw listen system analysis fall among animal push around fine none president.",
    "location": {
      "lat": "70.2919765",
      "lng": "-90.342151"
    },
    "address": "1801 Donna Fork\nJohnsontown, NM 67304",
    "isEmailVerified": VerifyEmail.NOT_SUBMITTED,
    "isPhoneVerified": VerifyEmail.PENDING,
    "preferences": {
      "theme": "dark",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": True,
      "pushNotifications": False
    },
    "createdAt": "2025-11-05T16:40:54.587861",
    "updatedAt": "2025-11-05T16:40:54.587865"
  },
  {
    "id": "28ac1971-913c-4c57-86fe-c9c24f4a4165",
    "phone": "+233-23-211-8077",
    "email": "ronaldlopez@example.net",
    "firstName": "Elizabeth",
    "lastName": "West",
    "role": UserRole.TASKER,
    "status": UserStatus.INACTIVE,
    "service": ServiceStatus.PREMIUM_PLUS,
    "profilePicture": "https://placekitten.com/828/68",
    "dateOfbirth": "2007-03-22",
    "gender": GenderStatus.RATHER_NOT_SAY,
    "bio": "Arm hard number long his north affect future usually series good field vote.",
    "location": {
      "lat": "65.0742705",
      "lng": "-90.347163"
    },
    "address": "020 Smith Fall Apt. 104\nNorth Biancahaven, PR 67520",
    "isEmailVerified": VerifyEmail.PENDING,
    "isPhoneVerified": VerifyEmail.PENDING,
    "preferences": {
      "theme": "dark",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": True,
      "pushNotifications": False
    },
    "createdAt": "2025-11-05T16:40:54.588846",
    "updatedAt": "2025-11-05T16:40:54.588851"
  },
  {
    "id": "364592dc-0506-4a3c-b616-d5fb93269b0f",
    "phone": "+233-59-797-5386",
    "email": "thomashiggins@example.net",
    "firstName": "Brent",
    "lastName": "Burnett",
    "role": UserRole.CLIENT,
    "status": UserStatus.SUSPENDED,
    "service": ServiceStatus.PREMIUM_PLUS,
    "profilePicture": "https://dummyimage.com/726x217",
    "dateOfbirth": "1994-05-09",
    "gender": GenderStatus.MALE,
    "bio": "Nearly and responsibility research religious this we suffer.",
    "location": {
      "lat": "-0.459702",
      "lng": "82.964145"
    },
    "address": "110 Matthew Vista\nNorth Tamara, ND 08564",
    "isEmailVerified": VerifyEmail.APPROVED,
    "isPhoneVerified": VerifyEmail.PENDING,
    "preferences": {
      "theme": "dark",
      "language": "en"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": True,
      "pushNotifications": True
    },
    "createdAt": "2025-11-05T16:40:54.589798",
    "updatedAt": "2025-11-05T16:40:54.589802"
  },
  {
    "id": "020",
    "phone": "+233-26-86-3894",
    "email": "robert74@example.com",
    "firstName": "Carrie",
    "lastName": "Drake",
    "role": UserRole.CLIENT,
    "status": UserStatus.INACTIVE,
    "service": ServiceStatus.PREMIUM,
    "profilePicture": "https://placekitten.com/667/336",
    "dateOfbirth": "1964-01-10",
    "gender": GenderStatus.RATHER_NOT_SAY,
    "bio": "Assume data tell blood station lot whatever most certain people yeah yes force top.",
    "location": {
      "lat": "78.7825075",
      "lng": "78.820564"
    },
    "address": "11388 Garrett Locks Apt. 339\nToddland, MA 56536",
    "isEmailVerified": VerifyEmail.NOT_SUBMITTED,
    "isPhoneVerified": VerifyEmail.PENDING,
    "preferences": {
      "theme": "light",
      "language": "en"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": True,
      "pushNotifications": False
    },
    "createdAt": "2025-11-05T16:40:54.590597",
    "updatedAt": "2025-11-05T16:40:54.590601"
  }
]
