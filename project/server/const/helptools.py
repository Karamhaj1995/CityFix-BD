def convert_arguments(params):
	return dict((k,v[0].decode('utf-8')) for  k,v in params.items())