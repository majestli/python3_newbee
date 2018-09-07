class ShortinputException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast
try:
    text=input('Enter someting--->')
    if len(text) <3:
        raise ShortinputException(len(text),3)
except EOFError:
    print('why did you do an EOF on me?')
except ShortinputException as ex:
    print(('shortinputexception: the input was'+'{0} long, expected at least {1}').format(ex.length,ex.atleast))
else:
    print('No exceptin was raised.')
