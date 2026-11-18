import os, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import csv2json


class T(unittest.TestCase):
    def write(self, text):
        f = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8")
        f.write(text); f.close(); self.addCleanup(os.unlink, f.name); return f.name

    def test_basic(self):
        self.assertEqual(csv2json.convert(self.write("a,b\n1,2\n")), [{"a": "1", "b": "2"}])

    def test_quoted_comma(self):
        self.assertEqual(csv2json.convert(self.write('n,city\n"Doe, J",Delhi\n'))[0]["n"], "Doe, J")

    def test_utf8(self):
        self.assertEqual(csv2json.convert(self.write("n\nगोस्वामी\n"))[0]["n"], "गोस्वामी")

    def test_missing_file_exit_code(self):
        self.assertEqual(csv2json.main(["x", "no_such_file.csv"]), 2)


if __name__ == "__main__":
    unittest.main()
