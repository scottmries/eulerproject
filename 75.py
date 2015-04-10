# generate the Pythagorean triples less than 1500000

# for coprime m,n 
# a = m**2 - n**2, b = 2mn, c = m**2 + n**2
# if m-n is even, divide a,b, and c by two

# multiply a,b, and c by integers through to the limit
# increment the value at a+b+c in a dictionary

# generate the next coprime pair until a+b+c > 1500000

# upper_bound = 1500000

class Coprimes(object):

	def __init__(self,limit):
		self.roots = [(2,1),(3,1)]
		self.primitive_triples = []
		self.all_triples = []
		self.generators = [self.generate_branch1,self.generate_branch2,self.generate_branch3]
		self.int_triangles = dict()
		self.limit = limit
		

	def primitive_pythag_triple(self,m,n):
		a = m**2 - n**2
		b = 2*m*n
		c = m**2 + n**2
		if (m-n)%2==0:
			return a/2,b/2,c/2
		else:
			return a,b,c

	def generate_branch1(self,m,n):
		# print "b1",
		n2 = m
		m2 = 2*m-n
		
		# print self.primitive_pythag_triple(m2,n2)
		return (m2,n2),self.primitive_pythag_triple(m2,n2)

	def generate_branch2(self,m,n):
		# print "b2",
		n2 = m
		m2 = 2*m+n
		# print self.primitive_pythag_triple(m2,n2)
		return (m2,n2),self.primitive_pythag_triple(m2,n2)

	def generate_branch3(self,m,n):
		# print "b3",
		m2 = m+2*n
		# print self.primitive_pythag_triple(m2,n)
		return (m2,n),self.primitive_pythag_triple(m2,n)

	def generate_with_prim_pythag_triple_sum_below(self):
		
		coprimes = list()
		for r in self.roots:
			for generator in self.generators:
				m,n = r[0],r[1]
				a,b,c = self.primitive_pythag_triple(m,n)
				print generator
				while True:
					if a + b + c < self.limit:
						self.primitive_triples.append((a,b,c))
						# print generator(m,n)
						g = generator(m,n)
						(m,n),(a,b,c) = g[0],g[1]
					else:
						break

	def triples_from_primitives_below(self):
		
		self.generate_with_prim_pythag_triple_sum_below()
		for primitive in self.primitive_triples:
			a,b,c = 0,0,0
			# a,b,c = primitive[0], primitive[1], primitive[2]
			while True:
				a += primitive[0]
				b += primitive[1]
				c += primitive[2]
				s = sum([a,b,c])
				
				if s < self.limit:
					print a,b,c
					if s in self.int_triangles:
						if list(sorted([a,b,c])) not in self.int_triangles[s]:
							self.int_triangles[s].append(list(sorted([a,b,c])))
					else:
						self.int_triangles[s] = [list(sorted([a,b,c]))]
				
					
					# i += 1
				else:
					break


	def count_single_solution_triangles(self):
		
		
		self.triples_from_primitives_below()
		# for t in self.int_triangles:
			# if self.int_triangles[t] > 1:
				# print "%s: %s" % (t, self.int_triangles[t])
		
		# print len(self.int_triangles.keys())
		solution = 0
		print len(self.int_triangles)
		for k in self.int_triangles:
			if len(self.int_triangles[k]) == 1:
				solution += 1
		return solution

low_coprimes = Coprimes(100)
# low_coprimes.generate_with_prim_pythag_triple_sum_below()
# print low_coprimes.count_single_solution_triangles()
coprimes = Coprimes(1500001)
print coprimes.count_single_solution_triangles()
print "120", coprimes.int_triangles[120]
