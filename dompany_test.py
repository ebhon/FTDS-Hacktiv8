import unittest
from company import Employee

class TestEmployee(unittest.TestCase):
    pass
    def test_assign_department(self):
        print ('proses test pertama dimulai')
        obj_1 = Employee("E7876", "ADAMS", 50000, "ACCOUNTING")
        cek_1 = obj_1.emp_department
        self.assertEqual(cek_1, 'ACCOUNTING')
        obj_1.assign_department("HR")
        cek_2 = obj_1.emp_department
        self.assertEqual(cek_2, 'HR')
        print ("berhasil ubah department")
        
if __name__ == "__main__":
    unittest.main()

