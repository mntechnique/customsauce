import frappe
from frappe import _

@frappe.whitelist()
def a_on_submit(self, method):
	scenario_2(self, method)
	# scenario_3(self, method)
	# scenario_4(self, method)
	# scenario_5(self, method)


def scenario_2(self, method):
	existingrow = frappe.get_doc("CS Table BY", {"parent": self.linked_field_ab, "field_by2": "abc"})
	existingrow.field_by1 = self.field_a

	existingrow.save()
	frappe.db.commit()

def scenario_3(self, method):
	line_items = frappe.get_all("CS Table AX", filters={"parent": self.name}, fields=["name", "field_ax1"])

	target_doc = frappe.get_doc("CS Doctype B", self.linked_field_ab)
	target_doc.field_b = line_items[0].field_ax1

	target_doc.save()
	frappe.db.commit()

def scenario_4(self, method):
	line_items = frappe.get_all("CS Table AX", filters={"parent": self.name}, fields=["name", "field_ax1"])
	target_doc = frappe.get_doc("CS Doctype B", self.linked_field_ab)

	print "Items"
	for item in line_items:
		print item.field_ax1

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
