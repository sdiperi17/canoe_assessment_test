<?php
class foo {
    public $value = 6;
    public function func1(&$value){
        $return = $value;
        $value += 1;
        return $return;
    }
    public function &func2(){
        return $this->value;
    }
    public function &func3(){
        static $value = 8;
        $value++;
        return $value;
    }
}
$obj = new foo();
$a = 2;
$b = $obj->func1($a);
echo "\nWhat is the value of $a and why?";
echo "\n $a is equal to 3 because func1(&$value) is using '&' before a parameter which means it accepts a reference to a variable as the parameter. Any changes that the function makes to the parameter (eg, $value += 1) will affect the $a variable passed by the calling function.\n";
echo "\n What is the value of $b and why?";
echo "\n Value of $b is 2 because we passing variable $a to func1 where variable $return is assigned to variable $a and func1 returned $return";
$a = &$obj->func2();
echo "\nWhat is the value of $a and why?";
echo "\n The value of $a is 6. In this example, as func2 is getter, the property of the object returned by the func2 function would be set, not the copy, as it would be without using reference syntax.";
$obj->value = 5;
echo "\nWhat is the value of $a and why?";
echo "\n The answer is remains the same 6. In the previous command, $a was assigned to &$obj->func2() by reference, which means $a is pointed to the value of &$obj->func2() which was set by getter func2";
$a = &$obj->func3();
echo "\nWhat is the value of $a and why?";
echo "\n Answer is 9. The method returns a value. Inside the method, $value becomes static, is reinstantiated, incremented and returned";
$obj->value = 7;
echo "\nWhat is the value of $a and why?";
echo "\n Answer is 9. Even though a function reference has been created, func3 still instantiates value and returns a value.";
?>