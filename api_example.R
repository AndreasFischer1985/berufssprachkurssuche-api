#----------------
# Simple Example
#----------------
install.packages(c("devtools","rjson","httr"))
devtools::install_github("AndreasFischer1985/qqBaseX")
clientId="bd24f42e-ad0b-4005-b834-23bb6800dc6c"
clientSecret="6776b89e-5728-4643-8cd5-c93aefb5314b"
postData=list( "grant_type"="client_credentials","client_id"=clientId,"client_secret"=clientSecret) 
token_request=httr::POST(
        url="https://rest.arbeitsagentur.de/oauth/gettoken_cc",
        body=postData,encode="form",
        config=httr::config(connecttimeout=60))
token=(httr::content(token_request, as='parsed')$access_token)
url="https://rest.arbeitsagentur.de/infosysbub/sprachfoerderung/pc/v1/bildungsangebot?systematiken=MC&page=0&umkreis=50&orte=Feucht_11.2147_49.375&sort=basc"
data_request=httr::GET(url=url, httr::add_headers(.headers=c("OAuthAccessToken"=token)),
        config=httr::config(connecttimeout=60))
data_request
data=rawToChar(httr::content(data_request))

