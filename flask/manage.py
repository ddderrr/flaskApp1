from migrate_anime import do_migrate_anime


@cli.command("migrate_anime")
def migrate_anime():
   do_migrate_anime()




@cli.command("seed_db")
def seed_db():
   # Call migrate_anime as part of seeding
   do_migrate_anime()