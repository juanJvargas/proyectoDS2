PGDMP     :                    v            ProyectoDjango    9.6.5    9.6.5 �    O	           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            P	           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            Q	           1262    98908    ProyectoDjango    DATABASE     �   CREATE DATABASE "ProyectoDjango" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Colombia.1252' LC_CTYPE = 'Spanish_Colombia.1252';
     DROP DATABASE "ProyectoDjango";
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            R	           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    12387    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            S	           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            �            1259    99174    appprincipal_actividadf    TABLE     �   CREATE TABLE appprincipal_actividadf (
    id integer NOT NULL,
    nombre character varying(40) NOT NULL,
    descripcion text NOT NULL,
    resultado_id integer NOT NULL
);
 +   DROP TABLE public.appprincipal_actividadf;
       public         postgres    false    3            �            1259    99172 (   appprincipal_actividaddeformacion_id_seq    SEQUENCE     �   CREATE SEQUENCE appprincipal_actividaddeformacion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ?   DROP SEQUENCE public.appprincipal_actividaddeformacion_id_seq;
       public       postgres    false    214    3            T	           0    0 (   appprincipal_actividaddeformacion_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE appprincipal_actividaddeformacion_id_seq OWNED BY appprincipal_actividadf.id;
            public       postgres    false    213            �            1259    107020     appprincipal_actividadevaluacion    TABLE     �   CREATE TABLE appprincipal_actividadevaluacion (
    id integer NOT NULL,
    nombre character varying(40) NOT NULL,
    descripcion text NOT NULL,
    indicador_id integer NOT NULL
);
 4   DROP TABLE public.appprincipal_actividadevaluacion;
       public         postgres    false    3            �            1259    99109    appprincipal_competencia    TABLE     �   CREATE TABLE appprincipal_competencia (
    id integer NOT NULL,
    nombre character varying(40) NOT NULL,
    descripcion text NOT NULL,
    curso_id character varying(10) NOT NULL
);
 ,   DROP TABLE public.appprincipal_competencia;
       public         postgres    false    3            �            1259    99107    appprincipal_competencia_id_seq    SEQUENCE     �   CREATE SEQUENCE appprincipal_competencia_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.appprincipal_competencia_id_seq;
       public       postgres    false    3    208            U	           0    0    appprincipal_competencia_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE appprincipal_competencia_id_seq OWNED BY appprincipal_competencia.id;
            public       postgres    false    207            �            1259    99058    appprincipal_curso    TABLE     �  CREATE TABLE appprincipal_curso (
    codigo character varying(10) NOT NULL,
    nombre character varying(40) NOT NULL,
    creditos integer NOT NULL,
    horas_clase_magistral integer NOT NULL,
    horas_estudio_independiente integer NOT NULL,
    tipo_curso character varying(50) NOT NULL,
    validable character varying(2) NOT NULL,
    habilitable character varying(2) NOT NULL,
    semestre integer NOT NULL,
    docente_id integer NOT NULL,
    programa_id character varying(10) NOT NULL
);
 &   DROP TABLE public.appprincipal_curso;
       public         postgres    false    3            �            1259    99157    appprincipal_indicador    TABLE     �   CREATE TABLE appprincipal_indicador (
    id integer NOT NULL,
    habilidad character varying(50) NOT NULL,
    contenido text NOT NULL,
    contexto text NOT NULL,
    resultado_id integer NOT NULL
);
 *   DROP TABLE public.appprincipal_indicador;
       public         postgres    false    3            �            1259    99155    appprincipal_indicador_id_seq    SEQUENCE        CREATE SEQUENCE appprincipal_indicador_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.appprincipal_indicador_id_seq;
       public       postgres    false    212    3            V	           0    0    appprincipal_indicador_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE appprincipal_indicador_id_seq OWNED BY appprincipal_indicador.id;
            public       postgres    false    211            �            1259    107018 '   appprincipal_indicadorevaluacion_id_seq    SEQUENCE     �   CREATE SEQUENCE appprincipal_indicadorevaluacion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 >   DROP SEQUENCE public.appprincipal_indicadorevaluacion_id_seq;
       public       postgres    false    3    219            W	           0    0 '   appprincipal_indicadorevaluacion_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE appprincipal_indicadorevaluacion_id_seq OWNED BY appprincipal_actividadevaluacion.id;
            public       postgres    false    218            �            1259    99065    appprincipal_profile    TABLE     u   CREATE TABLE appprincipal_profile (
    id integer NOT NULL,
    tipo text NOT NULL,
    user_id integer NOT NULL
);
 (   DROP TABLE public.appprincipal_profile;
       public         postgres    false    3            �            1259    99063    appprincipal_profile_id_seq    SEQUENCE     }   CREATE SEQUENCE appprincipal_profile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.appprincipal_profile_id_seq;
       public       postgres    false    3    205            X	           0    0    appprincipal_profile_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE appprincipal_profile_id_seq OWNED BY appprincipal_profile.id;
            public       postgres    false    204            �            1259    99076    appprincipal_programa    TABLE     ,  CREATE TABLE appprincipal_programa (
    codigo character varying(10) NOT NULL,
    nombre_programa character varying(50) NOT NULL,
    escuela character varying(40) NOT NULL,
    numero_semestres integer NOT NULL,
    numero_creditos_graduacion integer NOT NULL,
    director_id integer NOT NULL
);
 )   DROP TABLE public.appprincipal_programa;
       public         postgres    false    3            �            1259    99127    appprincipal_resultado    TABLE     �   CREATE TABLE appprincipal_resultado (
    id integer NOT NULL,
    verbo character varying(50) NOT NULL,
    contenido text NOT NULL,
    contexto text NOT NULL,
    proposito text NOT NULL,
    competencia_id integer NOT NULL
);
 *   DROP TABLE public.appprincipal_resultado;
       public         postgres    false    3            �            1259    99125    appprincipal_resultado_id_seq    SEQUENCE        CREATE SEQUENCE appprincipal_resultado_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.appprincipal_resultado_id_seq;
       public       postgres    false    3    210            Y	           0    0    appprincipal_resultado_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE appprincipal_resultado_id_seq OWNED BY appprincipal_resultado.id;
            public       postgres    false    209            �            1259    98940 
   auth_group    TABLE     ^   CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);
    DROP TABLE public.auth_group;
       public         postgres    false    3            �            1259    98938    auth_group_id_seq    SEQUENCE     s   CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public       postgres    false    192    3            Z	           0    0    auth_group_id_seq    SEQUENCE OWNED BY     9   ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;
            public       postgres    false    191            �            1259    98950    auth_group_permissions    TABLE     �   CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         postgres    false    3            �            1259    98948    auth_group_permissions_id_seq    SEQUENCE        CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public       postgres    false    194    3            [	           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;
            public       postgres    false    193            �            1259    98932    auth_permission    TABLE     �   CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         postgres    false    3            �            1259    98930    auth_permission_id_seq    SEQUENCE     x   CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public       postgres    false    3    190            \	           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;
            public       postgres    false    189            �            1259    98958 	   auth_user    TABLE     �  CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         postgres    false    3            �            1259    98968    auth_user_groups    TABLE     x   CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         postgres    false    3            �            1259    98966    auth_user_groups_id_seq    SEQUENCE     y   CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public       postgres    false    3    198            ]	           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;
            public       postgres    false    197            �            1259    98956    auth_user_id_seq    SEQUENCE     r   CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public       postgres    false    3    196            ^	           0    0    auth_user_id_seq    SEQUENCE OWNED BY     7   ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;
            public       postgres    false    195            �            1259    98976    auth_user_user_permissions    TABLE     �   CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         postgres    false    3            �            1259    98974 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public       postgres    false    200    3            _	           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;
            public       postgres    false    199            �            1259    99036    django_admin_log    TABLE     �  CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         postgres    false    3            �            1259    99034    django_admin_log_id_seq    SEQUENCE     y   CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public       postgres    false    202    3            `	           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;
            public       postgres    false    201            �            1259    98922    django_content_type    TABLE     �   CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         postgres    false    3            �            1259    98920    django_content_type_id_seq    SEQUENCE     |   CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public       postgres    false    3    188            a	           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;
            public       postgres    false    187            �            1259    98911    django_migrations    TABLE     �   CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         postgres    false    3            �            1259    98909    django_migrations_id_seq    SEQUENCE     z   CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public       postgres    false    3    186            b	           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;
            public       postgres    false    185            �            1259    99205    django_session    TABLE     �   CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         postgres    false    3            �            1259    99197    frontend_module    TABLE     �   CREATE TABLE frontend_module (
    id integer NOT NULL,
    label character varying(50) NOT NULL,
    installed boolean NOT NULL
);
 #   DROP TABLE public.frontend_module;
       public         postgres    false    3            �            1259    99195    frontend_module_id_seq    SEQUENCE     x   CREATE SEQUENCE frontend_module_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.frontend_module_id_seq;
       public       postgres    false    216    3            c	           0    0    frontend_module_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE frontend_module_id_seq OWNED BY frontend_module.id;
            public       postgres    false    215            Q           2604    107023 #   appprincipal_actividadevaluacion id    DEFAULT     �   ALTER TABLE ONLY appprincipal_actividadevaluacion ALTER COLUMN id SET DEFAULT nextval('appprincipal_indicadorevaluacion_id_seq'::regclass);
 R   ALTER TABLE public.appprincipal_actividadevaluacion ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    218    219    219            O           2604    99177    appprincipal_actividadf id    DEFAULT     �   ALTER TABLE ONLY appprincipal_actividadf ALTER COLUMN id SET DEFAULT nextval('appprincipal_actividaddeformacion_id_seq'::regclass);
 I   ALTER TABLE public.appprincipal_actividadf ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    214    213    214            L           2604    99112    appprincipal_competencia id    DEFAULT     |   ALTER TABLE ONLY appprincipal_competencia ALTER COLUMN id SET DEFAULT nextval('appprincipal_competencia_id_seq'::regclass);
 J   ALTER TABLE public.appprincipal_competencia ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    207    208    208            N           2604    99160    appprincipal_indicador id    DEFAULT     x   ALTER TABLE ONLY appprincipal_indicador ALTER COLUMN id SET DEFAULT nextval('appprincipal_indicador_id_seq'::regclass);
 H   ALTER TABLE public.appprincipal_indicador ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    212    211    212            K           2604    99068    appprincipal_profile id    DEFAULT     t   ALTER TABLE ONLY appprincipal_profile ALTER COLUMN id SET DEFAULT nextval('appprincipal_profile_id_seq'::regclass);
 F   ALTER TABLE public.appprincipal_profile ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    204    205    205            M           2604    99130    appprincipal_resultado id    DEFAULT     x   ALTER TABLE ONLY appprincipal_resultado ALTER COLUMN id SET DEFAULT nextval('appprincipal_resultado_id_seq'::regclass);
 H   ALTER TABLE public.appprincipal_resultado ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    209    210    210            D           2604    98943    auth_group id    DEFAULT     `   ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    191    192    192            E           2604    98953    auth_group_permissions id    DEFAULT     x   ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    194    193    194            C           2604    98935    auth_permission id    DEFAULT     j   ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    190    189    190            F           2604    98961    auth_user id    DEFAULT     ^   ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    196    195    196            G           2604    98971    auth_user_groups id    DEFAULT     l   ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    197    198    198            H           2604    98979    auth_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    199    200    200            I           2604    99039    django_admin_log id    DEFAULT     l   ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    202    201    202            B           2604    98925    django_content_type id    DEFAULT     r   ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    187    188    188            A           2604    98914    django_migrations id    DEFAULT     n   ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    186    185    186            P           2604    99200    frontend_module id    DEFAULT     j   ALTER TABLE ONLY frontend_module ALTER COLUMN id SET DEFAULT nextval('frontend_module_id_seq'::regclass);
 A   ALTER TABLE public.frontend_module ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    215    216    216            d	           0    0 (   appprincipal_actividaddeformacion_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('appprincipal_actividaddeformacion_id_seq', 1, false);
            public       postgres    false    213            L	          0    107020     appprincipal_actividadevaluacion 
   TABLE DATA               Z   COPY appprincipal_actividadevaluacion (id, nombre, descripcion, indicador_id) FROM stdin;
    public       postgres    false    219   ��       G	          0    99174    appprincipal_actividadf 
   TABLE DATA               Q   COPY appprincipal_actividadf (id, nombre, descripcion, resultado_id) FROM stdin;
    public       postgres    false    214   ��       A	          0    99109    appprincipal_competencia 
   TABLE DATA               N   COPY appprincipal_competencia (id, nombre, descripcion, curso_id) FROM stdin;
    public       postgres    false    208   ��       e	           0    0    appprincipal_competencia_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('appprincipal_competencia_id_seq', 1, false);
            public       postgres    false    207            <	          0    99058    appprincipal_curso 
   TABLE DATA               �   COPY appprincipal_curso (codigo, nombre, creditos, horas_clase_magistral, horas_estudio_independiente, tipo_curso, validable, habilitable, semestre, docente_id, programa_id) FROM stdin;
    public       postgres    false    203   �       E	          0    99157    appprincipal_indicador 
   TABLE DATA               [   COPY appprincipal_indicador (id, habilidad, contenido, contexto, resultado_id) FROM stdin;
    public       postgres    false    212   n�       f	           0    0    appprincipal_indicador_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('appprincipal_indicador_id_seq', 1, false);
            public       postgres    false    211            g	           0    0 '   appprincipal_indicadorevaluacion_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('appprincipal_indicadorevaluacion_id_seq', 1, false);
            public       postgres    false    218            >	          0    99065    appprincipal_profile 
   TABLE DATA               :   COPY appprincipal_profile (id, tipo, user_id) FROM stdin;
    public       postgres    false    205   ��       h	           0    0    appprincipal_profile_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('appprincipal_profile_id_seq', 4, true);
            public       postgres    false    204            ?	          0    99076    appprincipal_programa 
   TABLE DATA               �   COPY appprincipal_programa (codigo, nombre_programa, escuela, numero_semestres, numero_creditos_graduacion, director_id) FROM stdin;
    public       postgres    false    206   ��       C	          0    99127    appprincipal_resultado 
   TABLE DATA               d   COPY appprincipal_resultado (id, verbo, contenido, contexto, proposito, competencia_id) FROM stdin;
    public       postgres    false    210   '�       i	           0    0    appprincipal_resultado_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('appprincipal_resultado_id_seq', 1, false);
            public       postgres    false    209            1	          0    98940 
   auth_group 
   TABLE DATA               '   COPY auth_group (id, name) FROM stdin;
    public       postgres    false    192   D�       j	           0    0    auth_group_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('auth_group_id_seq', 1, false);
            public       postgres    false    191            3	          0    98950    auth_group_permissions 
   TABLE DATA               F   COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public       postgres    false    194   a�       k	           0    0    auth_group_permissions_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);
            public       postgres    false    193            /	          0    98932    auth_permission 
   TABLE DATA               G   COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
    public       postgres    false    190   ~�       l	           0    0    auth_permission_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('auth_permission_id_seq', 48, true);
            public       postgres    false    189            5	          0    98958 	   auth_user 
   TABLE DATA               �   COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public       postgres    false    196   ��       7	          0    98968    auth_user_groups 
   TABLE DATA               :   COPY auth_user_groups (id, user_id, group_id) FROM stdin;
    public       postgres    false    198   ��       m	           0    0    auth_user_groups_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);
            public       postgres    false    197            n	           0    0    auth_user_id_seq    SEQUENCE SET     7   SELECT pg_catalog.setval('auth_user_id_seq', 4, true);
            public       postgres    false    195            9	          0    98976    auth_user_user_permissions 
   TABLE DATA               I   COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public       postgres    false    200   ��       o	           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);
            public       postgres    false    199            ;	          0    99036    django_admin_log 
   TABLE DATA               �   COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public       postgres    false    202   ��       p	           0    0    django_admin_log_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);
            public       postgres    false    201            -	          0    98922    django_content_type 
   TABLE DATA               <   COPY django_content_type (id, app_label, model) FROM stdin;
    public       postgres    false    188   ��       q	           0    0    django_content_type_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('django_content_type_id_seq', 16, true);
            public       postgres    false    187            +	          0    98911    django_migrations 
   TABLE DATA               <   COPY django_migrations (id, app, name, applied) FROM stdin;
    public       postgres    false    186   ��       r	           0    0    django_migrations_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('django_migrations_id_seq', 27, true);
            public       postgres    false    185            J	          0    99205    django_session 
   TABLE DATA               I   COPY django_session (session_key, session_data, expire_date) FROM stdin;
    public       postgres    false    217   �       I	          0    99197    frontend_module 
   TABLE DATA               8   COPY frontend_module (id, label, installed) FROM stdin;
    public       postgres    false    216   *�       s	           0    0    frontend_module_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('frontend_module_id_seq', 1, false);
            public       postgres    false    215            �           2606    99182 >   appprincipal_actividadf appprincipal_actividaddeformacion_pkey 
   CONSTRAINT     u   ALTER TABLE ONLY appprincipal_actividadf
    ADD CONSTRAINT appprincipal_actividaddeformacion_pkey PRIMARY KEY (id);
 h   ALTER TABLE ONLY public.appprincipal_actividadf DROP CONSTRAINT appprincipal_actividaddeformacion_pkey;
       public         postgres    false    214    214            �           2606    99117 6   appprincipal_competencia appprincipal_competencia_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY appprincipal_competencia
    ADD CONSTRAINT appprincipal_competencia_pkey PRIMARY KEY (id);
 `   ALTER TABLE ONLY public.appprincipal_competencia DROP CONSTRAINT appprincipal_competencia_pkey;
       public         postgres    false    208    208            �           2606    99062 *   appprincipal_curso appprincipal_curso_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY appprincipal_curso
    ADD CONSTRAINT appprincipal_curso_pkey PRIMARY KEY (codigo);
 T   ALTER TABLE ONLY public.appprincipal_curso DROP CONSTRAINT appprincipal_curso_pkey;
       public         postgres    false    203    203            �           2606    99165 2   appprincipal_indicador appprincipal_indicador_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY appprincipal_indicador
    ADD CONSTRAINT appprincipal_indicador_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.appprincipal_indicador DROP CONSTRAINT appprincipal_indicador_pkey;
       public         postgres    false    212    212            �           2606    107028 F   appprincipal_actividadevaluacion appprincipal_indicadorevaluacion_pkey 
   CONSTRAINT     }   ALTER TABLE ONLY appprincipal_actividadevaluacion
    ADD CONSTRAINT appprincipal_indicadorevaluacion_pkey PRIMARY KEY (id);
 p   ALTER TABLE ONLY public.appprincipal_actividadevaluacion DROP CONSTRAINT appprincipal_indicadorevaluacion_pkey;
       public         postgres    false    219    219            �           2606    99073 .   appprincipal_profile appprincipal_profile_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY appprincipal_profile
    ADD CONSTRAINT appprincipal_profile_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.appprincipal_profile DROP CONSTRAINT appprincipal_profile_pkey;
       public         postgres    false    205    205            �           2606    99075 5   appprincipal_profile appprincipal_profile_user_id_key 
   CONSTRAINT     l   ALTER TABLE ONLY appprincipal_profile
    ADD CONSTRAINT appprincipal_profile_user_id_key UNIQUE (user_id);
 _   ALTER TABLE ONLY public.appprincipal_profile DROP CONSTRAINT appprincipal_profile_user_id_key;
       public         postgres    false    205    205            �           2606    99080 0   appprincipal_programa appprincipal_programa_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY appprincipal_programa
    ADD CONSTRAINT appprincipal_programa_pkey PRIMARY KEY (codigo);
 Z   ALTER TABLE ONLY public.appprincipal_programa DROP CONSTRAINT appprincipal_programa_pkey;
       public         postgres    false    206    206            �           2606    99135 2   appprincipal_resultado appprincipal_resultado_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY appprincipal_resultado
    ADD CONSTRAINT appprincipal_resultado_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.appprincipal_resultado DROP CONSTRAINT appprincipal_resultado_pkey;
       public         postgres    false    210    210            _           2606    98947    auth_group auth_group_name_key 
   CONSTRAINT     R   ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public         postgres    false    192    192            d           2606    99002 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public         postgres    false    194    194    194            g           2606    98955 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public         postgres    false    194    194            a           2606    98945    auth_group auth_group_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public         postgres    false    192    192            Z           2606    98988 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public         postgres    false    190    190    190            \           2606    98937 $   auth_permission auth_permission_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public         postgres    false    190    190            o           2606    98973 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public         postgres    false    198    198            r           2606    99017 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public         postgres    false    198    198    198            i           2606    98963    auth_user auth_user_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public         postgres    false    196    196            u           2606    98981 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public         postgres    false    200    200            x           2606    99031 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public         postgres    false    200    200    200            l           2606    99190     auth_user auth_user_username_key 
   CONSTRAINT     X   ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public         postgres    false    196    196            {           2606    99045 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public         postgres    false    202    202            U           2606    98929 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public         postgres    false    188    188    188            W           2606    98927 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public         postgres    false    188    188            S           2606    98919 (   django_migrations django_migrations_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public         postgres    false    186    186            �           2606    99212 "   django_session django_session_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public         postgres    false    217    217            �           2606    99202 $   frontend_module frontend_module_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY frontend_module
    ADD CONSTRAINT frontend_module_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.frontend_module DROP CONSTRAINT frontend_module_pkey;
       public         postgres    false    216    216            �           1259    99188 7   appprincipal_actividaddeformacion_resultado_id_94118ad7    INDEX     |   CREATE INDEX appprincipal_actividaddeformacion_resultado_id_94118ad7 ON appprincipal_actividadf USING btree (resultado_id);
 K   DROP INDEX public.appprincipal_actividaddeformacion_resultado_id_94118ad7;
       public         postgres    false    214            �           1259    99123 *   appprincipal_competencia_curso_id_622831e2    INDEX     l   CREATE INDEX appprincipal_competencia_curso_id_622831e2 ON appprincipal_competencia USING btree (curso_id);
 >   DROP INDEX public.appprincipal_competencia_curso_id_622831e2;
       public         postgres    false    208            �           1259    99124 /   appprincipal_competencia_curso_id_622831e2_like    INDEX     �   CREATE INDEX appprincipal_competencia_curso_id_622831e2_like ON appprincipal_competencia USING btree (curso_id varchar_pattern_ops);
 C   DROP INDEX public.appprincipal_competencia_curso_id_622831e2_like;
       public         postgres    false    208            }           1259    99086 '   appprincipal_curso_codigo_27dca65b_like    INDEX     u   CREATE INDEX appprincipal_curso_codigo_27dca65b_like ON appprincipal_curso USING btree (codigo varchar_pattern_ops);
 ;   DROP INDEX public.appprincipal_curso_codigo_27dca65b_like;
       public         postgres    false    203            ~           1259    99087 &   appprincipal_curso_docente_id_0010d4d8    INDEX     d   CREATE INDEX appprincipal_curso_docente_id_0010d4d8 ON appprincipal_curso USING btree (docente_id);
 :   DROP INDEX public.appprincipal_curso_docente_id_0010d4d8;
       public         postgres    false    203            �           1259    99100 '   appprincipal_curso_programa_id_21618ff8    INDEX     f   CREATE INDEX appprincipal_curso_programa_id_21618ff8 ON appprincipal_curso USING btree (programa_id);
 ;   DROP INDEX public.appprincipal_curso_programa_id_21618ff8;
       public         postgres    false    203            �           1259    99101 ,   appprincipal_curso_programa_id_21618ff8_like    INDEX        CREATE INDEX appprincipal_curso_programa_id_21618ff8_like ON appprincipal_curso USING btree (programa_id varchar_pattern_ops);
 @   DROP INDEX public.appprincipal_curso_programa_id_21618ff8_like;
       public         postgres    false    203            �           1259    99171 ,   appprincipal_indicador_resultado_id_60121364    INDEX     p   CREATE INDEX appprincipal_indicador_resultado_id_60121364 ON appprincipal_indicador USING btree (resultado_id);
 @   DROP INDEX public.appprincipal_indicador_resultado_id_60121364;
       public         postgres    false    212            �           1259    107034 6   appprincipal_indicadorevaluacion_indicador_id_9642db19    INDEX     �   CREATE INDEX appprincipal_indicadorevaluacion_indicador_id_9642db19 ON appprincipal_actividadevaluacion USING btree (indicador_id);
 J   DROP INDEX public.appprincipal_indicadorevaluacion_indicador_id_9642db19;
       public         postgres    false    219            �           1259    99098 *   appprincipal_programa_codigo_834d7579_like    INDEX     {   CREATE INDEX appprincipal_programa_codigo_834d7579_like ON appprincipal_programa USING btree (codigo varchar_pattern_ops);
 >   DROP INDEX public.appprincipal_programa_codigo_834d7579_like;
       public         postgres    false    206            �           1259    99099 *   appprincipal_programa_director_id_cc7ac78b    INDEX     l   CREATE INDEX appprincipal_programa_director_id_cc7ac78b ON appprincipal_programa USING btree (director_id);
 >   DROP INDEX public.appprincipal_programa_director_id_cc7ac78b;
       public         postgres    false    206            �           1259    99149 .   appprincipal_resultado_competencia_id_7c217458    INDEX     t   CREATE INDEX appprincipal_resultado_competencia_id_7c217458 ON appprincipal_resultado USING btree (competencia_id);
 B   DROP INDEX public.appprincipal_resultado_competencia_id_7c217458;
       public         postgres    false    210            ]           1259    98990    auth_group_name_a6ea08ec_like    INDEX     a   CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public         postgres    false    192            b           1259    99003 (   auth_group_permissions_group_id_b120cbf9    INDEX     h   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public         postgres    false    194            e           1259    99004 -   auth_group_permissions_permission_id_84c5c92e    INDEX     r   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public         postgres    false    194            X           1259    98989 (   auth_permission_content_type_id_2f476e4b    INDEX     h   CREATE INDEX auth_permission_content_type_id_2f476e4b ON auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public         postgres    false    190            m           1259    99019 "   auth_user_groups_group_id_97559544    INDEX     \   CREATE INDEX auth_user_groups_group_id_97559544 ON auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public         postgres    false    198            p           1259    99018 !   auth_user_groups_user_id_6a12ed8b    INDEX     Z   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public         postgres    false    198            s           1259    99033 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     z   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public         postgres    false    200            v           1259    99032 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     n   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public         postgres    false    200            j           1259    99191     auth_user_username_6821ab7c_like    INDEX     g   CREATE INDEX auth_user_username_6821ab7c_like ON auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public         postgres    false    196            y           1259    99056 )   django_admin_log_content_type_id_c4bce8eb    INDEX     j   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public         postgres    false    202            |           1259    99057 !   django_admin_log_user_id_c564eba6    INDEX     Z   CREATE INDEX django_admin_log_user_id_c564eba6 ON django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public         postgres    false    202            �           1259    99214 #   django_session_expire_date_a5c62663    INDEX     ^   CREATE INDEX django_session_expire_date_a5c62663 ON django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public         postgres    false    217            �           1259    99213 (   django_session_session_key_c0390e0f_like    INDEX     w   CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public         postgres    false    217            �           1259    99203    frontend_module_label_58c52d82    INDEX     T   CREATE INDEX frontend_module_label_58c52d82 ON frontend_module USING btree (label);
 2   DROP INDEX public.frontend_module_label_58c52d82;
       public         postgres    false    216            �           1259    99204 #   frontend_module_label_58c52d82_like    INDEX     m   CREATE INDEX frontend_module_label_58c52d82_like ON frontend_module USING btree (label varchar_pattern_ops);
 7   DROP INDEX public.frontend_module_label_58c52d82_like;
       public         postgres    false    216            �           2606    99183 O   appprincipal_actividadf appprincipal_activid_resultado_id_94118ad7_fk_appprinci    FK CONSTRAINT     �   ALTER TABLE ONLY appprincipal_actividadf
    ADD CONSTRAINT appprincipal_activid_resultado_id_94118ad7_fk_appprinci FOREIGN KEY (resultado_id) REFERENCES appprincipal_resultado(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.appprincipal_actividadf DROP CONSTRAINT appprincipal_activid_resultado_id_94118ad7_fk_appprinci;
       public       postgres    false    2193    210    214            �           2606    99144 L   appprincipal_competencia appprincipal_compete_curso_id_622831e2_fk_appprinci    FK CONSTRAINT     �   ALTER TABLE ONLY appprincipal_competencia
    ADD CONSTRAINT appprincipal_compete_curso_id_622831e2_fk_appprinci FOREIGN KEY (curso_id) REFERENCES appprincipal_curso(codigo) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.appprincipal_competencia DROP CONSTRAINT appprincipal_compete_curso_id_622831e2_fk_appprinci;
       public       postgres    false    2176    208    203            �           2606    99081 I   appprincipal_curso appprincipal_curso_docente_id_0010d4d8_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY appprincipal_curso
    ADD CONSTRAINT appprincipal_curso_docente_id_0010d4d8_fk_auth_user_id FOREIGN KEY (docente_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.appprincipal_curso DROP CONSTRAINT appprincipal_curso_docente_id_0010d4d8_fk_auth_user_id;
       public       postgres    false    196    203    2153            �           2606    99102 G   appprincipal_curso appprincipal_curso_programa_id_21618ff8_fk_appprinci    FK CONSTRAINT     �   ALTER TABLE ONLY appprincipal_curso
    ADD CONSTRAINT appprincipal_curso_programa_id_21618ff8_fk_appprinci FOREIGN KEY (programa_id) REFERENCES appprincipal_programa(codigo) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.appprincipal_curso DROP CONSTRAINT appprincipal_curso_programa_id_21618ff8_fk_appprinci;
       public       postgres    false    2186    203    206            �           2606    107029 X   appprincipal_actividadevaluacion appprincipal_indicad_indicador_id_9642db19_fk_appprinci    FK CONSTRAINT     �   ALTER TABLE ONLY appprincipal_actividadevaluacion
    ADD CONSTRAINT appprincipal_indicad_indicador_id_9642db19_fk_appprinci FOREIGN KEY (indicador_id) REFERENCES appprincipal_indicador(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.appprincipal_actividadevaluacion DROP CONSTRAINT appprincipal_indicad_indicador_id_9642db19_fk_appprinci;
       public       postgres    false    212    2195    219            �           2606    99166 N   appprincipal_indicador appprincipal_indicad_resultado_id_60121364_fk_appprinci    FK CONSTRAINT     �   ALTER TABLE ONLY appprincipal_indicador
    ADD CONSTRAINT appprincipal_indicad_resultado_id_60121364_fk_appprinci FOREIGN KEY (resultado_id) REFERENCES appprincipal_resultado(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.appprincipal_indicador DROP CONSTRAINT appprincipal_indicad_resultado_id_60121364_fk_appprinci;
       public       postgres    false    2193    210    212            �           2606    99088 J   appprincipal_profile appprincipal_profile_user_id_22b9693a_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY appprincipal_profile
    ADD CONSTRAINT appprincipal_profile_user_id_22b9693a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.appprincipal_profile DROP CONSTRAINT appprincipal_profile_user_id_22b9693a_fk_auth_user_id;
       public       postgres    false    196    2153    205            �           2606    99093 P   appprincipal_programa appprincipal_programa_director_id_cc7ac78b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY appprincipal_programa
    ADD CONSTRAINT appprincipal_programa_director_id_cc7ac78b_fk_auth_user_id FOREIGN KEY (director_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.appprincipal_programa DROP CONSTRAINT appprincipal_programa_director_id_cc7ac78b_fk_auth_user_id;
       public       postgres    false    2153    196    206            �           2606    99150 P   appprincipal_resultado appprincipal_resulta_competencia_id_7c217458_fk_appprinci    FK CONSTRAINT     �   ALTER TABLE ONLY appprincipal_resultado
    ADD CONSTRAINT appprincipal_resulta_competencia_id_7c217458_fk_appprinci FOREIGN KEY (competencia_id) REFERENCES appprincipal_competencia(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.appprincipal_resultado DROP CONSTRAINT appprincipal_resulta_competencia_id_7c217458_fk_appprinci;
       public       postgres    false    210    2190    208            �           2606    98996 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public       postgres    false    194    190    2140            �           2606    98991 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public       postgres    false    192    2145    194            �           2606    98982 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public       postgres    false    190    188    2135            �           2606    99011 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public       postgres    false    192    2145    198            �           2606    99006 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public       postgres    false    2153    198    196            �           2606    99025 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public       postgres    false    200    190    2140            �           2606    99020 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public       postgres    false    200    2153    196            �           2606    99046 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public       postgres    false    188    2135    202            �           2606    99051 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public       postgres    false    2153    202    196            L	      x������ � �      G	      x������ � �      A	      x������ � �      <	   Y   x�342�LN�I.�)-V(��,K��)�+-�4BN�����ĒҢD������D��L2�s�	Bn~�)F`��L1������ ��)p      E	      x������ � �      >	   :   x�3�L�,JM.�/�4�2�,(�OK-rL�9Sr3�8��8SR���9��b���� ���      ?	   B   x�342�,(*MMJ���KO��L-�L�44�445�4�2271�,IM����O�DQc�ihR���� ��|      C	      x������ � �      1	      x������ � �      3	      x������ � �      /	     x�m�[�� E�a^A+����FK#d�4�c{��R�~(�V:.8pJ�����B�c1n[���_�-K?7|��n�t(��<1���%u�u��NF��@�lБ�D�EO���]w�ZTQ�Kٿ�"�u����"���S�||�c=���jQ�C�#R)v���'�x����x�R�lǴ�q�o"�R��r� ��%9�mR�y��9�D�թ��C5r��G5�����z����X�D��i�&��9J~�6�ij�2�0-��̻����})�
���=�5��$s&�|׍{�m��,�ᶧY���#�<����{p����X���r_����30�u�!1*Y��8�B<=�e��)N�",�"A�@��~��5�����Jz�~�9$���`N�7Z�����aAί̈́�W!����/�H�8�_��5ru���2g��]��5K���.R,�2E�H�Z�3T�v����h(�M�5˪_|�k\�2�ג�ܸ�} �[O����<J򔬻���W��nп���k���R��,�0      5	   �  x�u�k��0�?ï����ԶP($�x�UW��c�l��ܼ e(��_0&��8MӜ�漧O�jR�=z�#v��`=����oS�w�ƨ;�]Їvm��8��qr\�&;u�����gI�>K"��'�+H�4�����*K�@:,��բ,Y2q�3����w<��>.�����(R ��i!�v�Y}�p�|$ic�N�Z�[��\./���2`1i�m�2��m�l��֛���r��vY��k:2n�׫�����c� ��J��U�֪2z�՛-��Ll�F�o��zg�;�q��G�{���`C&~��T&�y��Э��J�fh��k�\b^�O$;Rr��{~���wYq?KX�q����,�y��KE>𽢢�4�!��bR���ӫS�1������E3��L�骫ao�����4�`Q~�i��&�v'�c�V�ݜ����Y\c�1�1��쭦
�����Ӡ�*��,���7      7	      x������ � �      9	      x������ � �      ;	      x������ � �      -	   �   x�u�MjC1���aJ���w�F�z��Re;���M��t��F#a 3s�Q�r�Û�~�u��p��W�Bp|��b�y*���rn#wJ
�!5I���ukP�r�Di��@�HYW�ݯ�h��`�EZ���;Z]��]��������ո��������1,~�I�h�~<=?����4�
x��8_(�?�/ �{���      +	   C  x���[��0E��U�b��;k) �&�We;�쾒�z2c�>,�C�$T�8,nX����!���mW!u%�
�ȍ���H$��_�����L!k�)�I@+��~8WpM��$a�4�x�y�\?>���Gc۶��1A�Wv�����O1�ItUS�4�
�A����E�o�j��@���[�IF8r��"D��*'�˟�n��X�J&x��R�->"��	`|�r���^�?�3`9��X�,����n�}�m�89�I���G})E�ؓ%+u�a�%��Vǿ���0���we��uf�����nq�L.�~�c5`z��tn�ǿ�,΅�\�;�>Y��[ߝbb�1�1bǰWL:rB��e�Ԉ23��ௌ��K?k[���D�&����N��_����z�l�Q��;D>Sy�.��2�9M�q!���n��ݕ+���I�ˊ�8Ut��g)4�|F�I������<ۍX���K{��t��r��B���xP��H�ږ5�f���l�#���t{J<.O�_d�6�����V���q��&}݅� R^�`M4%js��Q��0�㔗(����?���� ���      J	     x�͔͎�8Fש����68@�Y$m���F� ��l$c'�L*�<}�^��3��L/Xز���C�|U]`�~�j������D7�~9C��x~hD�dBv�i�G�)i�$�Z��d5a/�'�IFv����@V����Fq�^N��I�����9��"y��L�:hx�"�m�n���0��a��Ny�ɏp���>W�h��p+9z���o_���6,�a8")KTOw�	��hOǽb�B�1�wS�K�l�j��
;e��Ä�}|���;X�#��%t�`1w��c��[頃��_��,���jq��OR?N3[�i�3[S�	�TQ(Lٴŀ"���膪��/ف��ݶ�� ���\ň�0d������1�xG���������';�����xxn�L�n�Ǉ�u�����Y-����;�_��U�3:���!��F3����c��6�bW�̎�4�6B�H��&I��~+� �#DJ�V��C������Q���!I�-�}��������gt��%F�
�b��+hڠB唲���xb}	.����0�Jq��
�<�uWXD1i���V�Rb>f���31f�����@�Z��CF8��hYj�W՘�1�u\�,�M��EQ�ؾ~��_�b��.�>���'v����n�~�纩?ow�+c�~Q�<��lHjXkcO����6ҽLr:�h/Y�5����o���dC�>�LG���c�Q�n� ��i��M�	����w����p}ob������;sc      I	      x������ � �     