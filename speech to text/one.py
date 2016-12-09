import string
import speech
while True:
    print('Talk with me now')
    phrase = speech.input()
    speech.say('You said %s' % phrase)
    print('You said [0}'.format(phrase))
    if phrase.lower() == 'goodbye':
        break
