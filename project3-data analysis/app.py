import justpy as jp #jp is variable

def app():
    wp=jp.QuasarPage() #search "quasar style" for different styles
    h1=jp.QDiv(a=wp,text="Analysis of reviews",classes="text-h1 text-center q-pa-md")
    p1=jp.QDiv(a=wp,text="these graph represents course review analysis")

    return wp

jp.justpy(app)