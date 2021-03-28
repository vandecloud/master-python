CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuarios(
    id            int(25) auto_increment NOT NULL,
    nombre    varchar(100),
    apellidos varchar(100),
    email     varchar(255) NOT NULL,
    password  varchar(255) NOT NULL,
    fecha     date NOT NULL
    CONSTRAINT pk_usuarios PRIMARY KEY (id)
    CONSTRAINT uq_email UNIQUE(email)
)   ENGINE =InnoDb;

CREATE TABLE notas(
    id          int (25) auto_increment NOT NULL,
    usuario_id  int (25) NOT NULL,
    titulo      varchar(255) NOT NULL,
    descripcion MEDIUMTEXT,
    fecha       date NOT NULLM
    CONSTRAINT pk_notas PRIMARY KEY(id)
    CONSTRAINT fk_nota_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)

)    ENGINE =InnoDb;



CREATE TABLE url(
    id              int(25) auto_increment NOT NULL,
    original_url    varchar(512),
    short_url       varchar(6),
    visits          int(255) NOT NULL,
    data_create     date NOT NULL
    CONSTRAINT pk_url PRIMARY KEY (id)
    CONSTRAINT uq_short_url UNIQUE(short_url)
)   ENGINE =InnoDb;

id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(3), unique=True)
    visits = db.Column (db.Integer, default=0)
    data_created = db.Column (db.DateTime, default=datetime.now)