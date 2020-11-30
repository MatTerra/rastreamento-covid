CREATE OR REPLACE VIEW internacoes_diagnostico AS
    SELECT usuario_id_, diagnostico_data_inicio_sintomas, diagnostico_data_exame, internacao_data_inicio,
           hospital_nome, internacao_uti, internacao_alta, diagnostico_data_recuperacao
    FROM diagnostico
        LEFT JOIN usuario ON usuario_id_ = diagnostico_usuario_id_
        LEFT JOIN internacao ON (diagnostico_data_exame <= internacao_data_inicio
                                 OR diagnostico_data_inicio_sintomas <= internacao_data_inicio)
                                AND internacao_usuario_id_ = diagnostico_usuario_id_
        LEFT JOIN hospital ON hospital_id_ = internacao_hospital_id_;