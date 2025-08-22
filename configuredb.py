from api_manager import app, db  # Importe o app e o objeto db do seu arquivo principal
with app.app_context():
    db.create_all()

exit()