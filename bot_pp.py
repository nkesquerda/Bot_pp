# -*- coding: utf-8 -*-
import sys
sys.path.append('C:\pywikipedia')
import wikipedia, re
def fes(pagina):
    pag = wikipedia.Page(wikipedia.getSite('ca'), pagina) # creem un objecte page on poder treballar
    noutext = text = pag.get() # obtenuim el text
    noutext = re.sub(u"\| ?pàgines ?= p\.?", "|pàgines=", text)
    wikipedia.showDiff(text, noutext)
    if raw_input(u"Vols penjar la pàgina [y/n]?") == "y":
        pag.put(noutext, comment=u"Robot fent canvis per la {{tl|ref-llibre}}")

fes(u'Maig')
