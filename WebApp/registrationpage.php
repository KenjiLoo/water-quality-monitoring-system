<?php include_once ("controller.php"); ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="UTF-8">
        <title>Registration Form</title>
        <link rel="stylesheet" href="styles.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <meta name="viewport" content="width=devide-width, initial-scale=1.0">
    </head>

    <body>
        <div class="registration">
        <div class="container">
                <div class="title">Registration</div>
                    <div class="user-details">
                        <form action="connect.php" method="post">
                  
                        <div class="input-box">
                            <input type="text" placeholder="Enter Your Name" required name="fullName">
                        </div>
                        <div class="input-box">
                            <input type="text" placeholder="Enter Your Username" required name="userName">
                        </div>
                            <div class="input-box">
                            <input type="email" placeholder="Enter Your Email" required name="email">
                        </div>
                        <div class="input-box">
                            <input type="text" placeholder="Enter Your Phone Number" required name="phoneNum">
                        </div>
                        <div class="input-box">
                            <input type="password" placeholder="Enter Your Password" id="password" name="password" required>
                        </div>
                        <div class="input-box">
                            <input type="password" placeholder="Reconfirm your Password" id="confirmPass" name="confirmPass" required>
                        </div>
                        <script>
                            var state = false;
                            function togglePW(){
        
                            if(state){
                                document.getElementById("password").setAttribute("type","password");
                                state = false;
                            } else{
                                document.getElementById("password").setAttribute("type","text");
                                state = true;
                             }
                        }
                        </script>
                        
                    </div>
                    <div class="register-button">
                        <input type="submit" name="signup" value="register">
                    </div>
                    <div class="'signup_link">
                        Already have an Account? <a href="index.php" id="linkLogin">Login here</a>
                    </div>
                    <?php
                            if(isset($_SESSION["error"])){
                                $error = $_SESSION["error"];
                                echo"<i style='color: red'>$error</i>";
                            } elseif(isset($_SESSION["error2"])){
                                $error2 = $_SESSION["error2"];
                                echo"<i style='color: red'>$error2</i>";
                            } elseif(isset($_SESSION["success"])){
                                $success = $_SESSION["success"];
                                echo"<i style ='color: green'>$success</i>";
                            }
                    ?>
                </form>
                </div>  
                </div>
        </body>
</html>

<?php
    unset($_SESSION["error"]);
    unset($_SESSION["error2"]);
    unset($_SESSION["success"]);
?>
