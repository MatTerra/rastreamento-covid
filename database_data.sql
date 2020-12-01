--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5 (Ubuntu 11.5-3.pgdg18.04+1)
-- Dumped by pg_dump version 12.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: sintoma; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.sintoma (sintoma_id_, sintoma_descricao, sintoma_risco) FROM stdin;
4                               	Perda de olfato/paladar	1
1                               	Febre	2
2                               	Tosse seca	2
3                               	Cansaço	1
5                               	Dores	1
6                               	Dor ou pressão no peito	3
7                               	Dificuldade de respirar	3
8                               	Perda da fala ou de movimento	4
\.


--
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.usuario (usuario_id_, usuario_ord, usuario_salt, usuario_password, usuario_primeiro_nome, usuario_ultimo_nome, usuario_consentimento, usuario_data_nascimento) FROM stdin;
62d0bbcb6d0e4d6cb3a205bb6685d422	2	EObHcLnuVv6R5wyV+4Q98aenpWPJy0xc	mxeQswNmT8W6LO+ErLfulQsayTMlrRM5Q8dD5SAGe7nuf0AFoBQdDN/bFLUwdhDEkOmKqdXZUeC4FqUJnF2N3w==	Mateus	Terra	t	2020-11-27
5046b143d0354697844f47a6812d0f3f	3	McnTgMLEwufOzbkUwuEcOH93Au0dlHsX	Y9mbO0R7xyP8FeGiFgwRFK8i3faFPt74XQdXZ/hHDW8+UM2QVa6iRbc1FdCa9h32NhndutZ0sSVb+LWp5R2LJQ==	tito	silva	t	2020-11-27
2c6a175207ec4b1a8a723f3695962421	4	lyoB1Zr/Le6ZXtVjP+SG28MZPZLJMEnq	bi9rEL1YkIEOQzjYwlmKH7ix6YfRkBU2QdpeJY5tMcCrFBmZJIfBvD4QLL5udl+8AvUBS99+X12zkU63/yWsQg==	Larissa	Araújo	t	2020-11-28
cab197f246ef4c418fa5d39b1261e5db	6	WQFnM6gTPCSaFpbsVO9PK+gEsKGtC2J5	es999cjIl4Ig8q/jU3wSFiKVmsR4XzGUFU5NS8Xcefik52PezzZfq8YLSkGe24w5v9tbYRodhwGJngLqHWU/YQ==	Felipe	Terra	t	2020-11-30
87f533b0294b4341bcfdf10b38ad3181	7	5s9j/WueO+SwzEyzV6MdxecqXNwXNufY	vW2TBL6Wv6jQzJ6EK5kXZkss9F888H5qvp6s219LY5iizvFHa/Q/56tVrwOjT3g8Lb7C+d3nEJpel32dWX9hkg==	André	Terra	t	2020-11-30
9c04c082c4f14f818fd876e63de414c1	8	/j45sWdXIWvIUNMxWm6B6/vEnC31kiQh	sWWhfZtNI+PxysiwpB3ja85rElx0LEcgOsqBA+zBAzpLOleqMjAlTSFevsnDRKEYXsMA/QoRz00prYXi4k9RFg==	João	Pires	t	2020-12-01
ece90961d0774ee2b23e9458674fc76a	9	Ub4iOc00G0L3cXRNBi/GyRRjai5R7CW+	/opnH7Spq3QH5QkHlAnE1n/DgvJa2hTKQZQWZHvjer+GYiJryBZSHDOURUdJGwHM5gglDJPiXjUezPQBY5wHQg==	Rafael	Oliveira	t	2020-12-01
\.


--
-- Data for Name: caso_sintoma; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.caso_sintoma (caso_sintoma_id_, caso_sintoma_usuario_id_, caso_sintoma_sintoma_id_, caso_sintoma_inicio, caso_sintoma_final) FROM stdin;
e2e8a0bad7d24745ad00cba7e585df71	2c6a175207ec4b1a8a723f3695962421	4                               	2020-10-23 00:00:00	2020-11-30 00:00:00
3fc58a5546d84466b3dc1b9b47af17d9	9c04c082c4f14f818fd876e63de414c1	8                               	2020-06-30 00:00:00	2020-07-05 00:00:00
567aefc7cc9345918836d6710b540e1e	9c04c082c4f14f818fd876e63de414c1	6                               	2020-06-20 00:00:00	2020-07-25 00:00:00
4c21dcadeb2b48d48a135222326b8bda	9c04c082c4f14f818fd876e63de414c1	4                               	2020-06-15 00:00:00	2020-09-15 00:00:00
3682dd16b095412fb6ff02ebce8919a3	62d0bbcb6d0e4d6cb3a205bb6685d422	3                               	2020-11-20 00:00:00	\N
0bd95f63dee54fef85b3c8e8b03fdb28	62d0bbcb6d0e4d6cb3a205bb6685d422	2                               	2020-11-22 00:00:00	\N
\.


