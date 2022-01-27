from flask import Flask,jsonify,request
import csv

all_movies=[]

with open('movies.csv') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]

liked_movies=[]
disliked_movies=[]
not_watched=[]

app=Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":"success"
    })

@app.route("/liked-movie",methods=["POST"])
def liked_movie():
    movie=all_movies[0]
    some_movies=all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/disliked-movie",methods=["POST"])
def disliked_movie():
    movie=all_movies[0]
    some_movies=all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/not-watched",methods=["POST"])
def not_watched():
    movie=all_movies[0]
    some_movies=all_movies[1:]
    not_watched.append(movie)
    return jsonify({
        "status":"success"
    }),201

if __name__ == "__main__":
    app.run()    
