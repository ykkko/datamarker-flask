"""
Этот модуль создает js скрипт для создания eventListener'ов.
Это очень кастомизированный блок.
"""



def make_if_block(key_num, class_num):
    return \
    """
        if (event.keyCode === %i) {
            document.getElementById('%s').click();
        }
    """ \
    % (key_num, 'class' + str(class_num))

def make_keyListenerJsScript(classes):

    start_script = """
    document.addEventListener('keyup', function(event) {
        event.preventDefault();
    """

    body_script = ''
    for n, cls in enumerate(classes):
        body_script += make_if_block(cls[1], n)

    end_script = """
    });"""

    with open('data/js/js_script.js', 'w+') as js_file:
        js_file.write(start_script + body_script + end_script)




if __name__ == "__main__":
    classes = [
        ['Original', 49],
        ['Photoshop', 50],
        ['oTHER', 51]
    ]

    print(make_keyListenerJsScript(classes))