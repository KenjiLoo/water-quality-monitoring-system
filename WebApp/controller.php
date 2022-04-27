<?php
    include_once("connection.php");
    // Connection Created Successfully

    session_start();

    // Store All Errors
    $errors = [];

    // When Sign Up Button Clicked
    if (isset($_POST['signup'])) {
        $fullName = mysqli_real_escape_string($conn, $_POST['fullNname']);
        $userName = mysqli_real_escape_string($conn, $_POST['userNname']);
        $email = mysqli_real_escape_string($conn, $_POST['email']);
        $phoneNum = mysqli_real_escape_string($conn, $_POST['phoneNum']);

        // check password length if password is less then 8 character so
        if (strlen(trim($_POST['password'])) < 8) {
            $errors['password'] = 'Use 8 or more characters with a mix of letters, numbers & symbols';
        } else {
            // if password not matched so
            if ($_POST['password'] != $_POST['confirmPassword']) {
                $errors['password'] = 'Password not matched';
            } else {
                $password = md5($_POST['password']);
            }
        }
        // generate a random Code
        $code = rand(999999, 111111);
        // set Status
        //$status = "Not Verified";
        //$set_status = "UPDATE registration SET status = '$status'";
        //$setStatus = mysqli_query($conn, $set_status) or die("Query Failed");
        
        // echo 'first name = ' .$fname . "<br> last name = " .$lname . "<br> email = " .$email . "<br> password = " .$password . "<br> gender = " .$gender . "<br>";

        // check email validation and save information
        $sql = "SELECT * FROM registration WHERE email = '$email'";
        $res = mysqli_query($conn, $sql) or die('query failed');
        if (mysqli_num_rows($res) > 0) {
            $errors['email'] = 'Email is Already Taken';
        }

        // count erros
        if (count($errors) === 0) {
            //$insertQuery = "INSERT INTO registration (fullName,userName,email,phoneNum,password,code,status)
            //VALUES ('$fullname','$userName','$email',$phoneNum,'$password',$code,'$status')";
            $insertQuery = "INSERT INTO registration (fullName,userName,email,phoneNum,password,code)
            VALUES ('$fullname','$userName','$email',$phoneNum,'$password',$code)";
            $insertInfo = mysqli_query($conn, $insertQuery);

            // Send Varification Code In Gmail
            if ($insertInfo) {
                // Configure Your Server To Send Mail From Local Host Link In Video Description (How To Config LocalHost Server)
                $subject = 'Email Verification Code';
                $message = "Our verification code is $code";
                $sender = 'From: h2owateranalysis@gmail.com';

                if (mail($email, $subject, $message, $sender)) {
                    $message = "We've sent a verification code to your Email <br> $email";

                    $_SESSION['message'] = $message;
                    header('location: otp.php');
                } else {
                    $errors['otp_errors'] = 'Failed while sending code!';
                }
            } else {
                $errors['db_errors'] = "Failed while inserting data into database!";
            }
        }
    }

    // if Verify Button Clicked
    if (isset($_POST['verify'])) {
        $_SESSION['message'] = "";
        $otp = mysqli_real_escape_string($conn, $_POST['otp']);
        $otp_query = "SELECT * FROM registration WHERE code = $otp";
        $otp_result = mysqli_query($conn, $otp_query);

        if (mysqli_num_rows($otp_result) > 0) {
            $fetch_data = mysqli_fetch_assoc($otp_result);
            $fetch_code = $fetch_data['code'];

            //$update_status = "Verified";
            $update_code = 0;

            //$update_query = "UPDATE registration SET status = '$update_status' , code = $update_code WHERE code = $fetch_code";
            $update_query = "UPDATE registration SET code = $update_code WHERE code = $fetch_code";
            $update_result = mysqli_query($conn, $update_query);

            if ($update_result) {
                header('location: loginpage.php');
            } else {
                $errors['db_error'] = "Failed To Insering Data In Database!";
            }
        } else {
            $errors['otp_error'] = "You enter invalid verification code!";
        }
    }

    // if forgot button will clicked

    if (isset($_POST['forgot_password'])) {
        $email = $_POST['email'];
        $_SESSION['email'] = $email;

        $emailCheckQuery = "SELECT * FROM registration WHERE email = '$email'";
        $emailCheckResult = mysqli_query($conn, $emailCheckQuery);
        // if query run
        if ($emailCheckResult) {
            // if email matched
            if (mysqli_num_rows($emailCheckResult) > 0) {
                $code = rand(999999, 111111);
                $updateQuery = "UPDATE registration SET code = $code WHERE email = '$email'";
                $updateResult = mysqli_query($conn, $updateQuery);
                if ($updateResult) {

                    $subject = 'Email Verification Code for h2oWaterAnalysis';
                    $message = "Our verification code is $code";
                    $sender = 'From: h2owateranalysis@gmail.com';

                    if (mail($email, $subject, $message, $sender)) {
                        $message = "We've sent a verification code to your Email <br> $email";

                        $_SESSION['message'] = $message;
                        header('location: verifyEmail.php');
                    } else {
                        $errors['otp_errors'] = 'Failed while sending code!';
                    }
                } else {
                    $errors['db_errors'] = "Failed while inserting data into database!";
                }
            }else{
                $errors['invalidEmail'] = "Invalid Email Address";
            }
        }else {
            $errors['db_error'] = "Failed while checking email from database!";
        }
    }
if(isset($_POST['verifyEmail'])){
    $_SESSION['message'] = "";
    $OTPverify = mysqli_real_escape_string($conn, $_POST['OTPverify']);
    $verifyQuery = "SELECT * FROM registration WHERE code = $OTPverify";
    $runVerifyQuery = mysqli_query($conn, $verifyQuery);
    if($runVerifyQuery){
        if(mysqli_num_rows($runVerifyQuery) > 0){
            $newQuery = "UPDATE registration SET code = 0 WHERE email = '$email'";
            $run = mysqli_query($conn,$newQuery);
            header("location: newPassword.php");
        }else{
            $errors['verification_error'] = "Invalid Verification Code";
        }
    }else{
        $errors['db_error'] = "Failed while checking Verification Code from database!";
    }
}

// change Password
if(isset($_POST['changePassword'])){
    $password = ($_POST['password']);
    $confirmPassword = ($_POST['confirmPassword']);
    
    if (strlen($_POST['password']) < 8) {
        $errors['password_error'] = 'Use 8 or more characters with a mix of letters, numbers & symbols';
    } else {
        // if password not matched so
        if ($_POST['password'] != $_POST['confirmPassword']) {
            $errors['password_error'] = 'Password not matched';
        } else {
            $email = $_SESSION['email'];
            $updatePassword = "UPDATE registration SET password = '$password' WHERE email = '$email'";
            $updateconfirmPass = "UPDATE registration SET confirmPass = '$password' WHERE email = '$email'";
            $updatePass = mysqli_query($conn, $updatePassword) or die("Query Failed");
            $updateconfirm = mysqli_query($conn, $updateconfirmPass) or die("Query Failed");
            session_unset();
            session_destroy();
            header('location: index.php');
        }
    }
}