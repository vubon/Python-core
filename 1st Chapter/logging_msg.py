'''
We can track events in a software application, this is known as logging.
Let’s start with a simple example, we will log a warning message

'''
import logging

#print a log message in the console.
logging.warning('This is a warning message ')

# we can easily output a file
logging.basicConfig(filename='program.log', level=logging.DEBUG)
logging.warning('An example message')
logging.warning('Anthor message ')

# time showing matter
logging.basicConfig(format='%(asctime)% s %(message)s', level=logging.DEBUG)
logging.info('App started')
logging.warning('Hello world')



