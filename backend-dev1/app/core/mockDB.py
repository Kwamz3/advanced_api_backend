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
    "description": "A computer hacker learns from mysterious rebels about the True nature of his reality and his role in the war against its controllers.",
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
    "phone": "+233-50-460-9878",
    "email": "jfigueroa@example.com",
    "firstName": "Michael",
    "lastName": "Jones",
    "role": "CLIENT",
    "status": "INACTIVE",
    "service": "PREMIUM_PLUS",
    "profilePicture": "https://picsum.photos/776/61",
    "dateOfbirth": "1976-10-31",
    "gender": "MALE",
    "bio": "Check example pretty key approach ground church one house others.",
    "location": {
      "lat": "30.642257",
      "lng": "150.455833"
    },
    "address": "35480 Cheryl Branch\nAllenborough, IN 16739",
    "isEmailVerified": "REJECTED",
    "isPhoneVerified": "PENDING",
    "preferences": {
      "theme": "light",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": False,
      "smsNotifications": True,
      "pushNotifications": True
    },
    "createdAt": "2025-11-24T12:50:06.264207",
    "updatedAt": "2025-11-24T12:50:06.264213"
  },
  {
    "id": "002",
    "phone": "+233-20-798-3291",
    "email": "jonesnicole@example.com",
    "firstName": "Dennis",
    "lastName": "Lutz",
    "role": "ADMIN",
    "status": "ACTIVE",
    "service": "PREMIUM",
    "profilePicture": "https://picsum.photos/97/115",
    "dateOfbirth": "1967-04-14",
    "gender": "MALE",
    "bio": "Stand both factor boy three sort bar ready discuss.",
    "location": {
      "lat": "81.646189",
      "lng": "18.699016"
    },
    "address": "98255 Bruce Shoal Suite 412\nRogerstown, ND 90475",
    "isEmailVerified": "NOT_SUBMITTED",
    "isPhoneVerified": "NOT_SUBMITTED",
    "preferences": {
      "theme": "dark",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": True,
      "pushNotifications": True
    },
    "createdAt": "2025-11-24T12:50:06.265086",
    "updatedAt": "2025-11-24T12:50:06.265090"
  },
  {
    "id": "003",
    "phone": "+233-23-911-5812",
    "email": "pedromurray@example.net",
    "firstName": "Veronica",
    "lastName": "Burgess",
    "role": "CLIENT",
    "status": "SUSPENDED",
    "service": "PREMIUM_PLUS",
    "profilePicture": "https://dummyimage.com/569x985",
    "dateOfbirth": "1991-08-29",
    "gender": "FEMALE",
    "bio": "Look record just note man available kid not social line.",
    "location": {
      "lat": "17.2769895",
      "lng": "-94.163715"
    },
    "address": "15992 Terry Ridges Apt. 134\nWest Russell, IN 17261",
    "isEmailVerified": "APPROVED",
    "isPhoneVerified": "APPROVED",
    "preferences": {
      "theme": "light",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": True,
      "pushNotifications": True
    },
    "createdAt": "2025-11-24T12:50:06.266010",
    "updatedAt": "2025-11-24T12:50:06.266014"
  },
  {
    "id": "004",
    "phone": "+233-24-809-2803",
    "email": "nmays@example.net",
    "firstName": "Aaron",
    "lastName": "Ray",
    "role": "TASKER",
    "status": "SUSPENDED",
    "service": "PREMIUM",
    "profilePicture": "https://dummyimage.com/421x842",
    "dateOfbirth": "1963-04-15",
    "gender": "MALE",
    "bio": "Fund beyond wide boy though station conference these rich from.",
    "location": {
      "lat": "60.5782385",
      "lng": "-18.910336"
    },
    "address": "7675 Brown Rest\nEast Jason, NM 55778",
    "isEmailVerified": "REJECTED",
    "isPhoneVerified": "REJECTED",
    "preferences": {
      "theme": "dark",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": False,
      "smsNotifications": False,
      "pushNotifications": False
    },
    "createdAt": "2025-11-24T12:50:06.266720",
    "updatedAt": "2025-11-24T12:50:06.266723"
  },
  {
    "id": "005",
    "phone": "+233-54-244-2980",
    "email": "mporter@example.com",
    "firstName": "Heather",
    "lastName": "Kelly",
    "role": "TASKER",
    "status": "SUSPENDED",
    "service": "PREMIUM",
    "profilePicture": "https://placekitten.com/187/234",
    "dateOfbirth": "1980-11-11",
    "gender": "FEMALE",
    "bio": "Accept hard various conference here address model choice lay quality.",
    "location": {
      "lat": "-29.8803735",
      "lng": "-116.029759"
    },
    "address": "696 Nicole Overpass\nThompsonville, DC 05267",
    "isEmailVerified": "NOT_SUBMITTED",
    "isPhoneVerified": "APPROVED",
    "preferences": {
      "theme": "light",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": False,
      "smsNotifications": False,
      "pushNotifications": True
    },
    "createdAt": "2025-11-24T12:50:06.267456",
    "updatedAt": "2025-11-24T12:50:06.267460"
  },
  {
    "id": "006",
    "phone": "+233-27-436-6960",
    "email": "dboyd@example.org",
    "firstName": "Amy",
    "lastName": "Wilson",
    "role": "TASKER",
    "status": "ACTIVE",
    "service": "PREMIUM_PLUS",
    "profilePicture": "https://placekitten.com/849/729",
    "dateOfbirth": "1989-08-26",
    "gender": "RATHER_NOT_SAY",
    "bio": "During step own type fish audience evidence property our rich western radio.",
    "location": {
      "lat": "-64.0076745",
      "lng": "-136.702135"
    },
    "address": "1323 Reese Forest Apt. 834\nEast Andrea, NE 11497",
    "isEmailVerified": "APPROVED",
    "isPhoneVerified": "NOT_SUBMITTED",
    "preferences": {
      "theme": "light",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": False,
      "smsNotifications": True,
      "pushNotifications": True
    },
    "createdAt": "2025-11-24T12:50:06.268143",
    "updatedAt": "2025-11-24T12:50:06.268147"
  },
  {
    "id": "007",
    "phone": "+233-20-838-5642",
    "email": "hannah62@example.net",
    "firstName": "Melissa",
    "lastName": "White",
    "role": "TASKER",
    "status": "INACTIVE",
    "service": "PREMIUM",
    "profilePicture": "https://placekitten.com/514/749",
    "dateOfbirth": "1965-04-08",
    "gender": "NOT_SELECTED",
    "bio": "View hard speech education evening go drug series large choose general PM give contain keep fact.",
    "location": {
      "lat": "-52.6228695",
      "lng": "-19.402825"
    },
    "address": "67394 Hall Ferry Apt. 398\nLake Tara, UT 90969",
    "isEmailVerified": "NOT_SUBMITTED",
    "isPhoneVerified": "PENDING",
    "preferences": {
      "theme": "dark",
      "language": "en"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": False,
      "pushNotifications": False
    },
    "createdAt": "2025-11-24T12:50:06.268802",
    "updatedAt": "2025-11-24T12:50:06.268805"
  },
  {
    "id": "008",
    "phone": "+233-54-307-3056",
    "email": "elizabethmoore@example.org",
    "firstName": "Jacob",
    "lastName": "Ramirez",
    "role": "ADMIN",
    "status": "SUSPENDED",
    "service": "PREMIUM_PLUS",
    "profilePicture": "https://dummyimage.com/613x427",
    "dateOfbirth": "1997-03-22",
    "gender": "MALE",
    "bio": "Anything stay receive science store soldier relate within.",
    "location": {
      "lat": "-76.8606685",
      "lng": "-64.037914"
    },
    "address": "2022 Joshua Courts Apt. 838\nPort Nicole, WI 90265",
    "isEmailVerified": "APPROVED",
    "isPhoneVerified": "APPROVED",
    "preferences": {
      "theme": "light",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": False,
      "smsNotifications": True,
      "pushNotifications": False
    },
    "createdAt": "2025-11-24T12:50:06.269580",
    "updatedAt": "2025-11-24T12:50:06.269584"
  },
  {
    "id": "009",
    "phone": "+233-24-304-7910",
    "email": "nancymcclain@example.net",
    "firstName": "Hannah",
    "lastName": "Payne",
    "role": "CLIENT",
    "status": "ACTIVE",
    "service": "FREE",
    "profilePicture": "https://placekitten.com/606/172",
    "dateOfbirth": "1969-01-31",
    "gender": "RATHER_NOT_SAY",
    "bio": "Suffer single tell building wife you then for outside produce.",
    "location": {
      "lat": "-79.409332",
      "lng": "158.492886"
    },
    "address": "37348 Kennedy Crossing\nWest David, AR 90939",
    "isEmailVerified": "APPROVED",
    "isPhoneVerified": "PENDING",
    "preferences": {
      "theme": "dark",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": False,
      "smsNotifications": False,
      "pushNotifications": True
    },
    "createdAt": "2025-11-24T12:50:06.270340",
    "updatedAt": "2025-11-24T12:50:06.270344"
  },
  {
    "id": "010",
    "phone": "+233-54-759-9029",
    "email": "sean57@example.com",
    "firstName": "Tiffany",
    "lastName": "Young",
    "role": "TASKER",
    "status": "SUSPENDED",
    "service": "FREE",
    "profilePicture": "https://picsum.photos/142/752",
    "dateOfbirth": "1977-03-27",
    "gender": "NOT_SELECTED",
    "bio": "Child bad drug appear prove public stay open also director same view minute manager director yet.",
    "location": {
      "lat": "-61.1882275",
      "lng": "67.776991"
    },
    "address": "9092 Courtney Crest Suite 283\nLake Omarhaven, IL 80734",
    "isEmailVerified": "REJECTED",
    "isPhoneVerified": "PENDING",
    "preferences": {
      "theme": "dark",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": False,
      "pushNotifications": False
    },
    "createdAt": "2025-11-24T12:50:06.270976",
    "updatedAt": "2025-11-24T12:50:06.270979"
  },
  {
    "id": "011",
    "phone": "+233-54-990-3206",
    "email": "colleensmith@example.com",
    "firstName": "Brooke",
    "lastName": "Miller",
    "role": "TASKER",
    "status": "SUSPENDED",
    "service": "PREMIUM",
    "profilePicture": "https://placekitten.com/420/190",
    "dateOfbirth": "1965-08-31",
    "gender": "FEMALE",
    "bio": "Those us drop pull collection fly commercial give professional nice us build cover animal next have.",
    "location": {
      "lat": "44.5786035",
      "lng": "-162.117485"
    },
    "address": "5497 Gilmore Bypass Apt. 416\nAdrienneshire, CT 22672",
    "isEmailVerified": "APPROVED",
    "isPhoneVerified": "REJECTED",
    "preferences": {
      "theme": "light",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": False,
      "pushNotifications": False
    },
    "createdAt": "2025-11-24T12:50:06.271736",
    "updatedAt": "2025-11-24T12:50:06.271740"
  },
  {
    "id": "012",
    "phone": "+233-20-485-2543",
    "email": "nicoleball@example.org",
    "firstName": "Melinda",
    "lastName": "Cooper",
    "role": "TASKER",
    "status": "ACTIVE",
    "service": "FREE",
    "profilePicture": "https://dummyimage.com/8x455",
    "dateOfbirth": "1984-12-04",
    "gender": "FEMALE",
    "bio": "Success with father beautiful degree give have federal someone among book wide here job.",
    "location": {
      "lat": "79.790066",
      "lng": "64.207261"
    },
    "address": "26208 James Expressway Suite 722\nSouth Michaelborough, MT 35807",
    "isEmailVerified": "REJECTED",
    "isPhoneVerified": "REJECTED",
    "preferences": {
      "theme": "dark",
      "language": "en"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": True,
      "pushNotifications": True
    },
    "createdAt": "2025-11-24T12:50:06.272481",
    "updatedAt": "2025-11-24T12:50:06.272485"
  },
  {
    "id": "013",
    "phone": "+233-50-566-9975",
    "email": "jennifer67@example.org",
    "firstName": "Eric",
    "lastName": "Alexander",
    "role": "ADMIN",
    "status": "INACTIVE",
    "service": "PREMIUM",
    "profilePicture": "https://dummyimage.com/996x187",
    "dateOfbirth": "1984-03-04",
    "gender": "MALE",
    "bio": "Certain item community rise type standard health.",
    "location": {
      "lat": "-77.6904355",
      "lng": "157.715459"
    },
    "address": "USNS Harris\nFPO AP 69830",
    "isEmailVerified": "APPROVED",
    "isPhoneVerified": "NOT_SUBMITTED",
    "preferences": {
      "theme": "light",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": False,
      "smsNotifications": True,
      "pushNotifications": True
    },
    "createdAt": "2025-11-24T12:50:06.273019",
    "updatedAt": "2025-11-24T12:50:06.273023"
  },
  {
    "id": "014",
    "phone": "+233-59-547-6154",
    "email": "ryan50@example.org",
    "firstName": "Michael",
    "lastName": "Meyers",
    "role": "ADMIN",
    "status": "INACTIVE",
    "service": "PREMIUM",
    "profilePicture": "https://dummyimage.com/807x736",
    "dateOfbirth": "2000-07-09",
    "gender": "MALE",
    "bio": "Himself scene among sit guy point now pull parent contain activity finish bank court degree.",
    "location": {
      "lat": "85.316912",
      "lng": "-100.637538"
    },
    "address": "21277 Samantha Neck Suite 720\nDavisshire, FM 08201",
    "isEmailVerified": "APPROVED",
    "isPhoneVerified": "APPROVED",
    "preferences": {
      "theme": "light",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": False,
      "pushNotifications": False
    },
    "createdAt": "2025-11-24T12:50:06.273865",
    "updatedAt": "2025-11-24T12:50:06.273868"
  },
  {
    "id": "015",
    "phone": "+233-59-271-6703",
    "email": "theresa16@example.net",
    "firstName": "Jennifer",
    "lastName": "White",
    "role": "ADMIN",
    "status": "INACTIVE",
    "service": "FREE",
    "profilePicture": "https://dummyimage.com/412x771",
    "dateOfbirth": "1981-03-14",
    "gender": "FEMALE",
    "bio": "Catch tell administration drop full perform break week deep wrong direction money side across.",
    "location": {
      "lat": "67.4960905",
      "lng": "-119.645570"
    },
    "address": "069 Campbell Fork Apt. 762\nDanielfurt, NY 02556",
    "isEmailVerified": "APPROVED",
    "isPhoneVerified": "PENDING",
    "preferences": {
      "theme": "light",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": False,
      "pushNotifications": True
    },
    "createdAt": "2025-11-24T12:50:06.274563",
    "updatedAt": "2025-11-24T12:50:06.274566"
  },
  {
    "id": "016",
    "phone": "+233-20-444-5307",
    "email": "nelsonstephanie@example.net",
    "firstName": "Jennifer",
    "lastName": "Brown",
    "role": "ADMIN",
    "status": "ACTIVE",
    "service": "PREMIUM_PLUS",
    "profilePicture": "https://placekitten.com/792/62",
    "dateOfbirth": "1962-05-23",
    "gender": "FEMALE",
    "bio": "Beyond cover safe cause national public choice say need she.",
    "location": {
      "lat": "-47.3366305",
      "lng": "-118.395846"
    },
    "address": "71549 Norris Walks Apt. 030\nLaurahaven, LA 65336",
    "isEmailVerified": "PENDING",
    "isPhoneVerified": "NOT_SUBMITTED",
    "preferences": {
      "theme": "dark",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": False,
      "smsNotifications": False,
      "pushNotifications": False
    },
    "createdAt": "2025-11-24T12:50:06.275393",
    "updatedAt": "2025-11-24T12:50:06.275396"
  },
  {
    "id": "017",
    "phone": "+233-20-160-7063",
    "email": "katie72@example.com",
    "firstName": "Mallory",
    "lastName": "Swanson",
    "role": "CLIENT",
    "status": "ACTIVE",
    "service": "PREMIUM_PLUS",
    "profilePicture": "https://dummyimage.com/872x355",
    "dateOfbirth": "1988-11-24",
    "gender": "RATHER_NOT_SAY",
    "bio": "Draw position sure easy on economy relate before.",
    "location": {
      "lat": "81.203346",
      "lng": "137.572299"
    },
    "address": "06549 Flowers Groves\nSouth Elizabeth, NV 05540",
    "isEmailVerified": "PENDING",
    "isPhoneVerified": "APPROVED",
    "preferences": {
      "theme": "light",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": False,
      "pushNotifications": True
    },
    "createdAt": "2025-11-24T12:50:06.276095",
    "updatedAt": "2025-11-24T12:50:06.276098"
  },
  {
    "id": "018",
    "phone": "+233-20-623-2931",
    "email": "dcox@example.org",
    "firstName": "Brandon",
    "lastName": "Andrews",
    "role": "TASKER",
    "status": "ACTIVE",
    "service": "PREMIUM_PLUS",
    "profilePicture": "https://dummyimage.com/931x858",
    "dateOfbirth": "1993-03-13",
    "gender": "MALE",
    "bio": "Southern join create mouth must growth expect wide drug may appear put staff girl decade.",
    "location": {
      "lat": "75.4481665",
      "lng": "-20.360215"
    },
    "address": "6322 Erica Shoals Apt. 120\nPort James, AK 14413",
    "isEmailVerified": "PENDING",
    "isPhoneVerified": "REJECTED",
    "preferences": {
      "theme": "dark",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": False,
      "pushNotifications": True
    },
    "createdAt": "2025-11-24T12:50:06.276742",
    "updatedAt": "2025-11-24T12:50:06.276745"
  },
  {
    "id": "019",
    "phone": "+233-59-880-5727",
    "email": "rhondacummings@example.net",
    "firstName": "Maria",
    "lastName": "Daniels",
    "role": "ADMIN",
    "status": "INACTIVE",
    "service": "PREMIUM",
    "profilePicture": "https://placekitten.com/151/380",
    "dateOfbirth": "1970-10-10",
    "gender": "NOT_SELECTED",
    "bio": "Artist half religious first order degree despite write field might affect.",
    "location": {
      "lat": "-80.5208455",
      "lng": "136.323983"
    },
    "address": "8274 Jones Lakes\nOrozcoview, NC 01497",
    "isEmailVerified": "PENDING",
    "isPhoneVerified": "NOT_SUBMITTED",
    "preferences": {
      "theme": "dark",
      "language": "es"
    },
    "notificationSettings": {
      "emailNotifications": True,
      "smsNotifications": True,
      "pushNotifications": True
    },
    "createdAt": "2025-11-24T12:50:06.277757",
    "updatedAt": "2025-11-24T12:50:06.277760"
  },
  {
    "id": "020",
    "phone": "+233-20-518-2062",
    "email": "fweaver@example.com",
    "firstName": "Jose",
    "lastName": "Martin",
    "role": "ADMIN",
    "status": "SUSPENDED",
    "service": "PREMIUM",
    "profilePicture": "https://placekitten.com/620/51",
    "dateOfbirth": "1994-03-18",
    "gender": "MALE",
    "bio": "Change their establish performance stock hold reality wish strategy.",
    "location": {
      "lat": "-74.236170",
      "lng": "30.295528"
    },
    "address": "831 Bradford Springs Apt. 366\nMichelleton, MD 98432",
    "isEmailVerified": "PENDING",
    "isPhoneVerified": "REJECTED",
    "preferences": {
      "theme": "dark",
      "language": "fr"
    },
    "notificationSettings": {
      "emailNotifications": False,
      "smsNotifications": True,
      "pushNotifications": False
    },
    "createdAt": "2025-11-24T12:50:06.278422",
    "updatedAt": "2025-11-24T12:50:06.278426"
  }
]
