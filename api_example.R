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
url="https://rest.arbeitsagentur.de/infosysbub/sprachfoerderung/pc/v1/bildungsangebot?systematiken=MC&page=0&umkreis=bundesweit&sort=basc"
data_request=httr::GET(url=url, httr::add_headers(.headers=c("OAuthAccessToken"=token)),
        config=httr::config(connecttimeout=60))
data_request
data=rjson::fromJSON(rawToChar(httr::content(data_request)))
maxPage=data$page$totalPages
completeData=lapply(1:maxPage,function(i){
        print(i);
	rjson::fromJSON(rawToChar(httr::content(
		httr::GET(url=paste0("https://rest.arbeitsagentur.de/infosysbub/sprachfoerderung/pc/v1/bildungsangebot",
				"?systematiken=MC&page=",i,"&umkreis=bundesweit&sort=basc"), 
			httr::add_headers(.headers=c("OAuthAccessToken"=token)),
        		config=httr::config(connecttimeout=60))
		)))
})
