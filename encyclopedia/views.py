import markdown2
from django.shortcuts import render
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def page(request,name):
    markdown_content = util.get_entry(name)
    if markdown_content:
        html_content = markdown2.markdown(markdown_content)
        return render(request, "encyclopedia/page.html", {
            "title":name,
            "html_content": html_content
        })
    else:
        return render(request, "encyclopedia/error.html")
