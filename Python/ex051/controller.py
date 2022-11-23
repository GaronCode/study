import view
import model

def button_click():
    va = view.get_value()
    vb = view.get_value()
    model.init(va, vb)
    res = model.sum()
    view.see(res)