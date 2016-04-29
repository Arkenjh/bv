from django.db import models
from tagging.fields import TagField
from tagging.models import Tag


class Division(models.Model):
	name = models.CharField("nom", max_length=50, blank=False, unique=True)
	available = models.BooleanField("actif", null=False, default=True)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField("nom", max_length=50, blank=False, unique=True)
	division = models.ForeignKey(Division, verbose_name="division")
	available = models.BooleanField("actif", null=False, default=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "categories"	

class SubCategory(models.Model):
	name = models.CharField("nom", max_length=50, blank=False, unique=True)
	category = models.ForeignKey(Category, verbose_name="catégorie")
	available = models.BooleanField("actif", null=False, default=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "sub categories"			

class Brand(models.Model):
	name = models.CharField("nom", max_length=50, blank=False, unique=True)
	tags = TagField()
	available = models.BooleanField("actif", null=False, default=True)

	def __str__(self):
		return self.name

# Create your models here.
class Products(models.Model):
	reference = models.CharField("ref", max_length=20, blank=False, null=False, unique=True)
	name = models.CharField("nom", max_length=150, blank=False)
	brand = models.ForeignKey(Brand, verbose_name="marque", blank=True, null=True)
	available = models.BooleanField("actif", null=False, default=True)

	def __str__(self):
		return "%s - %s" % (self.reference, self.name)

	class Meta:
		verbose_name = "product"
		verbose_name_plural = "products"			






import csv
import io

def import_from_csv(path):

	with io.open(path, encoding='iso-8859-15', newline='') as f:
		content = csv.reader(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_NONE)
		for row in content:
			try:
				created = Products.objects.get_or_create(
					reference=row[1],
					name=row[2],
				)

				print("%s (%s) = %s" % (row[0], row[1], row[2]))
			except IndexError:
				pass

def search_comp():
	data = {
		"jet tec":["comp jet tec", "rema jet tec", "reman jet tec"],
		"lama":["comp uprint", "rema uprint", "uprint", "reman uprint"], 
		"prolaser":["comp switch", "rema switch", "prolaser", "comp prol", "reman switch"], 
		"armor":["comp armor", "rema armor"], 
		"brother":["ruban bro tz"], 
		"muvit":["muvit"], 
		"clairefontaine":["clairalfa", "pollen"], 
		"gautier":["jazz", "mambo", "santos", "harmonica", "vermont", "sunday"]
	}

	for name, values in data.items():
		try:
			brand = Brand.objects.get(name=name)
			for pattern in values:
				products = Products.objects.filter(name__contains=pattern)
				count = 0
				if products.count():
					for product in products:
						product.brand = brand
						product.save()
						count += 1
				print("Pattern: %s, search %s #%d/%d" % (pattern, brand.name, count, products.count()))
		except:
			print("ERROR: %s" % (name))

def search_brands(force=False):
	for brand in Brand.objects.filter(available=True):
		print("--------------------")
		q = Products.objects.filter(brand=None, name__contains=brand.name.upper())
		print("Search: %s #%d" % (brand.name, q.count()))

		count = 0

		for product in q:
			product.brand = brand
			product.save()
			count += 1

		print("Saved: %s #%d/%d" % (brand.name, count, q.count()))

		for tag in Tag.objects.get_for_object(brand):
			products = Products.objects.filter(brand=None, name__contains=tag.name)
			print("Search: %s #%d" % (tag.name, products.count()))

			if products.count() and force:
				while 1:
					c = input("continue y/n: ? (y:default)")
					if c == 'n':
						break
					else:
						
						for product in products:
							print("\t### %s, %s ?" % (product.name, tag.name))
							while 1:
								response = input("\t### y/n: ? (y:default)")
								if response == "y":
									product.brand = brand
									product.save()
									break
								elif response == 'n':
									break
					break
			

	products = Products.objects.all()
	total = products.count()
	store = products.exclude(reference__startswith='8139').exclude(reference__startswith='8140').count()
	no_brand = products.filter(brand=None).count()
	brand = total - no_brand

	print("TOTAL: %d/%d/%d (%d) %d/100 completed" % (brand, total, store ,no_brand, (brand * 100 / total)))

PRODUCTS_CHOICES = [(product.id, "%s - %s" % (product.reference, product.name)) for product in Products.objects.filter(available=True)[:50]]
#PRODUCTS_CHOICES = []