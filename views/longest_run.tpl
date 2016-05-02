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
             <p>Add 0-4 Commands ('Please', 'You should', etc.)</p>
             <p>Currently Used : {{commands}} </p>
             <div class="form-group" "col-md-2">
               <textarea type="string" name="COMMAND_LIST" class="form-control" placeholder="command"></textarea>
             </div>
             <h3>Actions</h3>
             <p> Add 0-4 Actions ('run', 'recharge your battery')</p>
             <p>Currently Used : {{actions}} </p>
             <div class="form-group" "col-md-2">
               <textarea type="string" name="ACTION_LIST" class="form-control" placeholder="action"></textarea>
             </div>
             <h3>Address</h3>
             <p> Add 0-4 Addresses ('earthing', 'human')</p>
             <p>Currently Used : {{address}} </p>
             <div class="form-group" "col-md-2">
               <textarea type="string" name="ADDRESS_LIST" class="form-control" placeholder="address"></textarea>
             </div>
           </td>
         </tr>
       </table>
       <button type="submit" class="btn btn-default">Submit</button>
     </form>
<p>{{phrases}} </p>

</body>
</html>
