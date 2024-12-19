from flask import render_template, request, redirect, url_for
from app import app, db
from models import MovieReview

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    reviews = MovieReview.query.order_by(MovieReview.time_created.desc()).all()
    return render_template('data.html', reviews=reviews)


@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        new_review = MovieReview(
            movie_name=request.form['movie_name'],
            review=request.form['review'],
            rating=float(request.form['rating'])
        )
        
        db.session.add(new_review)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('add_review.html')
