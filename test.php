class foo {
public $value = 6; 
public function func1(&$value){
$return = $value; 
$value += 1; 
echo $return;
return $return; 
}
}

$obj = new foo();
$a=2; $b = $obj->func1($a)