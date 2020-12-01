-- CREATE OR REPLACE VIEW hospitais_view AS
    SELECT
        -- hospital.hospital_nome AS Nome,
        -- count_count AS Medicos,
        -- count_int  AS Internacoes
        *
    FROM
    (
        SELECT 
            hospital.hospital_id_ AS h_id,
            hospital.hospital_nome AS h_name,
            COUNT(contratacao.contratacao_medico_id_) AS count_cont
        FROM hospital
            LEFT JOIN contratacao ON contratacao.contratacao_hospital_id_ = hospital.hospital_id_
        GROUP BY hospital.hospital_id_
    ) AS hospital_contratacoes 
    LEFT JOIN 
    (
        SELECT 
            hospital.hospital_id_ AS h_id,
            hospital.hospital_nome AS h_name,
            COUNT(internacao.internacao_usuario_id_) AS count_int
        FROM hospital
            LEFT JOIN internacao  ON internacao.internacao_hospital_id_ = hospital.hospital_id_
        GROUP BY hospital.hospital_id_
    ) AS hospital_internacoes
    ON hospital_internacoes.h_id = hospital_contratacoes.h_id;