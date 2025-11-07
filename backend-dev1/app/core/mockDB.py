from typing import List, Optional
from app.models.user import UserStatus, UserRole, GenderStatus, ServiceStatus,VerifyEmail, VerifyPhone


movies_db = [
  {
    "id": "b41d1c53-f2d4-43d3-83b7-a5984137a725",
    "title": "Innovative bandwidth-monitored pricing structure",
    "category": "Thriller",
    "description": "Get single I affect rise impact face forward laugh.",
    "poster_url": "https://placekitten.com/400/600",
    "trailer_url": "https://youtube.com/watch?v=IVgcsJgWwKd",
    "duration": 81,
    "release_year": 2014,
    "rating": 7.7,
    "cast": "Jerry Gill, Melissa Velazquez",
    "producer": "James Cameron",
    "views": 26796,
    "created_at": "2025-11-06T19:41:56.895036",
    "updated_at": "2025-11-06T19:41:56.895043",
    "is_liked": False
  },
  {
    "id": "67ef44e3-1ef4-4ecb-b0c6-8900720b2938",
    "title": "Reduced system-worthy alliance",
    "category": "Action",
    "description": "Car show company sort war yard carry none mission total pass particularly.",
    "poster_url": "https://placekitten.com/400/600",
    "trailer_url": "https://youtube.com/watch?v=JYDkUbhNpHS",
    "duration": 139,
    "release_year": 2023,
    "rating": 3.5,
    "cast": "Joshua Smith, Melissa Lopez, Kevin Lambert, Stephen Sloan",
    "producer": "Martin Scorsese",
    "views": 32368,
    "created_at": "2025-11-06T19:41:56.895840",
    "updated_at": "2025-11-06T19:41:56.895844",
    "is_liked": True
  },
  {
    "id": "8728c600-b9b2-4283-a80a-38d7ac4e7238",
    "title": "Open-architected explicit core",
    "category": "Fantasy",
    "description": "Exactly fight picture while begin power state list drive blood plant.",
    "poster_url": "https://picsum.photos/400/600",
    "trailer_url": "https://youtube.com/watch?v=NHjpMtjgUtg",
    "duration": 127,
    "release_year": 1991,
    "rating": 5.2,
    "cast": "James Hernandez, Kenneth Murphy",
    "producer": "Jordan Peele",
    "views": 63865,
    "created_at": "2025-11-06T19:41:56.896260",
    "updated_at": "2025-11-06T19:41:56.896264",
    "is_liked": True
  },
  {
    "id": "fa64e161-a76a-4897-b2a6-d44fa86c37c1",
    "title": "Cross-platform composite service-desk",
    "category": "Sci-Fi",
    "description": "Old range modern song scene reveal guess he election truth.",
    "poster_url": "https://placekitten.com/400/600",
    "trailer_url": "https://youtube.com/watch?v=wixwxPbgfAC",
    "duration": 125,
    "release_year": 1996,
    "rating": 8.1,
    "cast": "Alexander Jackson, Ryan Simon",
    "producer": "Patty Jenkins",
    "views": 75717,
    "created_at": "2025-11-06T19:41:56.896761",
    "updated_at": "2025-11-06T19:41:56.896764",
    "is_liked": False
  },
  {
    "id": "1af866f8-eee5-461f-88bf-efa0cf273279",
    "title": "Cross-group coherent help-desk",
    "category": "Action",
    "description": "Face consider similar send now score yet Mr last technology action little late modern hard relationship ago newspaper.",
    "poster_url": "https://picsum.photos/400/600",
    "trailer_url": "https://youtube.com/watch?v=gXGXtoLUNJk",
    "duration": 109,
    "release_year": 2019,
    "rating": 3.9,
    "cast": "Evelyn Salazar, Isaiah Wood, Christopher Jones",
    "producer": "Steven Spielberg",
    "views": 87942,
    "created_at": "2025-11-06T19:41:56.897405",
    "updated_at": "2025-11-06T19:41:56.897408",
    "is_liked": True
  },
  {
    "id": "9e5d9884-8c74-40bf-bd07-8ef2f66251b3",
    "title": "Progressive homogeneous protocol",
    "category": "Fantasy",
    "description": "Think apply they can friend market seek cold south population next support law half her.",
    "poster_url": "https://placekitten.com/400/600",
    "trailer_url": "https://youtube.com/watch?v=MIjHVZZHxwR",
    "duration": 151,
    "release_year": 1999,
    "rating": 8.8,
    "cast": "Krista Dunlap, Julie Nixon, Amanda Sanders",
    "producer": "Christopher Nolan",
    "views": 13676,
    "created_at": "2025-11-06T19:41:56.898003",
    "updated_at": "2025-11-06T19:41:56.898006",
    "is_liked": False
  },
  {
    "id": "8cabbd90-6afd-43bc-bd30-7a8f0463ea7c",
    "title": "Digitized 24/7 collaboration",
    "category": "Horror",
    "description": "Final what window image assume institution kid including it.",
    "poster_url": "https://dummyimage.com/400x600",
    "trailer_url": "https://youtube.com/watch?v=dFdySkDqXOa",
    "duration": 126,
    "release_year": 2010,
    "rating": 2.3,
    "cast": "Katrina Livingston, Jonathan Quinn",
    "producer": "Martin Scorsese",
    "views": 91203,
    "created_at": "2025-11-06T19:41:56.898544",
    "updated_at": "2025-11-06T19:41:56.898550",
    "is_liked": False
  },
  {
    "id": "6ac31d68-414b-49b6-91fa-c38776f65f8d",
    "title": "Profound web-enabled circuit",
    "category": "Adventure",
    "description": "Work somebody middle national method increase recently trade music.",
    "poster_url": "https://placekitten.com/400/600",
    "trailer_url": "https://youtube.com/watch?v=lxueOApsUNO",
    "duration": 96,
    "release_year": 2021,
    "rating": 7.6,
    "cast": "Cheryl Shaffer, Lisa Austin, Jason Perry, Nicholas Franco, Jose Mcgrath",
    "producer": "Christopher Nolan",
    "views": 38318,
    "created_at": "2025-11-06T19:41:56.899574",
    "updated_at": "2025-11-06T19:41:56.899578",
    "is_liked": False
  },
  {
    "id": "9d9249b6-d324-44ec-afeb-81afef96e3a4",
    "title": "Persevering web-enabled flexibility",
    "category": "Comedy",
    "description": "Focus still treat recently participant various moment people employee True.",
    "poster_url": "https://placekitten.com/400/600",
    "trailer_url": "https://youtube.com/watch?v=VMoRwauToXw",
    "duration": 118,
    "release_year": 2003,
    "rating": 3.9,
    "cast": "Sheila Jones, Joel Morris",
    "producer": "Steven Spielberg",
    "views": 32040,
    "created_at": "2025-11-06T19:41:56.900015",
    "updated_at": "2025-11-06T19:41:56.900018",
    "is_liked": True
  },
  {
    "id": "74d856b3-aab4-49f4-8af3-e710a1411833",
    "title": "Down-sized fresh-thinking access",
    "category": "Adventure",
    "description": "Leader despite listen follow bank cold send past later statement style miss trade future region own.",
    "poster_url": "https://dummyimage.com/400x600",
    "trailer_url": "https://youtube.com/watch?v=ELGZBKIEpgB",
    "duration": 115,
    "release_year": 2008,
    "rating": 3.5,
    "cast": "Anthony Mendez, Michelle Smith, Anne Baker",
    "producer": "Quentin Tarantino",
    "views": 44137,
    "created_at": "2025-11-06T19:41:56.900665",
    "updated_at": "2025-11-06T19:41:56.900668",
    "is_liked": True
  },
  {
    "id": "917659e8-eb06-41a8-9065-9de51c6d7afb",
    "title": "Polarized tertiary standardization",
    "category": "Animation",
    "description": "Blue change local together occur best bit break at approach main.",
    "poster_url": "https://picsum.photos/400/600",
    "trailer_url": "https://youtube.com/watch?v=GkYTbEPNhAd",
    "duration": 155,
    "release_year": 2004,
    "rating": 4.0,
    "cast": "Shannon Gardner, Patricia Stewart",
    "producer": "Martin Scorsese",
    "views": 17624,
    "created_at": "2025-11-06T19:41:56.901099",
    "updated_at": "2025-11-06T19:41:56.901102",
    "is_liked": True
  },
  {
    "id": "64337dc2-dadd-48cc-bb53-7c5e9a088ef3",
    "title": "Automated user-facing budgetary management",
    "category": "Sci-Fi",
    "description": "Magazine quickly everyone war role field throw a hundred.",
    "poster_url": "https://dummyimage.com/400x600",
    "trailer_url": "https://youtube.com/watch?v=ArjKuDayefS",
    "duration": 113,
    "release_year": 2015,
    "rating": 1.0,
    "cast": "Gina Smith DVM, Eduardo Patterson, James Griffin, John Parsons, Anthony Patterson",
    "producer": "Greta Gerwig",
    "views": 72466,
    "created_at": "2025-11-06T19:41:56.902053",
    "updated_at": "2025-11-06T19:41:56.902056",
    "is_liked": False
  },
  {
    "id": "d7ac80e5-ebb5-4d1b-8848-01f9afda4f57",
    "title": "Enterprise-wide multi-state challenge",
    "category": "Thriller",
    "description": "Decide actually business it success green perhaps any benefit include require begin deep find southern.",
    "poster_url": "https://placekitten.com/400/600",
    "trailer_url": "https://youtube.com/watch?v=KBhoMBsfnnJ",
    "duration": 81,
    "release_year": 2003,
    "rating": 4.7,
    "cast": "Theresa Stone, Kristen Fuentes",
    "producer": "Martin Scorsese",
    "views": 83240,
    "created_at": "2025-11-06T19:41:56.902517",
    "updated_at": "2025-11-06T19:41:56.902520",
    "is_liked": False
  },
  {
    "id": "2a3fce9b-8ca2-4188-b57d-dfb2bd7fcbee",
    "title": "Synchronized reciprocal parallelism",
    "category": "Sci-Fi",
    "description": "Open ahead guess think stand himself door week west your American political lay occur.",
    "poster_url": "https://dummyimage.com/400x600",
    "trailer_url": "https://youtube.com/watch?v=kLzBlXTXaJU",
    "duration": 96,
    "release_year": 1994,
    "rating": 2.9,
    "cast": "Jason Hall, Steven Calderon, Amy Collins",
    "producer": "Quentin Tarantino",
    "views": 16379,
    "created_at": "2025-11-06T19:41:56.903104",
    "updated_at": "2025-11-06T19:41:56.903107",
    "is_liked": False
  },
  {
    "id": "7184178d-44b0-4e78-8f13-73faa9fc6c3c",
    "title": "Multi-layered mobile methodology",
    "category": "Drama",
    "description": "Decide personal rise break perhaps data arrive collection training up evening so minute fish peace.",
    "poster_url": "https://placekitten.com/400/600",
    "trailer_url": "https://youtube.com/watch?v=UZCpkDTKxMP",
    "duration": 154,
    "release_year": 1992,
    "rating": 2.5,
    "cast": "Todd Johnson, Susan Anderson",
    "producer": "Greta Gerwig",
    "views": 82294,
    "created_at": "2025-11-06T19:41:56.903570",
    "updated_at": "2025-11-06T19:41:56.903573",
    "is_liked": False
  },
  {
    "id": "789c0bab-289d-48a4-a554-ef4c9bc0ba91",
    "title": "Face-to-face tangible toolset",
    "category": "Drama",
    "description": "Movement central visit per manage during short human light dinner player fact.",
    "poster_url": "https://placekitten.com/400/600",
    "trailer_url": "https://youtube.com/watch?v=gJpjzQfcJin",
    "duration": 127,
    "release_year": 2025,
    "rating": 4.6,
    "cast": "Reginald Bright, Jo Campos, Joseph Williamson, Barbara Moreno, Michael Wallace",
    "producer": "Christopher Nolan",
    "views": 31386,
    "created_at": "2025-11-06T19:41:56.904522",
    "updated_at": "2025-11-06T19:41:56.904525",
    "is_liked": True
  },
  {
    "id": "f896ddf6-dddb-413d-a868-d283638295bb",
    "title": "Total real-time orchestration",
    "category": "Animation",
    "description": "Floor choice social choice to cut bill whatever three send build agree expert Republican cut drive information television.",
    "poster_url": "https://dummyimage.com/400x600",
    "trailer_url": "https://youtube.com/watch?v=wIoVFdXKQft",
    "duration": 155,
    "release_year": 2025,
    "rating": 5.5,
    "cast": "Vicki Macias, Susan Wilkerson, Kimberly Garza",
    "producer": "Steven Spielberg",
    "views": 23335,
    "created_at": "2025-11-06T19:41:56.905118",
    "updated_at": "2025-11-06T19:41:56.905122",
    "is_liked": False
  },
  {
    "id": "61fd3412-d23f-470e-a129-5b9e1aea2ed7",
    "title": "Future-proofed value-added structure",
    "category": "Fantasy",
    "description": "Begin very role few teacher time certainly majority bed even soldier.",
    "poster_url": "https://placekitten.com/400/600",
    "trailer_url": "https://youtube.com/watch?v=dysflGcCfdN",
    "duration": 111,
    "release_year": 1990,
    "rating": 2.7,
    "cast": "Michael Rice, Paula Hayes, Diane Johnson, John Richardson, David Floyd",
    "producer": "Jordan Peele",
    "views": 75462,
    "created_at": "2025-11-06T19:41:56.906063",
    "updated_at": "2025-11-06T19:41:56.906066",
    "is_liked": True
  },
  {
    "id": "975555af-d6fe-4384-82bb-a6c418c265bf",
    "title": "Cross-platform non-volatile circuit",
    "category": "Drama",
    "description": "Price son when dinner market with force agent price trouble chance stop cost dinner example education they.",
    "poster_url": "https://picsum.photos/400/600",
    "trailer_url": "https://youtube.com/watch?v=UHXNXTfTOuf",
    "duration": 176,
    "release_year": 2012,
    "rating": 6.2,
    "cast": "Elizabeth Martinez, Sandra Walters, Steven Terrell, Kelsey Lynch, Mark Peterson",
    "producer": "Quentin Tarantino",
    "views": 10868,
    "created_at": "2025-11-06T19:41:56.907014",
    "updated_at": "2025-11-06T19:41:56.907017",
    "is_liked": False
  },
  {
    "id": "bd28d10a-f38f-41dd-8a1c-c41af283c854",
    "title": "Business-focused context-sensitive paradigm",
    "category": "Drama",
    "description": "Assume cold throw nearly term speech if make anyone air building particularly certain campaign ball however nation scientist open avoid.",
    "poster_url": "https://placekitten.com/400/600",
    "trailer_url": "https://youtube.com/watch?v=EknPIDTCAQD",
    "duration": 125,
    "release_year": 2000,
    "rating": 9.5,
    "cast": "Angela Berg, Anthony Woods, Heather Johnson, Christine Boone",
    "producer": "Jordan Peele",
    "views": 86523,
    "created_at": "2025-11-06T19:41:56.907801",
    "updated_at": "2025-11-06T19:41:56.907804",
    "is_liked": False
  }
]

user_db = [
  {
    "id": "ed0f9045-6f6a-46e5-8f5b-6f165b28e802",
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
    "id": "5b4fb3be-2e8b-4cb3-8cbc-687fcabeaca0",
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
    "id": "8dfc4a90-7519-415c-89bc-c2ed494cb307",
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
    "id": "7de58417-3f8c-44c1-89e8-b374b87b0a5f",
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
    "id": "22fe62e6-3186-494f-9422-d7b421af0c76",
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
    "id": "11323935-1cd7-4514-b326-1cdb3f0a894d",
    "phone": "+233-55-310-5254",
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
    "id": "91836d59-4f90-4224-85a0-78ae00ad2e5b",
    "phone": "+233-20-554-2343",
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
    "id": "93dead5b-b598-456c-972b-1c3535a5b5f3",
    "phone": "+233-27-349-6123",
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
    "id": "c3088309-e105-4d6e-9acd-8330cfc1671b",
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
