"""
Script to populate SQLite database with mock data from mockDB.py
"""
import asyncio
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import AsyncSessionLocal, init_db
from app.models.users import User, UserRole, UserStatus, VerifyStatus, ServiceStatus, GenderStatus
from app.models.movies import MovieList
from app.core.mockDB import movies_db, user_db
import uuid


async def load_users():
    """Load users from mockDB.py into database"""
    print("Loading users from mockDB.py...")
    
    from sqlalchemy import select
    
    async with AsyncSessionLocal() as session:
        added_count = 0
        skipped_count = 0
        
        for user_data in user_db:
            # Check if user already exists (by email or phone)
            email = user_data.get('email')
            phone = user_data.get('phone')
            
            result = await session.execute(
                select(User).filter(
                    (User.email == email) | (User.phone == phone)
                )
            )
            existing_user = result.scalar_one_or_none()
            
            if existing_user:
                skipped_count += 1
                continue
            
            # Parse ISO datetime strings
            dob = datetime.fromisoformat(user_data['dateOfbirth'].replace('Z', '+00:00')) if user_data.get('dateOfbirth') else None
            
            user = User(
                phone=phone,
                email=email,
                firstName=user_data.get('firstName'),
                lastName=user_data.get('lastName'),
                role=user_data.get('role'),
                status=user_data.get('status'),
                profilePicture=user_data.get('profilePicture'),
                dateOfbirth=dob,
                gender=user_data.get('gender'),
                bio=user_data.get('bio'),
                service=user_data.get('service'),
                watchlist=user_data.get('watchlist'),
                address=user_data.get('address'),
                location=user_data.get('location'),
                isEmailVerified=user_data.get('isEmailVerified'),
                isPhoneVerified=user_data.get('isPhoneVerified'),
                preferences=user_data.get('preferences'),
                notificationSettings=user_data.get('notificationSettings'),
            )
            session.add(user)
            added_count += 1
        
        await session.commit()
        print(f"✓ Loaded {added_count} users (skipped {skipped_count} existing)")


async def load_movies():
    """Load movies from mockDB.py into database"""
    print("Loading movies from mockDB.py...")
    
    async with AsyncSessionLocal() as session:
        for movie_data in movies_db:
            movie = MovieList(
                title=movie_data.get('title'),
                category=movie_data.get('category'),
                description=movie_data.get('description'),
                poster_url=movie_data.get('poster_url'),
                trailer_url=movie_data.get('trailer_url'),
                duration=movie_data.get('duration'),
                release_year=movie_data.get('release_year'),
                rating=movie_data.get('rating'),
                cast=movie_data.get('cast'),
                producer=movie_data.get('producer'),
                views=movie_data.get('views', 0),
                is_liked=movie_data.get('is_liked', False),
            )
            session.add(movie)
        
        await session.commit()
        print(f"✓ Loaded {len(movies_db)} movies")


async def main():
    """Main function to populate database"""
    print("Starting database population...")
    print("=" * 50)
    
    # Initialize database tables
    await init_db()
    print("✓ Database tables initialized")
    
    try:
        await load_users()
        await load_movies()
        
        print("=" * 50)
        print("✓ Database population completed successfully!")
        
    except Exception as e:
        print(f"✗ Error populating database: {str(e)}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
