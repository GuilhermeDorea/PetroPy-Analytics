'''API Functions for handle the analytics requests'''
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# Db settings, no tracking for development purposes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gas_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Station(db.Model):
    '''Gas stations class, based on data loaded from the db'''
    id = db.Column(db.Integer, primary_key=True)
    regions = db.Column(db.String(100), nullable=False)
    states = db.Column(db.String(100), nullable=False)
    gas_station = db.Column(db.String(100), nullable=False)
    diesel = db.Column(db.Float, nullable=False)
    diesel_s10 = db.Column(db.Float, nullable=False)
    ethanol = db.Column(db.Float, nullable=False)
    gas = db.Column(db.Float, nullable=False)
    addgas = db.Column(db.Float, nullable=False)
    cng = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Produto {self.nome}>'
    
    def to_dict(self):
        """Converte o objeto Station para um dicionário."""
        return {
            'id': self.id,
            'regions': self.regions,
            'states': self.states,
            'gas': self.gas,
            'addgas': self.addgas,
            'ethanol': self.ethanol,
            'cng': self.cng,
            'diesel': self.diesel,
            'diesel_s10': self.diesel_s10
        }

def sql_mean(uf):
    '''Returns the state mean values per gas station'''
    query = text('''
                 SELECT
                    AVG(addgas) as addgas_mean,
                    AVG(gas) as gas_mean,
                    AVG(ethanol) as ethanol_mean,
                    AVG(cng) as cng_mean,
                    AVG(diesel) as diesel_mean,
                    AVG(diesel_s10) as diesel_s10_mean
                 FROM
                    station
                 WHERE
                     states = :state
                 
                 ''')
    
    result = db.session.execute(query,{'state':uf.upper()}).first()
    mean_prices = {"gas": round(result.gas_mean,2) if result.gas_mean else None,
                   "addgas": round(result.addgas_mean,2) if result.addgas_mean else None,
                   "ethanol": round(result.ethanol_mean,2) if result.ethanol_mean else None,
                   "cng": round(result.cng_mean,2) if result.cng_mean else None,
                   "diesel": round(result.diesel_mean,2) if result.diesel_mean else None,
                   "diesel_s10": round(result.diesel_s10_mean,2) if result.diesel_s10_mean else None}
    return jsonify({'state':uf.upper(), 'mean_prices':mean_prices})

# GET State mean
@app.route('/stations/<string:state>', methods=['GET'])
def get_state_mean(state):
    '''Get info from a ID (useless, only for development purposes)'''
    state_mean = sql_mean(state)
    return state_mean

# GET single ID
@app.route('/stations/<int:station_id>', methods=['GET'])
def get_station(station_id):
    '''Get info from a ID (useless, only for development purposes)'''
    station = Station.query.get_or_404(station_id) # get_or_404 já trata o erro se não encontrar
    return jsonify(station.to_dict())

app.run(port=5000,host='localhost', debug=True)
