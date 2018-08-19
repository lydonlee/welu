
import web

print("The answer is", 2*4)        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())
print("test")
class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'
print("The answer is", 2*2)

if __name__ == "__main__":
    app.run()