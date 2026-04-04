-- 1. Upsert (Добавить или обновить)
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;

-- 2. Удаление
CREATE OR REPLACE PROCEDURE delete_contact(p_search TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts WHERE name = p_search OR phone = p_search;
END;
$$;

-- 3. Массовая вставка с валидацией
CREATE OR REPLACE PROCEDURE bulk_insert(p_names VARCHAR[], p_phones VARCHAR[])
LANGUAGE plpgsql AS $$
DECLARE 
    i INT;
BEGIN
    -- Проверяем, что массив не пустой
    IF p_names IS NOT NULL THEN
        FOR i IN 1 .. array_upper(p_names, 1) LOOP
            -- Валидация: если номер >= 10 символов
            IF length(p_phones[i]) >= 10 THEN
                -- Используем логику IF EXISTS вместо ON CONFLICT для стабильности в процедуре
                IF EXISTS (SELECT 1 FROM contacts WHERE name = p_names[i]) THEN
                    UPDATE contacts SET phone = p_phones[i] WHERE name = p_names[i];
                ELSE
                    INSERT INTO contacts(name, phone) VALUES(p_names[i], p_phones[i]);
                END IF;
            ELSE
                RAISE NOTICE 'Некорректный номер для %: %', p_names[i], p_phones[i];
            END IF;
        END LOOP;
    END IF;
END;
$$;