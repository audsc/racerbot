<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 
<head>
    <link href="style.css" rel="stylesheet" type="text/css" />
</head>
 
<body>
<h1>{{title}}</h1>
    <form role="form" method="post" action="/Longest_Run">
       <table>
           <td>
             <h3>Commands</h3>
             <p>Add 0-4 Commands ('Please', 'You should', etc.</p>
             <div class="form-group" "col-md-2">
               <input type="string" name="COMMAND1" class="form-control" placeholder="command">
               <input type="string" name="COMMAND2" class="form-control" placeholder="command">
               <input type="string" name="COMMAND3" class="form-control" placeholder="command">
               <input type="string" name="COMMAND4" class="form-control" placeholder="command">
             </div>
             <h3>Actions</h3>
             <p> Add 0-4 Actions ('run', 'recharge your battery')</p>
             <div class="form-group" "col-md-2">
               <input type="string" name="ACTION1" class="form-control" placeholder="action">
               <input type="string" name="ACTION2" class="form-control" placeholder="action">
               <input type="string" name="ACTION3" class="form-control" placeholder="action">
               <input type="string" name="ACTION4" class="form-control" placeholder="action">
             </div>
             <h3>Address</h3>
             <p> Add 0-4 Addresses ('earthing', 'human')</p>
             <div class="form-group" "col-md-2">
               <input type="string" name="ADDRESS1" class="form-control" placeholder="address">
               <input type="string" name="ADDRESS2" class="form-control" placeholder="address">
               <input type="string" name="ADDRESS3" class="form-control" placeholder="address">
               <input type="string" name="ADDRESS4" class="form-control" placeholder="address">
             </div>
           </td>
         </tr>
       </table>
       <button type="submit" class="btn btn-default">Submit</button>
     </form>
<p>{{phrases}} </p>

</body>
</html>
