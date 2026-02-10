from flask.cli import FlaskGroup
from werkzeug.security import generate_password_hash
from app import app, db
from app.models.contact import Contact
from migrate_anime import do_migrate_anime


cli = FlaskGroup(app)    

@cli.command("seed_db")
def seed_db():
    db.session.add(AuthUser(email="flask@204212", name='สมชาย ทรงแบด',
                            password=generate_password_hash('1234',
                                                            method='sha256'),
                            avatar_url='https://ui-avatars.com/api/?name=\
สมชาย+ทรงแบด&background=83ee03&color=fff'))
    db.session.add(
        Contact(firstname='สมชาย', lastname='ทรงแบด', phone='081-111-1111'))
    db.session.commit()


from migrate_anime import do_migrate_anime


@cli.command("migrate_anime")
def migrate_anime():
   do_migrate_anime()




@cli.command("seed_db")
def seed_db():
   # Call migrate_anime as part of seeding
   do_migrate_anime()