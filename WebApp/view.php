<h1>Notifications</h1>

<?php
    
    include("functions.php");

    $id = $_GET['id'];


    $query = "SELECT * from `results` where `id` = '$id';";
    if(count(fetchAll($query))>0){
        foreach(fetchAll($query) as $i){
            if($i['difference_percentage'] < 50){
            
                echo '<i style="color:red;">
      Warning! Water is considered dirty!</i> <br/>';
            }else{
                echo "Water is clean.";
           }
        }
    }
    
?><br/>
<a href="monitor.php">Back</a>