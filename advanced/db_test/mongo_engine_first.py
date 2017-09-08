from mongoengine import *

connect("test",host='localhost',port=27017)

#defining a document
import datetime

#referencing other
class Author(Document):
	name = StringField()

class Post(Document):
	title = StringField(required=True, max_length=200)
	content = StringField(required=True)
	author = ReferenceField(Author)
	publised = DateTimeField(default=datetime.datetime.now())
	
	def __str__(self):
		aut = Author.objects(_id = self.author)
		author_name = aut.name
		return 'Author: '+str(author_name)+", title: "+str(self.title)+", content: "+str(self.content)+", published: " \
																								  ""+str(self.publised)
	

# author = Author('Ladin')
# author.save()
#
# post = Post(title='Sample Post', content='SOme angaging content', author = 'Ladin')
# post.save()
#
# print(post.title)
# post.title = 'A better post title'
# post.save()
# print(post.title)
# print(post.author)

# author = Author()
# author.name = input("Nhap vao ho ten:")
# # for post in Author.objects(name=author):
# # 	print(post.name)
# author.save()
# post = Post()
# post.author = author
# post.content = input("Nhap vao content")
# post.title = input("Nhap vao titel")
# post.save()

# for author in Author.objects():
# 	print(author.name)

post_count = Post.objects.count()
print(post_count)

posts = Post.objects()
for post in posts:
	print(post.to_json())
	print(post.__str__)