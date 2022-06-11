<?php

// POST-request:
//--------------
$url = 'https://rest.arbeitsagentur.de/oauth/gettoken_cc';
$data = array(
    'client_id' => 'bd24f42e-ad0b-4005-b834-23bb6800dc6c', 
    'client_secret' => '6776b89e-5728-4643-8cd5-c93aefb5314b', 
    'grant_type' => 'client_credentials');
$options = array(
    'http' => array(
        'method'  => 'POST',
        'content' => http_build_query($data)
    )
);
$context  = stream_context_create($options);
$tokendata = file_get_contents($url, false, $context);
header('Content-Type: application/json'); 
if(isset($_GET['token']) & $_GET['token']==='TRUE'){
	echo $tokendata;
} else {
    // GET-request:
    //-------------
    $url = 'https://rest.arbeitsagentur.de/infosysbub/sprachfoerderung/pc/v1/bildungsangebot?'.$_SERVER['QUERY_STRING'];
    $options = array(
        'http' => array(
            'header'  => "OAuthAccessToken:".json_decode($tokendata, true)['access_token']." \r\n",
            'method'  => 'GET'    
        )
    );
    $context  = stream_context_create($options);
    $searchdata = file_get_contents($url, false, $context);
    echo $searchdata;
}
?>

