-- Table: public.scherm

-- DROP TABLE IF EXISTS public.scherm;

CREATE TABLE IF NOT EXISTS public.scherm
(
    bericht character varying(140) COLLATE pg_catalog."default",
    datum date,
    naam character varying(255) COLLATE pg_catalog."default",
    steden character varying(50) COLLATE pg_catalog."default",
    beoordeling_datum date,
    naam_moderator character varying(255) COLLATE pg_catalog."default",
    email_moderator character varying(255) COLLATE pg_catalog."default",
    controle character varying(255) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.scherm
    OWNER to postgres;