-----------------------------
Thunderpush client for Python
-----------------------------

A Python library for sending messages to the `Thunderpush <https://github.com/thunderpush/thunderpush>`_ server.

Example
=======

::
	
	from thunderclient import Thunder

	c = Thunder("key", "secretkey", "localhost", 8080)

	print c.get_user_count()
	print c.get_users_in_channel("test")
	print c.send_message_to_user("test", {"msg": "hello!"})
	print c.send_message_to_channel("test", {"msg": "hello!"})
	print c.is_user_online("test")
	print c.disconnect_user("test")
