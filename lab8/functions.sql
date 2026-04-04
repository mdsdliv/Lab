-- 1. Поиск по паттерну
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p text)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT c.id, c.name, c.phone FROM contacts c
                 WHERE c.name ILIKE '%' || p || '%'
                    OR c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

-- 2. Пагинация
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT `c.name, c.phone FROM contacts c
                 ORDER BY c.id LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;