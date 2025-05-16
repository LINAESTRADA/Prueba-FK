import os
import logging
from flask import Blueprint, request, render_template, redirect, url_for
from models import db, EventLog
from datetime import datetime


if not os.path.exists('logs'):
    os.makedirs('logs')


logging.basicConfig(filename='logs/app.log', level=logging.ERROR)

bp = Blueprint('main', __name__)

@bp.route('/api/register', methods=['POST'])
def api_register_event():
    try:
        data = request.json
        event = EventLog(description=data['description'], event_type='api')
        db.session.add(event)
        db.session.commit()
        return {'message': 'Event registered successfully'}, 201
    except Exception as e:
        logging.error(f"API register error: {e}")
        return {'error': 'Internal Server Error'}, 500

@bp.route('/form/register', methods=['GET', 'POST'])
def form_register_event():
    if request.method == 'POST':
        try:
            description = request.form['description']
            event = EventLog(description=description, event_type='manual')
            db.session.add(event)
            db.session.commit()
            return redirect(url_for('main.query_events'))
        except Exception as e:
            logging.error(f"Form register error: {e}")
            return "Error al registrar el evento", 500
    return render_template('register.html')

@bp.route('/events', methods=['GET', 'POST'])
def query_events():
    events = []
    if request.method == 'POST':
        try:
            event_type = request.form.get('event_type')
            start_date = datetime.strptime(request.form.get('start_date'), "%Y-%m-%d")
            end_date = datetime.strptime(request.form.get('end_date'), "%Y-%m-%d")

            query = EventLog.query.filter(EventLog.timestamp.between(start_date, end_date))
            if event_type:
                query = query.filter_by(event_type=event_type)

            events = query.all()
        except Exception as e:
            logging.error(f"Query error: {e}")
            return "Error en la consulta", 500
    return render_template('query.html', events=events)