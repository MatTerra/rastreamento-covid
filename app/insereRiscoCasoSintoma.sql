-- Inserção de sintomas
-- Procura pelos checkins existentes no mesmo período de tempo
-- e adiciona o risco
CREATE OR REPLACE FUNCTION insereRiscoCasoSintoma() RETURNS TRIGGER AS $$
DECLARE usuarioCheckin checkin%rowtype;
DECLARE risco_sintoma INT;
BEGIN
    SELECT INTO risco_sintoma sintoma_risco FROM sintoma WHERE
        sintoma_id_ = new.caso_sintoma_id_;
    -- Busca checkins do usuario durante o periodo em
    -- que sentiu os sintomas
    FOR usuarioCheckin IN SELECT * FROM checkin 
        WHERE checkin_id_usuario = new.caso_sintoma_usuario_id_
              AND checkin_inicio < new.checkin_final
              AND checkin_final > new.checkin_inicio
    LOOP
        -- Atualiza o checkin do usuário
        UPDATE checkin SET checkin_risco = checkin_risco + risco_sintoma
        WHERE checkin_id_ = usuarioCheckin.checkin_id_;
        -- Atualiza os checkins de outros usuários que ocorreram na
        -- mesma hora (intervalos coincidentes) e mesmo local 
        FOR checkin
    END LOOP;
END;
$$
LANGUAGE 'plpgsql';


CREATE TRIGGER risco_trigger_on_caso_sintoma
BEFORE INSERT ON caso_sintoma
FOR EACH ROW
EXECUTE PROCEDURE insereRiscoCasoSintoma();