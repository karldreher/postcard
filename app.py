import flask
import db




@app.route('/', methods=['GET'])
    return render_template('index.html')

@app.route('/<string:username>/<string:postcard_id>', methods=['GET'])
def redirect(postcard_id):
    user = #get user_id from username
    postcard = #get card from postcards WHERE user_id=user
    return render_template('redirection_page.html', url=url)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
