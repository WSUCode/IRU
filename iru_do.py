
import os
root_path = os.getcwd()

def make_locale_mo():
    po_files = os.listdir( 
        os.path.join( root_path , 'locale', )
     )
    
    for f in po_files:
        f = f'{root_path}/locale/{f}/LC_MESSAGES/iru'
        os.system( f'msgfmt -o {f}.mo {f}.po' )