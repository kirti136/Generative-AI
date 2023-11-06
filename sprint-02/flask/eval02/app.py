from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data structure for posts
posts = []
post_id_counter = 1

# Create a post
@app.route('/create_post', methods=['POST'])
def create_post():
    global post_id_counter
    data = request.get_json()
    if 'username' in data and 'caption' in data:
        post = {
            'id': post_id_counter,
            'username': data['username'],
            'caption': data['caption'],
            'likes': 0,
            'comments': []
        }
        post_id_counter += 1
        posts.append(post)
        return jsonify({'message': 'Post created successfully'}), 201
    else:
        return jsonify({'error': 'Invalid data'}), 400

# View all posts
@app.route('/view_posts', methods=['GET'])
def view_posts():
    return jsonify(posts)

# Delete a post by ID
@app.route('/delete_post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        posts.remove(post)
        return jsonify({'message': 'Post deleted successfully'}), 200
    else:
        return jsonify({'error': 'Post not found'}), 404

# Like a post
@app.route('/like_post/<int:post_id>', methods=['PUT'])
def like_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        post['likes'] += 1
        return jsonify({'message': 'Liked the post'}), 200
    else:
        return jsonify({'error': 'Post not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
