# #!C:\dev\markerweb\venv\Scripts\python.exe
# import cgitb
# cgitb.enable()

"""
Приложение берет первый файл из папки src и передает в html клиенту.
От клиента приложение получает ответ. И копирует файл в папку, соответствующую этому ответу.
Таким образом размечаются все данные из src.

Может было бы круто сделать возможность исправлять ответы.

ВХОДНЫЕ ДАННЫЕ:
src - папка, где лежат фотки
dst - папка, где будут создаваться папки с именами классов
classes - список имен классов и код клавиши на клавиатуре для этого класса
"""

import os
import shutil
from flask import Flask, request, render_template, redirect, session, url_for, escape
from js_maker import make_keyListenerJsScript


app = Flask(__name__, static_folder='data')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'   # set the secret key.  keep this really secret


src = 'data/dataset/all_images/'
dst = 'data/dataset/'
classes = [
    ['1_x_long', 49],   # key "1"
    ['2_long', 50],     # key "2"
    ['3_medium', 51],
    ['4_closeup', 52],
    ['5_detail', 53],
    ['6_other', 54],
]


keyListenerJsScript = make_keyListenerJsScript(classes)
photoForUserDict = {}
file_list = os.listdir(src)
print(file_list)


@app.route("/next", methods=['GET', 'POST'])
def next_image():

    try:
        user_name = escape(session['username'])
    except:
        return redirect('/login')

    print('[%s] IN /next' % user_name)

    if user_name not in photoForUserDict.keys():
        print('[%s] NEED IN NEW PHOTO!' % user_name)
        print(photoForUserDict)

        image_name = None

        for photo in file_list:
            print(photo)
            if photo not in photoForUserDict.values():
                image_name = photo
                break

        print(image_name)

        if image_name is None:
            print('ERROR: NO MORE PHOTO IN %s' % src)
            return render_template('finish.html', user_name=user_name)

        print('TRY TO SEND [%s] TO [%s]' % (image_name, user_name))
        photoForUserDict[user_name] = image_name

        print(photoForUserDict)
        return render_template("next.html",
                               path_name='dataset/all_images/',
                               image_name=image_name,
                               user_name=user_name,
                               classes=classes)
    else:
        print('USER [%s] ALREADY THERE!' % user_name)
        print(photoForUserDict)
        return render_template("next.html",
                               path_name='dataset/all_images/',
                               image_name=photoForUserDict[user_name],
                               user_name=user_name,
                               classes=classes)


@app.route('/handle_data', methods=['POST'])
def handle_data():

    user_name = request.form['userName']

    # print(photoForUserDict)
    print(user_name)

    del photoForUserDict[user_name]
    # print(photoForUserDict)

    answer = request.form['class']
    image_name = request.form['imageName']
    print('{} SAID THAT {} IS {}'.format(user_name, image_name, answer))

    source = src + '{}'.format(image_name)
    destination = dst + '{}/'.format(answer)

    # Если директории с именем класса еще нет, создаем.
    # Можно вынести создание диров наверх и сразу всех. Чтоб не проверять постоянно условие
    if not os.path.exists(destination):
        os.makedirs(destination)

    if source.split('/')[-1] in file_list:
        os.rename(source, destination + str(image_name))
        # shutil.copyfile(source, destination + str(image_name))
        file_list.remove(image_name)
    else:
        print('ERROR: {} IS NO LONGER IN THE {}'.format(image_name, src))

    return redirect('/next')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('next_image'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route("/", methods=['GET', 'POST'])
def start():
    return redirect('/next')


if __name__ == '__main__':
    app.run(debug=False)
