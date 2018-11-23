import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_00(self):
        """Simple program: int main() {} """
        input = """
        var x:integer;
        var y:real;
        procedure f();
        begin
            putInt(10);
        end
        procedure main(); 
        begin 
            putInt(100);
        end"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_20(self):
        """Simple program: int main() {} """
        input = """
        procedure main();
        var x:integer;
        begin
            x := 1;
            putInt(x);
            x:=10;
            putInt(x*2);
        end

        """
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    def test_21(self):
        """Simple program: int main() {} """
        input = """
        var x:integer;
        procedure main();
        begin
            x := 1;
            putInt(x);
            x:=10;
            putInt(x*2);
        end

        """
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,521))
