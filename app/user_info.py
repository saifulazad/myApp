import redis



class Userinfo:

	def __init__(self , email):
		self.db = redis.Redis(host='localhost', port=6379, db=0)
		
		self.email = self.db.get(email)
		
		
			
	def is_matched(self , email,  password):
		
		if self.email == password:
			return True
		
		return False
		
        def is_authenticated(self):
                return True

        def is_active(self):
                return True

        def is_anonymous(self):
                return False

        def get_id(self):
                return self.email
        def __repr__(self):
                return '<User %r>' % (self.email)	
		
		
