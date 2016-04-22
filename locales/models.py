from django.db import models

DEPARTMENTS = (('01', '84','Ain'),
('02', '32','Aisne'),
('03', '84','Allier'),
('04', '93','Alpes-de-Haute-Provence'),
('05', '93','Hautes-Alpes'),
('06', '93','Alpes-Maritimes'),
('07', '84','Ardèche'),
('08', '44','Ardennes'),
('09', '76','Ariège'),
('10', '44','Aube'),
('11', '76','Aude'),
('12', '76','Aveyron'),
('13', '93','Bouches-du-Rhône'),
('14', '28','Calvados'),
('15', '84','Cantal'),
('16', '75','Charente'),
('17', '75','Charente-Maritime'),
('18', '24','Cher'),
('19', '75','Corrèze'),
('21', '27','Côte-d\'Or'),
('22', '53','Côtes-d\'Armor'),
('23', '75','Creuse'),
('24', '75','Dordogne'),
('25', '27','Doubs'),
('26', '84','Drôme'),
('27', '28','Eure'),
('28', '24','Eure-et-Loir'),
('29', '53','Finistère'),
('30', '76','Gard'),
('31', '76','Haute-Garonne'),
('32', '76','Gers'),
('33', '75','Gironde'),
('34', '76','Hérault'),
('35', '53','Ille-et-Vilaine'),
('36', '24','Indre'),
('37', '24','Indre-et-Loire'),
('38', '84','Isère'),
('39', '27','Jura'),
('40', '75','Landes'),
('41', '24','Loir-et-Cher'),
('42', '84','Loire'),
('43', '84','Haute-Loire'),
('44', '52','Loire-Atlantique'),
('45', '24','Loiret'),
('46', '76','Lot'),
('47', '75','Lot-et-Garonne'),
('48', '76','Lozère'),
('49', '52','Maine-et-Loire'),
('50', '28','Manche'),
('51', '44','Marne'),
('52', '44','Haute-Marne'),
('53', '52','Mayenne'),
('54', '44','Meurthe-et-Moselle'),
('55', '44','Meuse'),
('56', '53','Morbihan'),
('57', '44','Moselle'),
('58', '27','Nièvre'),
('59', '32','Nord'),
('60', '32','Oise'),
('61', '28','Orne'),
('62', '32','Pas-de-Calais'),
('63', '84','Puy-de-Dôme'),
('64', '75','Pyrénées-Atlantiques'),
('65', '76','Hautes-Pyrénées'),
('66', '76','Pyrénées-Orientales'),
('67', '44','Bas-Rhin'),
('68', '44','Haut-Rhin'),
('69', '84','Rhône'),
('70', '27','Haute-Saône'),
('71', '27','Saône-et-Loire'),
('72', '52','Sarthe'),
('73', '84','Savoie'),
('74', '84','Haute-Savoie'),
('75', '11','Paris'),
('76', '28','Seine-Maritime'),
('77', '11','Seine-et-Marne'),
('78', '11','Yvelines'),
('79', '75','Deux-Sèvres'),
('80', '32','Somme'),
('81', '76','Tarn'),
('82', '76','Tarn-et-Garonne'),
('83', '93','Var'),
('84', '93','Vaucluse'),
('85', '52','Vendée'),
('86', '75','Vienne'),
('87', '75','Haute-Vienne'),
('88', '44','Vosges'),
('89', '27','Yonne'),
('90', '27','Territoire de Belfort'),
('91', '11','Essonne'),
('92', '11','Hauts-de-Seine'),
('93', '11','Seine-Saint-Denis'),
('94', '11','Val-de-Marne'),
('95', '11','Val-d\'Oise'),
('2A', '94','Corse-du-Sud'),
('2B', '94','Haute-Corse'),
('971', '01', 'Guadeloupe'),
('972', '02', 'Martinique'),
('973', '03', 'Guyane'),
('974', '04', 'La Réunion'),
('976', '06', 'Mayotte'))



