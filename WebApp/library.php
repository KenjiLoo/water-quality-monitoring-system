<!DOCTYPE html >
<html>
<head>
    <meta name="viewport" content="with=device-width, initial-scale=1.0">
    <title>SEGP 9A_Library</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  </head>
  <body>
    <section class="sub-header">
    <nav>
        <a href="mainpage.html"> <img src="images/frontpagelogo.png"></a>
        <div class="nav-links" id="navLinks">
            <i class="fa fa-times" onclick="hideMenu()"></i>
            <ul>
                <li><a href="mainpage.html">HOME</a></li>
                <li><a href="intro.html">INTRODUCTION</a></li>
                <li><a href="library.php">LIBRARY</a></li>
                <li><a href="monitor.php">MONITOR</a></li>
                <li><a href="index.php">LOGOUT</a></li>
                
            </ul>
        </div>
        <i class="fa fa-bars" onclick="showMenu()"></i>
    </nav>
    <h1>Past Results</h1>
</section>
 
<?php 
//connect to mysql server with host,username,password
//if connection fails stop further execution and show mysql error
$connection=mysqli_connect('localhost','root','','hfyql1ju_csv_db_7') or die(mysqli_error(die));
//select a database for given connection
//if database selection  fails stop further execution and show mysql error
mysqli_select_db($connection,'hfyql1ju_csv_db_7') or die(mysqli_error(die));

//execute a mysql query to retrieve all the users from users table
//if  query  fails stop further execution and show mysql error
$query=mysqli_query($connection,"SELECT * FROM results") or die(mysqli_error(die));
 
//if we get any results we show them in table data
if(mysqli_num_rows($query)>0):
   
 
?>
<div class ="table-container">
<table class="library-table">
    <thead>
    <tr>
        <th>Id</th>
        <th>diff_percentage (%) </th>
        <th>Colour</th>
        <th>Image</th>
        <th>Date</th>
    </tr>
    </thead>
  <?php 
  // looping 
  while($row=mysqli_fetch_object($query)):?>
  <tbody>
  <tr>
    <td data-label="ID:"><?php echo $row->id;  //row id ?></td>
    <td data-label="diff_percentage(%):"><?php echo $row->difference_percentage; // row first name ?></td>
    <td data-label="Colour:"><?php echo $row->colour; //row last name  ?></td>
    <td data-label="Image:"><img src="data:image/jpg;charset=utf8;base64,<?php echo base64_encode($row->image);?>" height="187" width="110"/>
    <td data-label="Date:"><?php echo $row->date; //row created time ?></td>
  </tr>
  </tbody>
  <?php endwhile;?>
</table>
 </div>
<?php 
// no result show 
else: ?>
<h3>No Results found.</h3>
<?php endif; ?>

        <!-----------Javascript for Toggle Menu------->
        <script>
            var navLinks = document.getElementById("navLinks");
            function showMenu(){
                navLinks.style.right = "0";
            }
            function hideMenu(){
                navLinks.style.right = "-200px";
            }
        </script>
    
     <!------Footer------>

     <section class="footer">
        <h4>Follow Us</h4>
      <div class="icons">
          <i class="fa fa-facebook"></i>
          <i class="fa fa-twitter"></i>
          <i class="fa fa-instagram"></i>
          <i class="fa fa-snapchat"></i>
          <i class="fa fa-youtube"></i>
      </div>
    </section>
  </body>
</html>