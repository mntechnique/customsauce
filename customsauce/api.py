import frappe
from frappe import _

@frappe.whitelist()
def a_on_submit(self, method):
	#scenario_1(self, method)
	scenario_3_new(self, method)
	# scenario_2(self, method)
	# scenario_3(self, method)
	# scenario_4(self, method)
	# scenario_5(self, method)

@frappe.whitelist()
def a_on_cancel(self, method):
	scenario_1_cancel(self, method)

#On Submit
def scenario_1(self, method):	
	target_doc = frappe.get_doc("CS Doctype B", self.linked_field_ab)
	existing_row_id = frappe.db.get_value("CS Table BY", filters={"parent": self.linked_field_ab, "field_by1": self.field_a}, fieldname="name")

	if not existing_row_id:
		target_doc.append("table_b", {
			"field_by1": self.field_a
		})
		target_doc.save()
		frappe.db.commit()

def scenario_2(self, method):
	existing_row = frappe.get_doc("CS Table BY", {"parent": self.linked_field_ab, "field_by2": "abc"})
	existing_row.field_by1 = self.field_a

	existing_row.save()
	frappe.db.commit()

def scenario_3(self, method):
	line_items = frappe.get_all("CS Table AX", filters={"parent": self.name}, fields=["name", "field_ax1"])

	target_doc = frappe.get_doc("CS Doctype B", self.linked_field_ab)
	target_doc.field_b = line_items[0].field_ax1

	target_doc.save()
	frappe.db.commit()

def scenario_3_new(self, method):
	for li_a in self.table_a: 
		
		# set_value by-passes permissions matrix  
		# frappe.db.set_value("CS DocType C", i.ac, "field_c", i.field_ax1);
		# frappe.db.commit()	

		oc = frappe.get_doc("CS DocType C", li_a.ac)
		oc.field_c = li_a.field_ax1
		oc.save()
		frappe.db.commit()

def scenario_4(self, method):
	line_items = frappe.get_all("CS Table AX", filters={"parent": self.name}, fields=["name", "field_ax1"])
	
	#Find existing details row where field_by1 = field_ax1.value
	existing_row_id = frappe.db.get_value("CS Table BY", filters={"parent": self.linked_field_ab, "field_by1": line_items[0].field_ax1}, fieldname="name")

	if not existing_row_id:
		target_doc = frappe.get_doc("CS Doctype B", self.linked_field_ab)
		target_doc.append("table_b", {
			"field_by1": line_items[0].field_ax1
		})

		target_doc.save()
		frappe.db.commit()
	
def scenario_5(self, method):
	line_items = frappe.get_all("CS Table AX", filters={"parent": self.name}, fields=["name", "field_ax1"])
	target_line_item = frappe.get_doc("CS Table BY", {"parent": self.linked_field_ab, "field_by2": "abc"})

	target_line_item.field_by1 = line_items[0].field_ax1

	target_line_item.save()
	frappe.db.commit()	


#CANCEL
def scenario_1_cancel(self, method):
	existing_row_id = frappe.db.get_value("CS Table BY", filters={"parent": self.linked_field_ab, "field_by1": self.field_a}, fieldname="name")
	
	frappe.delete_doc("CS Table BY", existing_row_id)
	frappe.db.commit()