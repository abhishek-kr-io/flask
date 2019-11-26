
# Boilerplate code start here..
# create a flash application instance
from flask import Flask,render_template,request,redirect, url_for, jsonify
app = Flask(__name__)

# Boilerplate code ends here..


#Simulate a pseudo database here 
shopping_list= ['Milk','Cheese','Curd','Coke','Rice']
# We will use template to display this shopping list. 
# templates have place holders to show webpages,dynamic contents.. 

@app.route('/', methods=['GET','POST'])
def index():
    global shopping_list
    if request.method=="POST":
        shopping_list.append(request.form['item'])

   # return '<h1>Shopping list</h1>'    #not so efficient if you have lot of HTML 
   #Better way is to use template as below
    #return render_template('index.html') 
    return render_template('index.html', items=shopping_list)  #passing shopping_list to template. 



@app.route('/remove/<name>')
def remove_item(name):
    global shopping_list
    if name in shopping_list:
        shopping_list.remove(name)
    return redirect(url_for('index'))




@app.route('/api/items')
def get_items():
    global shopping_list
    return jsonify({'items': shopping_list})



# Boilerplate code start here..
if __name__=='__main__':
    #run webserver 
    app.run(debug=True)     # we are running the app in debug mode. 
                            # debug mode will restart the webserver whenever the files changes.

# Boilerplate code ends here..     