--
-- Data for Name: local; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.local (local_id_, local_ord, local_nome, local_longitude, local_latitude) FROM stdin;
2bb9857a26d44cad96674452aa81c0bd	1	Iguatemi	-47.88579335396371	-15.720324649070855
b8adf15ec5b2400cb6ee8beb7cc702a8	2	Boulevard	-47.899150000160816	-15.733490344528596
f274bae54d9a444d830d100540feb751	3	Big Box Qi 8	-47.85030160822356	-15.74378596625258
3c0b3e542d3e425681af4168886557fe	4	Pão de Açúcar Lago Norte	-47.887251719766724	-15.72288437962212
b05316d9005c4216adddc86ab7530dfc	5	Padaria Ilha dos Pães	-47.83940111082768	-15.75340988758394
9e4213b403f440f8aca8833aa8132241	6	Big Box Qi 3	-47.86479090208811	-15.7333974029369
ba9f19d13c1642a7a31c3f6dabd7f09e	7	Delegacia Lago Norte	-47.86485527510626	-15.731838039937644
70180e23d66d4312836ade9b3e3facb6	8	INDI Lago Norte	-47.86283825387099	-15.729271777453494
\.


--
-- Data for Name: checkin; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.checkin (checkin_id_, checkin_id_usuario, checkin_local_id_, checkin_risco, checkin_inicio, checkin_final) FROM stdin;
2daa753afe8048a5b87819a7311fe88c	87f533b0294b4341bcfdf10b38ad3181	f274bae54d9a444d830d100540feb751	0	2020-09-10 15:00:00	2020-09-10 16:07:00
7d58db7b03a44abcb042436b23304970	9c04c082c4f14f818fd876e63de414c1	2bb9857a26d44cad96674452aa81c0bd	11	2020-11-01 09:00:00	2020-11-01 22:00:00
0da3dde599554a0bbee6f9b02f4b6e46	87f533b0294b4341bcfdf10b38ad3181	2bb9857a26d44cad96674452aa81c0bd	6	2020-11-01 12:00:00	2020-11-01 22:00:00
664d1b45cf5a48d4945384a4964090dd	2c6a175207ec4b1a8a723f3695962421	2bb9857a26d44cad96674452aa81c0bd	6	2020-11-01 14:00:00	2020-11-01 20:00:00
03a39c9b628d4566a2dd9a5e8b5866f9	62d0bbcb6d0e4d6cb3a205bb6685d422	2bb9857a26d44cad96674452aa81c0bd	10	2020-11-01 16:00:00	2020-11-01 18:00:00
58c43183c33a4731a8153ce8ea0b6db5	cab197f246ef4c418fa5d39b1261e5db	2bb9857a26d44cad96674452aa81c0bd	10	2020-11-01 15:00:00	2020-11-01 15:30:00
\.


--
-- Data for Name: hospital; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.hospital (hospital_id_, hospital_local, hospital_nome) FROM stdin;
d565829ca2154de2acaf169655087f31	Setor Hospitalar Norte	Santa Lúcia Norte
48984b3835a3469494980ae21eddb0ef	Setor Hospitalar Norte	Santa Helena
c9c61034132c4519a16e4f1ce2a27438	Setor Sudoeste	HFA
42ac21a81e47421bb1a3ac5d0e767b39	Setor Hospitalar Sul	Santa Lúcia Sul
9a2c71c5c7384a818d1f8d25186c52b5	SMHN Q 2	HRAN
\.


--
-- Data for Name: medico; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.medico (medico_id_, medico_nome) FROM stdin;
2ce71090258b4d50a7bdadf916a06735	João Pires
20c8f384c0fc4f94ada61d2cd123644c	Clara Silva
de46a7cd25df4c65af3c217eefbe15b8	Alberto Souza
8c42ee4c5f124df6bec97cb075938634	Larissa Tavares
3e394096803049978a91ab8b50299239	Luna Costa
\.


