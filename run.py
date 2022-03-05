import os
from thebuzz import app, db


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True)
