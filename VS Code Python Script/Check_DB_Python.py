with engine.connect() as conn:
    result = conn.execute(db.text("SHOW DATABASES"))
    print([r[0] for r in result])
