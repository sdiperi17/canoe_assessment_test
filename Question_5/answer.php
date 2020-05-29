In a form, we have three input boxes for users to type in their choices of courses and submit the form without refreshing the page(i.e using ajax request). Here are the requirements:
1. User can type in 1, 2 or 3 courses 2. Each choice is case insensitive (also, user can type anything, in any case or leave it empty) 3. The choices have to contain “calculus”(in any case, e.g “Calculus” or “CALCULUS”) in one input
box. 4. Because form onsubmit returns false, the form is submitted through ajax by calling submitForm(),
add your Javascript/jQuery code inside of this function. 5. The PHP on the server side needs to do the same validation as in Javascript/jQuery to make sure
data is consistent.
<form action="/post" onsubmit="submitForm();return
false;">
Choice A: <input type="text" name="choices[]"/> Choice B: <input type="text" name="choices[]"/> Choice C: <input type="text" name="choices[]"/> <input type="submit" value="Submit"/> </form>
Finish the Javascript/jQuery and PHP code after each “//add your code after this line” shown below.
JQuer y:
function submitForm() {
var $form = $('form'); var url = $('form').attr('action'); // add your code after this line
   }
PHP :
class MyController extends Controller {
public function post() {
$inputs = Input::all(); //add your code after this line

  //end of add your code
if($this->save($inputs)
){
return [ 'status'=>'success' ]; } else {
return ['status'=>'error', 'errorMessage' => $this->getLastErrorMessage()]; } } }