--
-- Data for Name: contratacao; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.contratacao (contratacao_medico_id_, contratacao_hospital_id_) FROM stdin;
8c42ee4c5f124df6bec97cb075938634	c9c61034132c4519a16e4f1ce2a27438
de46a7cd25df4c65af3c217eefbe15b8	c9c61034132c4519a16e4f1ce2a27438
de46a7cd25df4c65af3c217eefbe15b8	d565829ca2154de2acaf169655087f31
20c8f384c0fc4f94ada61d2cd123644c	9a2c71c5c7384a818d1f8d25186c52b5
20c8f384c0fc4f94ada61d2cd123644c	48984b3835a3469494980ae21eddb0ef
2ce71090258b4d50a7bdadf916a06735	42ac21a81e47421bb1a3ac5d0e767b39
2ce71090258b4d50a7bdadf916a06735	d565829ca2154de2acaf169655087f31
3e394096803049978a91ab8b50299239	48984b3835a3469494980ae21eddb0ef
\.


--
-- Data for Name: emissor; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.emissor (emissor_id_, emissor_nome, emissor_local) FROM stdin;
17ab607cf8b14cfa9322c5fa95dc46b5	Sabin Lago Norte	Lago Norte Qi 2
5a9f7cca3f0d46f0a34a5d5ddb7a9f4b	Sabin Deck Norte	Deck Norte, CA do Lago Norte
3dfbd5eb0d42432282156c0a208ab8cc	Exame W3 Norte	Ed. Biosphere
1da7a38351604f6e851dd68c86c39e5d	Exame Asa Norte II	Ed. Carlton Center
5bcd5a3d835544b0816a92e415fe03bf	Sec. de Saúde DF	DF
\.


--
-- Data for Name: diagnostico; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.diagnostico (diagnostico_usuario_id_, diagnostico_emissor_id_, diagnostico_data_exame, diagnostico_data_inicio_sintomas, diagnostico_data_fim_sintomas, diagnostico_data_recuperacao) FROM stdin;
cab197f246ef4c418fa5d39b1261e5db	5a9f7cca3f0d46f0a34a5d5ddb7a9f4b	2020-10-29	2020-11-03	2020-11-18	2020-11-21
2c6a175207ec4b1a8a723f3695962421	17ab607cf8b14cfa9322c5fa95dc46b5	2020-10-28	2020-10-23	2020-11-10	2020-11-13
87f533b0294b4341bcfdf10b38ad3181	17ab607cf8b14cfa9322c5fa95dc46b5	2020-10-29	2020-10-22	2020-11-10	2020-11-12
9c04c082c4f14f818fd876e63de414c1	5a9f7cca3f0d46f0a34a5d5ddb7a9f4b	2020-06-25	2020-06-15	2020-08-15	2020-08-16
62d0bbcb6d0e4d6cb3a205bb6685d422	5bcd5a3d835544b0816a92e415fe03bf	2020-11-28	2020-11-20	\N	\N
ece90961d0774ee2b23e9458674fc76a	3dfbd5eb0d42432282156c0a208ab8cc	2020-09-20	2020-09-15	2020-09-25	\N
\.


--
-- Data for Name: email; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.email (email_id_, email_email, email_usuario_id_, email_primario) FROM stdin;
0a199e2d8a8d4f4891445345a7bef7ec	mat	62d0bbcb6d0e4d6cb3a205bb6685d422	t
ac1e693624c946de92225410db1f58c5	jt	5046b143d0354697844f47a6812d0f3f	t
59bf63bc85db450996b78bef34a904b3	lisa	2c6a175207ec4b1a8a723f3695962421	t
b317620213d4432ea5d16ddf5067ff0d	de	87f533b0294b4341bcfdf10b38ad3181	t
73e2e9f3e7f548c8881651d775b64824	pires	9c04c082c4f14f818fd876e63de414c1	t
d4fac457a0c84e40aac2922c6370944e	lipe@gmail.com	cab197f246ef4c418fa5d39b1261e5db	t
6cea9b10a20a4078960cdbda166b7de9	rafael@oliveira.com	ece90961d0774ee2b23e9458674fc76a	t
\.


