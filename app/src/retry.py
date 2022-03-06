"""
Código obtido de <https://wiki.python.org/moin/PythonDecoratorLibrary#Retry>
Com modificações de ArjanCodes <https://www.youtube.com/watch?v=ZsvftkbbrR0>

Alterações menores por Erick Gabriel Brunoro Mesquita
"""


import time
from math import floor
from functools import wraps

# Retry decorator with exponential backoff
def retry(ExceptionToCheck, tries=4, delay=3, backoff=1, logger=None):
	'''Retries a function or method until it returns True.

	delay sets the initial delay in seconds, and backoff sets the factor by which
	the delay should lengthen after each failure. backoff must be greater or equal than 1,
	or else it isn't really a backoff. tries must be at least 0, and delay
	greater than 0.'''

	if backoff < 1:
		raise ValueError("backoff must be greater or equal than 1")

	tries = floor(tries)
	if tries < 0:
		raise ValueError("tries must be 0 or greater")

	if delay <= 0:
		raise ValueError("delay must be greater than 0")

	def deco_retry(f):

		@wraps(f)
		def f_retry(*args, **kwargs):
			mtries, mdelay = tries, delay # make mutable
			success = False			
			
			while mtries > 1:
				try:
					return f(*args, **kwargs) # attempt

				except ExceptionToCheck as e:
					msg = f"{str(e)}. Tentando novamente em {mdelay} segundos..."
					if logger:
						logger.warning(msg)
					else:
						print(msg)
					
					
					mtries -= 1        # consume an attempt
					time.sleep(mdelay) # wait...
					mdelay *= backoff  # make future wait longer

				

			return f(*args, **kwargs) # Tenta pela última vez

		return f_retry # true decorator -> decorated function
	return deco_retry  # @retry(arg[, ...]) -> true decorator