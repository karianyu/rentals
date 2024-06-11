# Copyright (c) 2024, karianyu and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Vehicle(WebsiteGenerator):

	def before_save(self):
		self.set_title()
		self.set_route()
	
	def set_title(self):
		self.title = f'{self.make} { self.model} , {self.year}'

	def set_route(self):
		self.route = self.name

 