from faker import Faker
import random
import uuid
from datetime import datetime
from app.models.user import UserRole, UserStatus, VerifyEmail, VerifyPhone, ServiceStatus, GenderStatus

fake = Faker()

def generate_mock_users(n=20):
    users = []
    
    for _ in range(n):
        gender = random.choice(list(GenderStatus))
        role = random.choice(list(UserRole))
        status = random.choice(list(UserStatus))
        service = random.choice(list(ServiceStatus))
        
        user = {
            "id": str(uuid.uuid4()),
            "phone": fake.phone_number(),
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
            "createdAt": datetime.utcnow().isoformat(),
            "updatedAt": datetime.utcnow().isoformat(),
        }
        users.append(user)
    return users


if __name__ == "__main__":
    mock_users = generate_mock_users(20)
    print(mock_users[:5])  # preview the first 5 users
    print(f"✅ Generated {len(mock_users)} mock users.")