--
-- Data for Name: internacao; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.internacao (internacao_hospital_id_, internacao_usuario_id_, internacao_data_inicio, internacao_uti, internacao_alta) FROM stdin;
d565829ca2154de2acaf169655087f31	2c6a175207ec4b1a8a723f3695962421	2020-11-03	t	2020-11-15
d565829ca2154de2acaf169655087f31	2c6a175207ec4b1a8a723f3695962421	2020-10-30	f	2020-11-03
c9c61034132c4519a16e4f1ce2a27438	9c04c082c4f14f818fd876e63de414c1	2020-06-30	t	2020-07-08
c9c61034132c4519a16e4f1ce2a27438	9c04c082c4f14f818fd876e63de414c1	2020-07-08	f	2020-08-16
48984b3835a3469494980ae21eddb0ef	62d0bbcb6d0e4d6cb3a205bb6685d422	2020-11-30	f	\N
\.


--
-- Data for Name: medicamento; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.medicamento (medicamento_id_, medicamento_nome) FROM stdin;
064de3e7f8cc491080f53f4f0d90c91f	Ivermectina
810822cf8eb64abbbbe713fb77a3eed8	Cloroquina
996d27142091416ea7af09b5f04bc018	Remdesivir
c66613b41d2748eb84b35d6a53a264a4	Favipiravir
2fa345d4fd34497fab92888f98aced60	Dexametasona
\.


--
-- Data for Name: notificacao; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.notificacao (notificacao_checkin_id_, notificacao_recebida) FROM stdin;
664d1b45cf5a48d4945384a4964090dd	f
03a39c9b628d4566a2dd9a5e8b5866f9	t
0da3dde599554a0bbee6f9b02f4b6e46	t
7d58db7b03a44abcb042436b23304970	f
58c43183c33a4731a8153ce8ea0b6db5	t
\.


--
-- Data for Name: telefone; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.telefone (telefone_id_, telefone_telefone, telefone_usuario_id_) FROM stdin;
b20664df8ae246f8ae413c0ca71268f0	986162112	62d0bbcb6d0e4d6cb3a205bb6685d422
2a8f55dc6479449283790ec433e685d2	990089090	5046b143d0354697844f47a6812d0f3f
2c4c00d5766b4104968e39926fed1c5d	33681037 	62d0bbcb6d0e4d6cb3a205bb6685d422
18ba65b15ee444328979e688119ad52c	918923754	2c6a175207ec4b1a8a723f3695962421
2aad81fcb45c4c8aba3c0c605bfc7e64	923488572	cab197f246ef4c418fa5d39b1261e5db
\.


--
-- Data for Name: tratamento; Type: TABLE DATA; Schema: public; Owner: gqgckjtj
--

COPY public.tratamento (tratamento_medicamento_id_, tratamento_medico_id_, tratamento_usuario_id_, tratamento_posologia) FROM stdin;
064de3e7f8cc491080f53f4f0d90c91f	8c42ee4c5f124df6bec97cb075938634	62d0bbcb6d0e4d6cb3a205bb6685d422	1 comprimido e reforço após 15 dias
064de3e7f8cc491080f53f4f0d90c91f	8c42ee4c5f124df6bec97cb075938634	5046b143d0354697844f47a6812d0f3f	1 comprimido e reforço após 15 dias
064de3e7f8cc491080f53f4f0d90c91f	8c42ee4c5f124df6bec97cb075938634	9c04c082c4f14f818fd876e63de414c1	1 comprimido e reforço após 15 dias
2fa345d4fd34497fab92888f98aced60	8c42ee4c5f124df6bec97cb075938634	62d0bbcb6d0e4d6cb3a205bb6685d422	200mg 1 vez ao dia
996d27142091416ea7af09b5f04bc018	de46a7cd25df4c65af3c217eefbe15b8	87f533b0294b4341bcfdf10b38ad3181	1 dose e reforço após 7 dias
\.


--
-- Name: checkin_checkin_id__seq; Type: SEQUENCE SET; Schema: public; Owner: gqgckjtj
--

SELECT pg_catalog.setval('public.checkin_checkin_id__seq', 1, false);


--
-- Name: local_local_ord_seq; Type: SEQUENCE SET; Schema: public; Owner: gqgckjtj
--

SELECT pg_catalog.setval('public.local_local_ord_seq', 8, true);


--
-- Name: usuario_usuario_ord_seq; Type: SEQUENCE SET; Schema: public; Owner: gqgckjtj
--

SELECT pg_catalog.setval('public.usuario_usuario_ord_seq', 9, true);


--
-- PostgreSQL database dump complete
--

