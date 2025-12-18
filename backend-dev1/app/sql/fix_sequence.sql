-- Fix the movie_list ID sequence
-- This resets the sequence to the maximum ID + 1
SELECT
    setval (
        pg_get_serial_sequence ('movie_list', 'id'),
        COALESCE(MAX(id), 1),
        true
    )
FROM
    movie_list;

-- Fix the users ID sequence
-- This resets the sequence to the maximum ID + 1
SELECT
    setval (
        pg_get_serial_sequence ('users', 'id'),
        COALESCE(MAX(id), 1),
        true
    )
FROM
    users;