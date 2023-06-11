#js2py
import js2py

js = '''
function test(){
var a,b,c
a='+2 '
b='84-'
a+='245-'
b+='4570'
c='8'
document.write(a+c+b)
}
test()
'''.replace('document.write', 'return ')

result = js2py.eval_js(js)
print(result)