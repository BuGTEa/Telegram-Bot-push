def check_status(a, func):
	if a.status_code != 200:
		return ConnectionError(f'Some Wrong when handle {func}')
	else:
		return a.json()