class FrenchRegions(models.Model):
	code = models.CharField("code", max_length=2)
	name = models.CharField("nom", max_length=50)
	upper_name = models.CharField("nom", max_length=50)

	def __str__(self):
		return "%s (%s)" % (self.name, self.code)

class Countries(models.Model):
	code = models.IntegerField("code")
	alpha2 = models.CharField("alpha2", max_length=2)
	alpha3 = models.CharField("alpha3", max_length=3)
	name_en_gb = models.CharField("nom", max_length=50)
	name_fr_fr =models.CharField("nom", max_length=50)	

	def __str__(self):
		return "%s (%s)" % (self.name_fr_fr, self.alpha2)

# departement_id`, `departement_code`, `departement_nom`, `departement_nom_uppercase`, `departement_slug`, `departement_nom_soundex`
class FrenchDepartments(models.Model):
	code = models.CharField("code", max_length=3)
	name = models.CharField("nom", max_length=50)
	upper_name = models.CharField("nom", max_length=50)
	slug = models.CharField("slug", max_length=50)
	soundex = models.CharField("soundex", max_length=20)
	region = models.ForeignKey(FrenchRegions, verbose_name="region", null=True)

	def __str__(self):
		return "%s (%s)" % (self.name, self.code)

FRENCH_DEPARTMENTS = [(department.id, department.name) for department in FrenchDepartments.objects.all()]
#FRENCH_DEPARTMENTS = []

class FrenchTowns(models.Model):
	department = models.ForeignKey(FrenchDepartments, verbose_name="departement", null=True)
	_department = models.CharField("departement", max_length=3)
	slug = models.CharField("slug", max_length=3)
	name = models.CharField("nom", max_length=45)
	short_name = models.CharField("nom court", max_length=45)
	full_name = models.CharField("nom complet", max_length=45)
	soundex = models.CharField("soundex", max_length=20)
	metaphone = models.CharField("metaphone", max_length=22)
	zipcode = models.CharField("code postal", max_length=10)
	township = models.CharField("commune", max_length=45)
	township_code = models.CharField("code commune", max_length=5)
	district = models.IntegerField("arrondissement")
	canton = models.CharField("canton", max_length=45)
	amdi = models.IntegerField("amdi")
	population_2010 = models.IntegerField("population 2010")
	population_1999 = models.IntegerField("population 1999")
	population_2012 = models.IntegerField("population 2012")
	density_2010 = models.IntegerField("densité")
	area = models.FloatField("surface")
	longitude_deg = models.FloatField("longitude deg")
	latitude_deg = models.FloatField("latitude deg")
	longitude_grd = models.CharField("longitude grd", max_length=9)
	latitude_grd = models.CharField("latitude grd", max_length=8)
	longitude_dms = models.CharField("longitude dms", max_length=9)
	latitude_dms = models.CharField("latitude dms", max_length=8)
	zmin = models.IntegerField("zmin")
	zmax = models.IntegerField("zmax")

	def __str__(self):
		return "%s (%s)" % (self.name, self.zipcode)



### set department foreignkey from _department
def LinkDepartmentsToTown():
	count = 0
	towns = FrenchTowns.objects.filter(department=None)
	for town in towns:
		try:
			if town.department is None:
				department = FrenchDepartments.objects.get(code__iexact=town._department)
				town.department = department
				print("%s - %s" % (town.name, department.name))
				count += 1
				town.save()
		except:
			print("ERREUR: %s - '%s'" % (town.name, town._department))

	print("### TOTAL: %d/%s" % (count, towns.count()))

def LinkDepartmentsToRegions():
	count = 0
	for (dep_code, region_code, dep_name) in DEPARTMENTS:
		
		department = FrenchDepartments.objects.get(code__iexact=dep_code)
		region = FrenchRegions.objects.get(code__iexact=region_code)
		department.region = region
		department.save()
		print("%s = %s" % (department.name, region.name))
		count += 1
	
		#print("ERREUR: %s (%s) (%s)" % (dep_name, dep_code, region_code))
	print("### TOTAL: %d/%s" % (count, len(DEPARTMENTS)))