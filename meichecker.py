from lxml import etree
doc = etree.parse("mei-Neumes2.rng")
relaxng = etree.RelaxNG(doc)
def main(filename):

    foil = etree.parse(filename)
    relaxng.validate(foil)
    print(relaxng.error_log.__str__())
    return relaxng.error_log.__str__()
        
