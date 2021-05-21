import os
import yaml

def get_categories(question_list,answer_list):
	w = open("questions.txt","w")

	for i in range(len(question_list)):
		w.write("{}. {} ANSWER: {}\n".format(i+1,question_list[i],answer_list[i]))
	w.close()

	os.system("python2 augur.py questions.txt  -t SCOP -r 5")

	categories = yaml.load("\n".join(open("questions.txt.yml").read().split("\n")[:-2]))
	return {'categories':[i['category'] for i in categories],'subcategories':[i['subcategory'] for i in categories]}

print(get_categories(["This quantity can be measured with a Galilean device that relies on changes in liquid density. The surface form of this quantity is measured with a pyrometer. The first reliable tool for measuring this quantity was a sealed glass tube of (*) mercury. Absolute scales for this quantity include Rankine and Kelvin, and its standard scale is based on the freezing and boiling points of water. For ten points, name this quantity recorded in degrees Celsius."]*1000,["Temperature"]*1000))
