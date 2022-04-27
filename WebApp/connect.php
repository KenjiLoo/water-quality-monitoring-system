<?php
    session_start();
    $error ="Password and confirm pass are different! Please try again!";
    $success ="New record inserted Successfully!";
    $error2 ="There is an error, plaese try again!";
    $fullName = isset($_POST['fullName']) ? $_POST["fullName"] : "";
    $userName = isset($_POST['userName']) ? $_POST["userName"] : "";
    $email = isset($_POST['email']) ? $_POST["email"] : "";
    $phoneNum = isset($_POST['phoneNum']) ? $_POST["phoneNum"] : "";
    $password = isset($_POST['password']) ? $_POST["password"] : "";
    $confirmPass = isset($_POST['confirmPass']) ? $_POST["confirmPass"] : "";

    if (!empty($fullName) || !empty($userName) || !empty($email) || !empty($phoneNum) || !empty($password) || !empty($confirmPass)){
        $host = "localhost";
        $dbUsername = "root";
        $dbPassword = " ";
        $dbname = "hfyql1ju_SEGP";


        //create connection
        $conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);
        $errors = [];
        if(mysqli_connect_error()){
            die('Connect Error('. mysqli_connect_errno().')'. mysqli_connect_error());
        } else{
            $SELECT = "SELECT email FROM registration WHERE email = ? Limit 1";
            $INSERT = "INSERT Into registration (fullName, userName, email, phoneNum, password, confirmPass) values(?, ?, ?, ?, ?, ?)";
            
            //Prepare statement
            $stmt = $conn->prepare($SELECT);
            $stmt->bind_param("s",$email);
            $stmt->execute();
            $stmt->bind_result($email);
            $stmt->store_result();
            $rnum = $stmt->num_rows;

            if($rnum==0){
                $stmt->close();

                $stmt = $conn->prepare($INSERT);
                $stmt->bind_param("sssiss", $fullName, $userName, $email, $phoneNum, $password, $confirmPass);
                $stmt->execute();
                if($_POST['password'] === $_POST['confirmPass']){
                    $_SESSION["success"] = $success;
                    header("Location:registrationpage.php");
                } else{
                    $_SESSION["error"] = $error;
                    header("Location:registrationpage.php");
                }
            } else{
                $_SESSION["error2"] = $error2;
                header("Location: registrationpage.php");
            }
            $stmt->close();
            $conn->close();
        } 

    } else{
        $_SESSION["error2"] = $error2;
        header("Location: registrationpage.php");
    }
?>