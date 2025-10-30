"""
Common database types
"""

from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID


class UUID(TypeDecorator):
    """Platform-independent UUID type. """
    impl = CHAR
    cache_ok=True
    
    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(PostgresUUID())
        else:
            return dialect.type_descriptor(CHAR(36))
        
    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            return str(value)
        
    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return str(value)