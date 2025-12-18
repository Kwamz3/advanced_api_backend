from sqlalchemy.types import TypeDecorator, String
from sqlalchemy.orm import Session


class MovieID(TypeDecorator):
    """
    Custom type for Movie IDs in the format 'stp-0001', 'stp-0002', etc.
    """
    impl = String(12)  # 'stp-' (4) + up to 8 digits
    cache_ok = True
    
    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(String(12))
    
    def process_bind_param(self, value, dialect):
        """Process the value before storing it in the database"""
        if value is None:
            return value
        return str(value)
    
    def process_result_value(self, value, dialect):
        """Process the value retrieved from the database"""
        if value is None:
            return value
        return str(value)


def generate_movie_id(session: Session) -> str:
    """
    Generate a new sequential movie ID in the format 'stp-0001'.
    Queries the database for the highest existing ID and increments it.
    """
    # Import here to avoid circular imports
    from app.models.movies import MovieList
    
    # Get the highest movie ID from the database
    result = session.query(MovieList.id).order_by(MovieList.id.desc()).first()
    
    if result and result[0]:
        last_id = result[0]
        # Extract the numeric part and increment
        if isinstance(last_id, str) and last_id.startswith('stp-'):
            try:
                num = int(last_id.split('-')[1])
                new_num = num + 1
            except (IndexError, ValueError):
                new_num = 1
        else:
            new_num = 1
    else:
        new_num = 1
    
    # Format as 'stp-0001' with zero-padding (minimum 4 digits)
    return f"stp-{new_num:04d}"
