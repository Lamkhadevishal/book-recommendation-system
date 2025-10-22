from flask import Flask,render_template
import pickle
popular_df= pickle.load(open('popular.pkl','rb'))
pt=pickle.load(open("pt.pkl",'rb'))
book=pickle.load(open('book.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))



app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           Votes=list(popular_df['num_of_rating'].values),
                           rating=list(popular_df['avg_of_rating'].values)
    )
@app.route("/recommend")
def recommend_ui():
    return render_template("recommend.html")
@app.route('/recommend_books')
def recommend():
   return 
    


if __name__=='__main__':
    app.run(debug=True)