from flask import Flask,jsonify,request
app = Flask(__name__)
posts ={}
count = 1;

@app.route("/posts",methods=["GET"])
def get_posts():
    return jsonify(list(posts.values()))


@app.route("/posts",methods=["POST"])
def add_posts():
   global count
   data = request.get_json()
   username = data.get('username')
   caption = data.get('caption')

   post = {
       'id':count,
       'username':username,
       'caption':caption,
       'likes':0,
       'comments':[]
   }
   posts[count] = post
   count +=1
   return jsonify(post),201

@app.route("/posts/<int:post_id>", methods =["DELETE"])
def delete_post(post_id):
 if post_id in posts:
    del posts[post_id]
    return jsonify({"message":"Post deleted Successfully"})
 else:
    return jsonify({"message":"Error occured while Deleting"})
 
if __name__ == "__main__":
    app.run(debug=True)