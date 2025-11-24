from faker import Faker
import random
import uuid
import json
from datetime import datetime
from app.models.users import UserRole, UserStatus, VerifyEmail, VerifyPhone, ServiceStatus, GenderStatus

fake = Faker()

def generate_mock_users(n=20):
    users = []
    
    def ghana_num():
        
        prefixes = ["20", "23", "24", "26", "27", "28", "50", "54", "55", "59"]
        prefix = random.choice(prefixes)
        
        mid = random.randint(111, 999)
        end = random.randint(1111, 9999)
        
        return f"+233-{prefix}-{mid}-{end}"
        
    
    for _ in range(n):
        gender = random.choice(list(GenderStatus))
        role = random.choice(list(UserRole))
        status = random.choice(list(UserStatus))
        service = random.choice(list(ServiceStatus))
        
        user = {
            "id": str(uuid.uuid4()),
            "phone": ghana_num(),
            "email": fake.unique.email(),
            "firstName": fake.first_name_male() if gender == GenderStatus.MALE else fake.first_name_female(),
            "lastName": fake.last_name(),
            "role": role.value,
            "status": status.value,
            "service": service.value,
            "profilePicture": fake.image_url(),
            "dateOfbirth": fake.date_of_birth(minimum_age=18, maximum_age=70).isoformat(),
            "gender": gender.value,
            "bio": fake.sentence(nb_words=12),
            "location": {
                "lat": fake.latitude(),
                "lng": fake.longitude()
            },
            "address": fake.address(),
            "isEmailVerified": random.choice(list(VerifyEmail)).value,
            "isPhoneVerified": random.choice(list(VerifyPhone)).value,
            "preferences": {
                "theme": random.choice(["light", "dark"]),
                "language": random.choice(["en", "fr", "es"]),
            },
            "notificationSettings": {
                "emailNotifications": fake.boolean(),
                "smsNotifications": fake.boolean(),
                "pushNotifications": fake.boolean(),
            },
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat(),
        }
        users.append(user)
    return users


if __name__ == "__main__":
    mock_users = generate_mock_users(20)
    
    # Write to JSON file
    output_file = "mock_users.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(mock_users, f, indent=2, ensure_ascii=False, default=str)
    
    print(f" Generated {len(mock_users)} mock users.")
    print(f" Written to {output_file}")
