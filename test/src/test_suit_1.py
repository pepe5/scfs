# https://www.codegrepper.com/code-examples/python/python+subprocess+run+environment+variables
import os, subprocess
E = os.environ.copy ()
E ["PATH"] = "./main/lib:" + E ["PATH"]

def test_catalog_f1 ():
    RC = subprocess.call ('test/lib/catalog_f1', env = E); RC
    assert RC == 0
