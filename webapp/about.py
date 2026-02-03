import justpy as jp
from docutils.nodes import container

from webapp import layout

class About:
    path = "/about"
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is About page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Bla bla bla
        """, classes="text-lg")
        return wp
