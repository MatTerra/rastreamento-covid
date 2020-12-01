CREATE OR REPLACE VIEW hospitais_view AS
    SELECT
        hospital_contratacoes.h_name AS Nome,
        hospital_internacoes.count_int AS Internacoes,
        hospital_contratacoes.count_cont AS Contratacoes,
        (cast(hospital_internacoes.count_int as decimal)/cast(hospital_contratacoes.count_cont as decimal)) AS Relação
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
            WHERE internacao.internacao_alta IS NULL
        GROUP BY hospital.hospital_id_
    ) AS hospital_internacoes
    ON hospital_internacoes.h_id = hospital_contratacoes.h_id
    ORDER BY Relação DESC;