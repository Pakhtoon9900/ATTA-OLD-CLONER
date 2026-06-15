import random
from random import choice as rc
from random import randint as rr

def get_real_ua():
    brands={"Realme":[("RMX3263","11"),("RMX3085","12"),("RMX3700","13"),("RMX3840","14"),("RMX3888","15")],"Xiaomi":[("M2010J19SG","11"),("MZB0A8L","12"),("2201116TG","13"),("2311DRK48G","14"),("2407FRK8G","15")],"Samsung":[("SM-M145P","11"),("SM-A135F","12"),("SM-S918B","13"),("SM-A556E","14"),("SM-S938B","15")],"Oppo":[("CPH2269","11"),("CPH2451","12"),("CPH2371","13"),("CPH2609","14"),("CPH2651","15")],"OnePlus":[("GM1901","11"),("IN2023","12"),("CPH2449","13"),("CPH2581","14"),("CPH2653","15")],"Infinix":[("X657","11"),("X6833B","12"),("X696","13"),("X6881","14"),("X6895","15")],"Google":[("Pixel 4a","11"),("Pixel 6","12"),("Pixel 7","13"),("Pixel 8","14"),("Pixel 9","15")]}
    chrome_versions={"11":["Chrome/141.0.7390.115","Chrome/142.0.7444.171","Chrome/143.0.7499.120"],"12":["Chrome/139.0.7258.158","Chrome/140.0.7339.145","Chrome/141.0.7390.115"],"13":["Chrome/137.0.7151.141","Chrome/138.0.7204.168","Chrome/139.0.7258.158"],"14":["Chrome/135.0.7049.100","Chrome/136.0.7103.60","Chrome/137.0.7151.141"],"15":["Chrome/133.0.6943.60","Chrome/134.0.6998.90","Chrome/135.0.7049.100"]}
    builds={"11":"RP1A.201005.001","12":"SP1A.210812.016","13":"TP1A.220905.001","14":"UP1A.231005.007","15":"AP1A.240905.006"}
    brand = random.choice(list(brands.keys()))
    model, android = random.choice(brands[brand])
    chrome = random.choice(chrome_versions[android])
    build = builds[android]
    ua = f"Mozilla/5.0 (Linux; Android {android}; {model} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 {chrome} Mobile Safari/537.36"
    return ua    


   
    
{
  ":method": "POST",
  ":authority": "www.facebook.com",
  ":path": "/api/graphql/",
  ":scheme": "https",
  "content-length": "10488",
  "sec-ch-ua-full-version-list": "\"Chromium\";v=\"148.0.0.0\", \"Google Chrome\";v=\"148.0.0.0\", \"Not/A)Brand\";v=\"99.0.0.0\"",
  "sec-ch-ua-platform": "\"Linux\"",
  "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
  "x-fb-friendly-name": "useCDSWebLoginMutation",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-model": "\"\"",
  "x-asbd-id": "359341",
  "x-fb-lsd": "AdRL3qOKFMTeMf3VxmCcBpMx8NA",
  "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
  "content-type": "application/x-www-form-urlencoded",
  "sec-ch-ua-platform-version": "\"\"",
  "accept": "*/*",
  "sec-gpc": "1",
  "accept-language": "en-US,en;q=0.6",
  "origin": "https://www.facebook.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://www.facebook.com/?skip_api_login=1&api_key=823425307723964&kid_directed_site=0&app_id=823425307723964&signed_next=1&next=https%3A%2F%2Foauth.facebook.com%2Fv2.4%2Fdialog%2Foauth%3Fapp_id%3D823425307723964%26cbt%3D1780665168001%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd251581d9082d253%2526domain%253Dwww.coursera.org%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.coursera.org%25252Ff56d8bc7f5b71006a%2526relation%253Dopener%26client_id%3D823425307723964%26display%3Dtouch%26domain%3Dwww.coursera.org%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.coursera.org%252F%253FauthMode%253Dlogin%26locale%3Den_US%26logger_id%3Df3df018733bbeb361%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfc7559ed6d55e3b18%2526domain%253Dwww.coursera.org%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.coursera.org%25252Ff56d8bc7f5b71006a%2526relation%253Dopener%2526frame%253Df881504cd5ed73379%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Dpublic_profile%252Cemail%252Cuser_friends%252Cuser_birthday%26sdk%3Djoey%26version%3Dv2.4%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfc7559ed6d55e3b18%26domain%3Dwww.coursera.org%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.coursera.org%252Ff56d8bc7f5b71006a%26relation%3Dopener%26frame%3Df881504cd5ed73379%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&is_business_login=0&refsrc=deprecated&_rdr",
  "accept-encoding": "gzip, deflate, br, zstd",
  "cookie": "wd=980x1873",
  "priority": "u=1, i"
}

{
  "av": "0",
  "__user": "0",
  "__a": "1",
  "__req": "5",
  "__hs": "20609.HYP:comet_loggedout_pkg.2.1...0",
  "dpr": "1",
  "__ccg": "GOOD",
  "__rev": "1040906968",
  "__s": "lwxa7z:767obf:xuj3yi",
  "__hsi": "7647898705894247812",
  "__dyn": "7xeUmwlE7ibwKBAg5S1Dxu13w8CewSwMwNw9G2S0lW4o0B-q1ew6ywaq0yE7i0n24oaEd86a3a1YwBgao6C0Mo2swaO4U2zxe2GewbS361qw8Xxm16wa-0raazo7u0zE2ZwrU6qE15E6O1FwlA1HGp1yU5N90HwtU1fEhw5yw66w9O3mdw",
  "__csr": "hAowjn14PskykKanAAhqClpty22aBxm48aECuEGuAuHBCGXh9oqym8Bx6FE8GzbAyUC26i0yEa47QAUoxZ28mKaG2rw-yolppHK17wWxyfKi2q2_zqxG1Mw7swqodo16-lAQfw7IwnEpwpE1dU0fA80cHU1Ro0HmdzUF0p83jAw0FlhK7At01lKU011zGxB035809TC08Xw8q1Da1jw0Eqw0O_w1spwf10et01Gq4Q01iahK7F604Q216ayU17FUvAw0x_wByk0NpFd05rw1h22206_k",
  "__hsdp": "ge541714O018q0cgwae085w0Isw2xU1vE",
  "__hblp": "0ba04do5y9w3482zw4hw961xwpo08lUuwdm0ki2i0a7w5-wJzE6a6821w6Uw23U8U98vxq0jq0IU2Bwj8",
  "__sjsp": "ge545hIl14O0",
  "__comet_req": "15",
  "locale": "en_GB",
  "lsd": "AdRL3qOKFMTeMf3VxmCcBpMx8NA",
  "jazoest": "22258",
  "__spin_r": "1040906968",
  "__spin_b": "trunk",
  "__spin_t": "1780665178",
  "qpl_active_flow_ids": "175125627,516759801",
  "fb_api_caller_class": "RelayModern",
  "fb_api_req_friendly_name": "useCDSWebLoginMutation",
  "server_timestamps": "true",
  "variables": "{\"input\":{\"actor_id\":\"0\",\"client_mutation_id\":\"1\",\"access_flow_version\":\"pre_mt_behavior\",\"app\":\"facebook\",\"auth_domain_data_key\":null,\"caa_login_request_extra_info\":{\"ab_test_data\":\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI\",\"shared_prefs_data\":\"eyIzMDAwMCI6W3sidCI6MTc4MDY2NTE4Mi41NDksImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS8ifSwidiI6ZmFsc2V9XSwiMzAwMDEiOlt7InQiOjE3ODA2NjUxODIuNTUsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS8ifSwidiI6MH1dLCIzMDAwMiI6W3sidCI6MTc4MDY2NTE4Mi41NTEsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS8ifSwidiI6MH1dLCIzMDAwMyI6W3sidCI6MTc4MDY2NTE4Mi41NTEsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS8ifSwidiI6WyJlbi1VUyJdfV0sIjMwMDA0IjpbeyJ0IjoxNzgwNjY1MTgyLjU1MiwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyJ9LCJlIjp7ImVjIjozfX1dLCIzMDAwNSI6W3sidCI6MTc4MDY2NTE4Mi41NTksImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS8ifSwidiI6eyJ3Ijo5ODAsImgiOjE2MTF9fV0sIjMwMDA3IjpbeyJ0IjoxNzgwNjY1MTgyLjU2LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOiJkZWZhdWx0In1dLCIzMDAwOCI6W3sidCI6MTc4MDY2NTE4Mi42MTUsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS8ifSwidiI6InByb21wdCJ9XSwiMzAwMTIiOlt7InQiOjE3ODA2NjUxODIuNTYzLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOiJHb29nbGUgSW5jLiJ9XSwiMzAwMTMiOlt7InQiOjE3ODA2NjUxODIuNTYzLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOiI1LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQ4LjAuMC4wIFNhZmFyaS81MzcuMzYifV0sIjMwMDE1IjpbeyJ0IjoxNzgwNjY1MTgyLjU2NCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyJ9LCJ2IjoiTGludXggYXJtdjgxIn1dLCIzMDAxOCI6W3sidCI6MTc4MDY2NTE4Mi41NjQsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS8ifSwidiI6N31dLCIzMDAyMiI6W3sidCI6MTc4MDY2NTE4Mi41OSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyJ9LCJ2Ijp0cnVlfV0sIjMwMDQwIjpbeyJ0IjoxNzgwNjY1MTgyLjU5MSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyJ9LCJ2IjotMzMwfV0sIjMwMDkzIjpbeyJ0IjoxNzgwNjY1MTgyLjU5MiwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyJ9LCJ2Ijo1fV0sIjMwMDk0IjpbeyJ0IjoxNzgwNjY1MTgyLjU5MiwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyJ9LCJ2IjoiTW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQ4LjAuMC4wIFNhZmFyaS81MzcuMzYifV0sIjMwMDk1IjpbeyJ0IjoxNzgwNjY1MTgyLjU5MywiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyJ9LCJ2IjoxfV0sIjMwMTA2IjpbeyJ0IjoxNzgwNjY1MTgyLjU0NywiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyJ9LCJ2IjpmYWxzZX0seyJ0IjoxNzgwNjY1MTg0LjE5MSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyJ9LCJ2Ijp0cnVlfV0sIjMwMTA3IjpbeyJ0IjoxNzgwNjY1MTgyLjU0OSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyJ9LCJ2IjpmYWxzZX0seyJ0IjoxNzgwNjY1MTg0LjA5MywiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyJ9LCJ2Ijp0cnVlfV19\",\"cuid\":\"\",\"guid\":\"f33fce4bde3904160\",\"jazoest\":\"22280\",\"lgndim\":\"eyJ3IjozNjAsImgiOjgyMCwiYXciOjM2MCwiYWgiOjgyMCwiYyI6MjR9\",\"lgnjs\":\"1780665182\",\"lgnrnd\":\"061258_SRva\",\"locale\":\"en_GB\",\"login_source\":\"comet_headerless_login\",\"lsd\":\"AdRL3qOKFMTeMf3VxmCcBpMx-WY\",\"next\":\"https://oauth.facebook.com/v2.4/dialog/oauth?app_id=823425307723964&cbt=1780665168001&channel_url=https%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd251581d9082d253%2526domain%253Dwww.coursera.org%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.coursera.org%25252Ff56d8bc7f5b71006a%2526relation%253Dopener&client_id=823425307723964&display=touch&domain=www.coursera.org&e2e=%257B%257D&fallback_redirect_uri=https%253A%252F%252Fwww.coursera.org%252F%253FauthMode%253Dlogin&locale=en_US&logger_id=f3df018733bbeb361&origin=2&redirect_uri=https%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfc7559ed6d55e3b18%2526domain%253Dwww.coursera.org%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.coursera.org%25252Ff56d8bc7f5b71006a%2526relation%253Dopener%2526frame%253Df881504cd5ed73379&response_type=token%252Csigned_request%252Cgraph_domain&return_scopes=true&scope=public_profile%252Cemail%252Cuser_friends%252Cuser_birthday&sdk=joey&version=v2.4&ret=login&fbapp_pres=0&tp=unspecified\",\"prefill_contact_point\":\"\",\"prefill_source\":\"\",\"prefill_type\":\"\",\"skstamp\":\"\",\"timezone\":\"-330\"},\"credential_type\":\"password\",\"dyi_job_id\":\"\",\"enc_password\":{\"sensitive_string_value\":\"#PWD_BROWSER:5:1780665189:AWZQAFJWvYWDLlb8f7qlOwErsxFqx2gVlVb/5pf3yBUoRLED4WmPvOgWDW3wTbTdAx/CpvgDs/+wx3HLIeqwgG+3hQgR+oDeholndlh40iQ8sk/zUOilZvLheHJwmEJpSbMFQczHUQY6Ntds\"},\"event_request_id\":\"471ba3f9-e838-418b-b73e-1168db4c1a6e\",\"identifier\":\"629749393\",\"ig_web_device_id\":null,\"initial_request_id\":\"1\",\"lids\":null,\"login_source\":\"COMET_HEADERLESS_LOGIN\",\"next\":\"https://oauth.facebook.com/v2.4/dialog/oauth?app_id=823425307723964&cbt=1780665168001&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfd251581d9082d253%26domain%3Dwww.coursera.org%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.coursera.org%252Ff56d8bc7f5b71006a%26relation%3Dopener&client_id=823425307723964&display=touch&domain=www.coursera.org&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.coursera.org%2F%3FauthMode%3Dlogin&locale=en_US&logger_id=f3df018733bbeb361&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfc7559ed6d55e3b18%26domain%3Dwww.coursera.org%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.coursera.org%252Ff56d8bc7f5b71006a%26relation%3Dopener%26frame%3Df881504cd5ed73379&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&scope=public_profile%2Cemail%2Cuser_friends%2Cuser_birthday&sdk=joey&version=v2.4&ret=login&fbapp_pres=0&tp=unspecified\",\"passkey_payload\":null,\"password\":{\"sensitive_string_value\":\"#PWD_BROWSER:5:1780665189:AWZQAFJWvYWDLlb8f7qlOwErsxFqx2gVlVb/5pf3yBUoRLED4WmPvOgWDW3wTbTdAx/CpvgDs/+wx3HLIeqwgG+3hQgR+oDeholndlh40iQ8sk/zUOilZvLheHJwmEJpSbMFQczHUQY6Ntds\"},\"persistent\":true,\"query_params\":\"{\\\"skip_api_login\\\":\\\"1\\\",\\\"api_key\\\":\\\"823425307723964\\\",\\\"kid_directed_site\\\":\\\"0\\\",\\\"app_id\\\":\\\"823425307723964\\\",\\\"signed_next\\\":\\\"1\\\",\\\"next\\\":\\\"https://oauth.facebook.com/v2.4/dialog/oauth?app_id=823425307723964&cbt=1780665168001&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfd251581d9082d253%26domain%3Dwww.coursera.org%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.coursera.org%252Ff56d8bc7f5b71006a%26relation%3Dopener&client_id=823425307723964&display=touch&domain=www.coursera.org&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.coursera.org%2F%3FauthMode%3Dlogin&locale=en_US&logger_id=f3df018733bbeb361&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfc7559ed6d55e3b18%26domain%3Dwww.coursera.org%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.coursera.org%252Ff56d8bc7f5b71006a%26relation%3Dopener%26frame%3Df881504cd5ed73379&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&scope=public_profile%2Cemail%2Cuser_friends%2Cuser_birthday&sdk=joey&version=v2.4&ret=login&fbapp_pres=0&tp=unspecified\\\",\\\"cancel_url\\\":\\\"https://staticxx.facebook.com/x/connect/xd_arbiter/?version=46#cb=fc7559ed6d55e3b18&domain=www.coursera.org&is_canvas=false&origin=https%3A%2F%2Fwww.coursera.org%2Ff56d8bc7f5b71006a&relation=opener&frame=f881504cd5ed73379&error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied\\\",\\\"display\\\":\\\"touch\\\",\\\"locale\\\":\\\"en_GB\\\",\\\"pl_dbl\\\":\\\"0\\\",\\\"is_business_login\\\":\\\"0\\\",\\\"refsrc\\\":\\\"deprecated\\\",\\\"_rdr\\\":null}\",\"trusted_device_records\":\"{}\",\"use_uid_to_login\":false,\"waterfall_id\":\"e573bbe5-b354-45d8-9cf7-2039ba2c93c0\"},\"scale\":1}",
  "doc_id": "9807605492696448",
  "fb_api_analytics_tags": "[\"qpl_active_flow_ids=175125627,516759801\"]"
}

https://oauth.facebook.com/oauth/dialog/login.php?skip_api_login=1&api_key=823425307723964&kid_directed_site=0&app_id=823425307723964&signed_next=1&next=https%3A%2F%2Foauth.facebook.com%2Fv2.4%2Fdialog%2Foauth%3Fapp_id%3D823425307723964%26cbt%3D1780665168001%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd251581d9082d253%2526domain%253Dwww.coursera.org%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.coursera.org%25252Ff56d8bc7f5b71006a%2526relation%253Dopener%26client_id%3D823425307723964%26display%3Dtouch%26domain%3Dwww.coursera.org%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.coursera.org%252F%253FauthMode%253Dlogin%26locale%3Den_US%26logger_id%3Df3df018733bbeb361%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfc7559ed6d55e3b18%2526domain%253Dwww.coursera.org%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.coursera.org%25252Ff56d8bc7f5b71006a%2526relation%253Dopener%2526frame%253Df881504cd5ed73379%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Dpublic_profile%252Cemail%252Cuser_friends%252Cuser_birthday%26sdk%3Djoey%26version%3Dv2.4%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfc7559ed6d55e3b18%26domain%3Dwww.coursera.org%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.coursera.org%252Ff56d8bc7f5b71006a%26relation%3Dopener%26frame%3Df881504cd5ed73379%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&is_business_login=0&refsrc=deprecated&_rdr


###Graphql###&&__

##BLOCKSSSS_####

https://oauth.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=021718b2ffa2bddc0057512aaf38c6b2c089ed2476781266404734663e9e8403

{
  ":method": "POST",
  ":authority": "oauth.facebook.com",
  ":path": "/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=021718b2ffa2bddc0057512aaf38c6b2c089ed2476781266404734663e9e8403",
  ":scheme": "https",
  "content-length": "5963",
  "sec-ch-ua-full-version-list": "\"Chromium\";v=\"148.0.0.0\", \"Google Chrome\";v=\"148.0.0.0\", \"Not/A)Brand\";v=\"99.0.0.0\"",
  "sec-ch-ua-platform": "\"Android\"",
  "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
  "sec-ch-ua-model": "\"\"",
  "sec-ch-ua-mobile": "?1",
  "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36",
  "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
  "sec-ch-ua-platform-version": "\"14.0.0\"",
  "accept": "*/*",
  "sec-gpc": "1",
  "accept-language": "en-US,en;q=0.6",
  "origin": "https://oauth.facebook.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://oauth.facebook.com/oauth/dialog/login.php?skip_api_login=1&api_key=823425307723964&kid_directed_site=0&app_id=823425307723964&signed_next=1&next=https%3A%2F%2Foauth.facebook.com%2Fv2.4%2Fdialog%2Foauth%3Fapp_id%3D823425307723964%26cbt%3D1780665513452%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1b62d218004d21d9%2526domain%253Dwww.coursera.org%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.coursera.org%25252Ffe0eaeebadcde5b9d%2526relation%253Dopener%26client_id%3D823425307723964%26display%3Dtouch%26domain%3Dwww.coursera.org%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.coursera.org%252F%253FauthMode%253Dlogin%26locale%3Den_US%26logger_id%3Df4329733532d9f1d7%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df30aa0e9aa98d4092%2526domain%253Dwww.coursera.org%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.coursera.org%25252Ffe0eaeebadcde5b9d%2526relation%253Dopener%2526frame%253Dfcf741fd0879458ca%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Dpublic_profile%252Cemail%252Cuser_friends%252Cuser_birthday%26sdk%3Djoey%26version%3Dv2.4%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df30aa0e9aa98d4092%26domain%3Dwww.coursera.org%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.coursera.org%252Ffe0eaeebadcde5b9d%26relation%3Dopener%26frame%3Dfcf741fd0879458ca%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&is_business_login=0&refsrc=deprecated",
  "accept-encoding": "gzip, deflate, br, zstd",
  "cookie": "fr=0mdVDOJ67TYVy4GDY..BqHUN9..AAA.0.0.BqIsyx.AWcmDVq3nu536OGFP2_6hy9GYW0",
  "priority": "u=1, i"
}

{
  "__aaid": "0",
  "__user": "0",
  "__a": "1",
  "__req": "4",
  "__hs": "20609.BP:wbloks_caa_pkg.2.0...0",
  "dpr": "3",
  "__ccg": "GOOD",
  "__rev": "1040911178",
  "__s": "uy9u66:5m173m:grkqse",
  "__hsi": "7647900148818652532",
  "__dyn": "0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jwea",
  "locale": "en_GB",
  "fb_dtsg": "NAfzlOUh6vbU4LyGG7UZWXGZJq1upSKAYEnP_Hm4gxJYdb8m6CsGP6Q:0:0",
  "jazoest": "24902",
  "lsd": "AdRL3qOKFMTeMf3VxmCcBpMxiB4",
  "params": "{\"params\":\"{\\\"server_params\\\":{\\\"next_uri\\\":\\\"https://oauth.facebook.com/v2.4/dialog/oauth?app_id=823425307723964&cbt=1780665513452&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1b62d218004d21d9%26domain%3Dwww.coursera.org%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.coursera.org%252Ffe0eaeebadcde5b9d%26relation%3Dopener&client_id=823425307723964&display=touch&domain=www.coursera.org&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.coursera.org%2F%3FauthMode%3Dlogin&locale=en_US&logger_id=f4329733532d9f1d7&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df30aa0e9aa98d4092%26domain%3Dwww.coursera.org%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.coursera.org%252Ffe0eaeebadcde5b9d%26relation%3Dopener%26frame%3Dfcf741fd0879458ca&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&scope=public_profile%2Cemail%2Cuser_friends%2Cuser_birthday&sdk=joey&version=v2.4&ret=login&fbapp_pres=0&tp=unspecified\\\",\\\"credential_type\\\":\\\"password\\\",\\\"username_text_input_id\\\":\\\"y9sse9:58\\\",\\\"password_text_input_id\\\":\\\"y9sse9:59\\\",\\\"login_source\\\":\\\"Login\\\",\\\"login_credential_type\\\":\\\"none\\\",\\\"server_login_source\\\":\\\"login\\\",\\\"ar_event_source\\\":\\\"login_home_page\\\",\\\"should_trigger_override_login_success_action\\\":0,\\\"should_trigger_override_login_2fa_action\\\":0,\\\"is_caa_perf_enabled\\\":0,\\\"reg_flow_source\\\":\\\"login_home_native_integration_point\\\",\\\"caller\\\":\\\"gslr\\\",\\\"is_from_landing_page\\\":0,\\\"is_from_empty_password\\\":0,\\\"is_from_aymh\\\":0,\\\"is_from_password_entry_page\\\":0,\\\"is_from_assistive_id\\\":0,\\\"is_from_msplit_fallback\\\":0,\\\"two_step_login_type\\\":\\\"one_step_login\\\",\\\"left_nav_button_action\\\":\\\"NONE\\\",\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"INTERNAL__latency_qpl_instance_id\\\":\\\"207230969700199\\\",\\\"device_id\\\":null,\\\"family_device_id\\\":null,\\\"waterfall_id\\\":null,\\\"offline_experiment_group\\\":null,\\\"layered_homepage_experiment_group\\\":null,\\\"is_platform_login\\\":0,\\\"is_from_logged_in_switcher\\\":0,\\\"is_from_logged_out\\\":0,\\\"access_flow_version\\\":\\\"pre_mt_behavior\\\",\\\"login_surface\\\":\\\"login_home\\\",\\\"login_entry_point\\\":\\\"logged_out\\\"},\\\"client_input_params\\\":{\\\"machine_id\\\":\\\"\\\",\\\"cloud_trust_token\\\":null,\\\"block_store_machine_id\\\":\\\"\\\",\\\"zero_balance_state\\\":\\\"\\\",\\\"contact_point\\\":\\\"6293739390\\\",\\\"password\\\":\\\"#PWD_BROWSER:5:1780665521:AWZQABIOiu/7ACVnVvTDSK8hYfy+ZHzAqYI7nPp2G4UJAl9iEX96g/D5zh+g9KL+7laHZ5/KUyZVetd8pkmC5E9v50mhlJaZTTMgJxbgPJrotitkgGRPtaO1Leur7rpI4oYLclRCDGRyRMoG\\\",\\\"accounts_list\\\":[],\\\"fb_ig_device_id\\\":[],\\\"secure_family_device_id\\\":\\\"\\\",\\\"encrypted_msisdn\\\":\\\"\\\",\\\"headers_infra_flow_id\\\":\\\"\\\",\\\"try_num\\\":1,\\\"login_attempt_count\\\":1,\\\"event_flow\\\":\\\"login_manual\\\",\\\"event_step\\\":\\\"home_page\\\",\\\"openid_tokens\\\":{},\\\"auth_secure_device_id\\\":\\\"\\\",\\\"client_known_key_hash\\\":\\\"\\\",\\\"has_whatsapp_installed\\\":0,\\\"sso_token_map_json_string\\\":\\\"\\\",\\\"should_show_nested_nta_from_aymh\\\":0,\\\"gms_incoming_call_retriever_eligibility\\\":\\\"client_not_supported\\\",\\\"password_contains_non_ascii\\\":\\\"false\\\",\\\"has_granted_read_contacts_permissions\\\":0,\\\"has_granted_read_phone_permissions\\\":0,\\\"app_manager_id\\\":\\\"\\\",\\\"aymh_accounts\\\":[{\\\"id\\\":\\\"\\\",\\\"profiles\\\":{\\\"id\\\":{\\\"user_id\\\":\\\"\\\",\\\"name\\\":\\\"\\\",\\\"profile_picture_url\\\":\\\"\\\",\\\"small_profile_picture_url\\\":null,\\\"notification_count\\\":0,\\\"credential_type\\\":\\\"none\\\",\\\"token\\\":\\\"\\\",\\\"last_access_time\\\":0,\\\"is_derived\\\":0,\\\"username\\\":\\\"\\\",\\\"password\\\":\\\"\\\",\\\"has_smartlock\\\":0,\\\"account_center_id\\\":\\\"\\\",\\\"account_source\\\":\\\"\\\",\\\"credentials\\\":[],\\\"nta_eligibility_reason\\\":null,\\\"from_accurate_privacy_result\\\":0,\\\"dbln_validated\\\":0}}}],\\\"sso_accounts_auth_data\\\":[],\\\"blocked_uids\\\":[],\\\"network_bssid\\\":null,\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\"},\\\"aac\\\":\\\"\\\"}}\"}"
}

####DEVICEEE####LOCGINNN_####

GET URL= https://oauth.facebook.com/oauth/dialog/login.php?skip_api_login=1&api_key=313137469260&kid_directed_site=0&app_id=313137469260&signed_next=1&next=https%3A%2F%2Foauth.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D313137469260%26cbt%3D1780665805614%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df0a148c9644153d3c%2526domain%253Dwww.udemy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252Ffab0fe2a641bc0012%2526relation%253Dopener%26client_id%3D313137469260%26display%3Dtouch%26domain%3Dwww.udemy.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.udemy.com%252Fjoin%252Fpasswordless-auth%252F%253Flocale%253Den_US%2526next%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252F%25253Futm_campaign%25253DBrand-Udemy_la.EN_cc.India_dev.%252526utm_source%25253Dgoogle%252526utm_medium%25253Dpaid-search%252526portfolio%25253DBrandDirect%252526utm_audience%25253Dmx%252526utm_tactic%25253Dbrand%252526utm_term%25253D_._ag_133043842301_._ad_595460368494_._kw_udemy%252526utm_content%25253Dg%252526funnel%25253D%252526test%25253D%252526gad_source%25253D1%252526gad_campaignid%25253D17099057432%252526gbraid%25253D0AAAAADROdO3kQMqW6PhSENUk4n46puNRq%252526gclid%25253DEAIaIQobChMI1KqD6JjwlAMV26NLBR3S1w99EAAYASAAEgLDdvD_BwE%2526response_type%253Dhtml%2526action%253Dlogin%2526mode%26locale%3Den_US%26logger_id%3Dfd6c649320c0e272e%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df999f791f4a7561fb%2526domain%253Dwww.udemy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252Ffab0fe2a641bc0012%2526relation%253Dopener%2526frame%253Df51ab5f50a93813c2%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv18.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df999f791f4a7561fb%26domain%3Dwww.udemy.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.udemy.com%252Ffab0fe2a641bc0012%26relation%3Dopener%26frame%3Df51ab5f50a93813c2%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&is_business_login=0&refsrc=deprecated

POST URL= https://oauth.facebook.com/login/device-based/login/async/?api_key=313137469260&auth_token=85cb936b10de7ebb3e82154471cb59a8&skip_api_login=1&signed_next=1&next=https%3A%2F%2Foauth.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D313137469260%26cbt%3D1780665805614%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df0a148c9644153d3c%2526domain%253Dwww.udemy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252Ffab0fe2a641bc0012%2526relation%253Dopener%26client_id%3D313137469260%26display%3Dtouch%26domain%3Dwww.udemy.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.udemy.com%252Fjoin%252Fpasswordless-auth%252F%253Flocale%253Den_US%2526next%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252F%25253Futm_campaign%25253DBrand-Udemy_la.EN_cc.India_dev.%252526utm_source%25253Dgoogle%252526utm_medium%25253Dpaid-search%252526portfolio%25253DBrandDirect%252526utm_audience%25253Dmx%252526utm_tactic%25253Dbrand%252526utm_term%25253D_._ag_133043842301_._ad_595460368494_._kw_udemy%252526utm_content%25253Dg%252526funnel%25253D%252526test%25253D%252526gad_source%25253D1%252526gad_campaignid%25253D17099057432%252526gbraid%25253D0AAAAADROdO3kQMqW6PhSENUk4n46puNRq%252526gclid%25253DEAIaIQobChMI1KqD6JjwlAMV26NLBR3S1w99EAAYASAAEgLDdvD_BwE%2526response_type%253Dhtml%2526action%253Dlogin%2526mode%26locale%3Den_US%26logger_id%3Dfd6c649320c0e272e%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df999f791f4a7561fb%2526domain%253Dwww.udemy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252Ffab0fe2a641bc0012%2526relation%253Dopener%2526frame%253Df51ab5f50a93813c2%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv18.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=313137469260&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df999f791f4a7561fb%26domain%3Dwww.udemy.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.udemy.com%252Ffab0fe2a641bc0012%26relation%3Dopener%26frame%3Df51ab5f50a93813c2%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100

{
  ":method": "POST",
  ":authority": "oauth.facebook.com",
  ":path": "/login/device-based/login/async/?api_key=313137469260&auth_token=85cb936b10de7ebb3e82154471cb59a8&skip_api_login=1&signed_next=1&next=https%3A%2F%2Foauth.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D313137469260%26cbt%3D1780665805614%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df0a148c9644153d3c%2526domain%253Dwww.udemy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252Ffab0fe2a641bc0012%2526relation%253Dopener%26client_id%3D313137469260%26display%3Dtouch%26domain%3Dwww.udemy.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.udemy.com%252Fjoin%252Fpasswordless-auth%252F%253Flocale%253Den_US%2526next%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252F%25253Futm_campaign%25253DBrand-Udemy_la.EN_cc.India_dev.%252526utm_source%25253Dgoogle%252526utm_medium%25253Dpaid-search%252526portfolio%25253DBrandDirect%252526utm_audience%25253Dmx%252526utm_tactic%25253Dbrand%252526utm_term%25253D_._ag_133043842301_._ad_595460368494_._kw_udemy%252526utm_content%25253Dg%252526funnel%25253D%252526test%25253D%252526gad_source%25253D1%252526gad_campaignid%25253D17099057432%252526gbraid%25253D0AAAAADROdO3kQMqW6PhSENUk4n46puNRq%252526gclid%25253DEAIaIQobChMI1KqD6JjwlAMV26NLBR3S1w99EAAYASAAEgLDdvD_BwE%2526response_type%253Dhtml%2526action%253Dlogin%2526mode%26locale%3Den_US%26logger_id%3Dfd6c649320c0e272e%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df999f791f4a7561fb%2526domain%253Dwww.udemy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252Ffab0fe2a641bc0012%2526relation%253Dopener%2526frame%253Df51ab5f50a93813c2%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv18.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=313137469260&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df999f791f4a7561fb%26domain%3Dwww.udemy.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.udemy.com%252Ffab0fe2a641bc0012%26relation%3Dopener%26frame%3Df51ab5f50a93813c2%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100",
  ":scheme": "https",
  "content-length": "2097",
  "sec-ch-ua": "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  "sec-ch-ua-mobile": "?1",
  "user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
  "x-response-format": "JSONStream",
  "content-type": "application/x-www-form-urlencoded",
  "x-fb-lsd": "AdQ0rZHafUVR7XkjnxS3WFrrt3c",
  "sec-ch-ua-platform-version": "\"14.0.0\"",
  "x-requested-with": "XMLHttpRequest",
  "x-asbd-id": "359341",
  "sec-ch-ua-full-version-list": "\"Chromium\";v=\"137.0.7337.0\", \"Not/A)Brand\";v=\"24.0.0.0\"",
  "sec-ch-ua-model": "\"Infinix X6711\"",
  "sec-ch-prefers-color-scheme": "light",
  "sec-ch-ua-platform": "\"Android\"",
  "accept": "*/*",
  "origin": "https://oauth.facebook.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://oauth.facebook.com/oauth/dialog/login.php?skip_api_login=1&api_key=313137469260&kid_directed_site=0&app_id=313137469260&signed_next=1&next=https%3A%2F%2Foauth.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D313137469260%26cbt%3D1780665805614%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df0a148c9644153d3c%2526domain%253Dwww.udemy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252Ffab0fe2a641bc0012%2526relation%253Dopener%26client_id%3D313137469260%26display%3Dtouch%26domain%3Dwww.udemy.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.udemy.com%252Fjoin%252Fpasswordless-auth%252F%253Flocale%253Den_US%2526next%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252F%25253Futm_campaign%25253DBrand-Udemy_la.EN_cc.India_dev.%252526utm_source%25253Dgoogle%252526utm_medium%25253Dpaid-search%252526portfolio%25253DBrandDirect%252526utm_audience%25253Dmx%252526utm_tactic%25253Dbrand%252526utm_term%25253D_._ag_133043842301_._ad_595460368494_._kw_udemy%252526utm_content%25253Dg%252526funnel%25253D%252526test%25253D%252526gad_source%25253D1%252526gad_campaignid%25253D17099057432%252526gbraid%25253D0AAAAADROdO3kQMqW6PhSENUk4n46puNRq%252526gclid%25253DEAIaIQobChMI1KqD6JjwlAMV26NLBR3S1w99EAAYASAAEgLDdvD_BwE%2526response_type%253Dhtml%2526action%253Dlogin%2526mode%26locale%3Den_US%26logger_id%3Dfd6c649320c0e272e%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df999f791f4a7561fb%2526domain%253Dwww.udemy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252Ffab0fe2a641bc0012%2526relation%253Dopener%2526frame%253Df51ab5f50a93813c2%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv18.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df999f791f4a7561fb%26domain%3Dwww.udemy.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.udemy.com%252Ffab0fe2a641bc0012%26relation%3Dopener%26frame%3Df51ab5f50a93813c2%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&is_business_login=0&refsrc=deprecated",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "en-US,en;q=0.9",
  "cookie": "fr=0sEcxkiuf6OhXOZDH..BqIs3P..AAA.0.0.BqIs3v.AWfh80USrQxLWO6ymnJALXpd53E"
}

{
  ":method": "POST",
  ":authority": "oauth.facebook.com",
  ":path": "/login/device-based/login/async/?api_key=313137469260&auth_token=85cb936b10de7ebb3e82154471cb59a8&skip_api_login=1&signed_next=1&next=https%3A%2F%2Foauth.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D313137469260%26cbt%3D1780665805614%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df0a148c9644153d3c%2526domain%253Dwww.udemy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252Ffab0fe2a641bc0012%2526relation%253Dopener%26client_id%3D313137469260%26display%3Dtouch%26domain%3Dwww.udemy.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.udemy.com%252Fjoin%252Fpasswordless-auth%252F%253Flocale%253Den_US%2526next%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252F%25253Futm_campaign%25253DBrand-Udemy_la.EN_cc.India_dev.%252526utm_source%25253Dgoogle%252526utm_medium%25253Dpaid-search%252526portfolio%25253DBrandDirect%252526utm_audience%25253Dmx%252526utm_tactic%25253Dbrand%252526utm_term%25253D_._ag_133043842301_._ad_595460368494_._kw_udemy%252526utm_content%25253Dg%252526funnel%25253D%252526test%25253D%252526gad_source%25253D1%252526gad_campaignid%25253D17099057432%252526gbraid%25253D0AAAAADROdO3kQMqW6PhSENUk4n46puNRq%252526gclid%25253DEAIaIQobChMI1KqD6JjwlAMV26NLBR3S1w99EAAYASAAEgLDdvD_BwE%2526response_type%253Dhtml%2526action%253Dlogin%2526mode%26locale%3Den_US%26logger_id%3Dfd6c649320c0e272e%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df999f791f4a7561fb%2526domain%253Dwww.udemy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252Ffab0fe2a641bc0012%2526relation%253Dopener%2526frame%253Df51ab5f50a93813c2%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv18.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=313137469260&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df999f791f4a7561fb%26domain%3Dwww.udemy.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.udemy.com%252Ffab0fe2a641bc0012%26relation%3Dopener%26frame%3Df51ab5f50a93813c2%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100",
  ":scheme": "https",
  "content-length": "2097",
  "sec-ch-ua": "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  "sec-ch-ua-mobile": "?1",
  "user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
  "x-response-format": "JSONStream",
  "content-type": "application/x-www-form-urlencoded",
  "x-fb-lsd": "AdQ0rZHafUVR7XkjnxS3WFrrt3c",
  "sec-ch-ua-platform-version": "\"14.0.0\"",
  "x-requested-with": "XMLHttpRequest",
  "x-asbd-id": "359341",
  "sec-ch-ua-full-version-list": "\"Chromium\";v=\"137.0.7337.0\", \"Not/A)Brand\";v=\"24.0.0.0\"",
  "sec-ch-ua-model": "\"Infinix X6711\"",
  "sec-ch-prefers-color-scheme": "light",
  "sec-ch-ua-platform": "\"Android\"",
  "accept": "*/*",
  "origin": "https://oauth.facebook.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://oauth.facebook.com/oauth/dialog/login.php?skip_api_login=1&api_key=313137469260&kid_directed_site=0&app_id=313137469260&signed_next=1&next=https%3A%2F%2Foauth.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D313137469260%26cbt%3D1780665805614%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df0a148c9644153d3c%2526domain%253Dwww.udemy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252Ffab0fe2a641bc0012%2526relation%253Dopener%26client_id%3D313137469260%26display%3Dtouch%26domain%3Dwww.udemy.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.udemy.com%252Fjoin%252Fpasswordless-auth%252F%253Flocale%253Den_US%2526next%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252F%25253Futm_campaign%25253DBrand-Udemy_la.EN_cc.India_dev.%252526utm_source%25253Dgoogle%252526utm_medium%25253Dpaid-search%252526portfolio%25253DBrandDirect%252526utm_audience%25253Dmx%252526utm_tactic%25253Dbrand%252526utm_term%25253D_._ag_133043842301_._ad_595460368494_._kw_udemy%252526utm_content%25253Dg%252526funnel%25253D%252526test%25253D%252526gad_source%25253D1%252526gad_campaignid%25253D17099057432%252526gbraid%25253D0AAAAADROdO3kQMqW6PhSENUk4n46puNRq%252526gclid%25253DEAIaIQobChMI1KqD6JjwlAMV26NLBR3S1w99EAAYASAAEgLDdvD_BwE%2526response_type%253Dhtml%2526action%253Dlogin%2526mode%26locale%3Den_US%26logger_id%3Dfd6c649320c0e272e%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df999f791f4a7561fb%2526domain%253Dwww.udemy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.udemy.com%25252Ffab0fe2a641bc0012%2526relation%253Dopener%2526frame%253Df51ab5f50a93813c2%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv18.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df999f791f4a7561fb%26domain%3Dwww.udemy.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.udemy.com%252Ffab0fe2a641bc0012%26relation%3Dopener%26frame%3Df51ab5f50a93813c2%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&is_business_login=0&refsrc=deprecated",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "en-US,en;q=0.9",
  "cookie": "fr=0sEcxkiuf6OhXOZDH..BqIs3P..AAA.0.0.BqIs3v.AWfh80USrQxLWO6ymnJALXpd53E"
}

{
  "m_ts": "1780665836",
  "li": "7M0ianq_QoXQ3kQkg1y3PuBl",
  "try_number": "0",
  "unrecognized_tries": "0",
  "email": "0840383030",
  "prefill_contact_point": "",
  "prefill_source": "",
  "prefill_type": "",
  "first_prefill_source": "",
  "first_prefill_type": "",
  "had_cp_prefilled": "false",
  "had_password_prefilled": "false",
  "is_smart_lock": "false",
  "bi_xrwh": "0",
  "bi_wvdp": "{\"hwc\":true,\"hwcr\":false,\"has_dnt\":true,\"has_standalone\":false,\"wnd_toStr_toStr\":\"function toString() { [native code] }\",\"hasPerm\":true,\"permission_query_toString\":\"function query() { [native code] }\",\"permission_query_toString_toString\":\"function toString() { [native code] }\",\"has_seWo\":true,\"has_meDe\":true,\"has_creds\":true,\"has_hwi_bt\":false,\"has_agjsi\":false,\"iframeProto\":\"function get contentWindow() { [native code] }\",\"remap\":false,\"iframeData\":{\"hwc\":true,\"hwcr\":false,\"has_dnt\":true,\"has_standalone\":false,\"wnd_toStr_toStr\":\"function toString() { [native code] }\",\"hasPerm\":true,\"permission_query_toString\":\"function query() { [native code] }\",\"permission_query_toString_toString\":\"function toString() { [native code] }\",\"has_seWo\":true,\"has_meDe\":true,\"has_creds\":true,\"has_hwi_bt\":false,\"has_agjsi\":false}}",
  "encpass": "#PWD_BROWSER:5:1780665846:AWZQAMuvtmhxXwGK9hkMlECDUbjGKZQHR40C/Da/URomOT0Ea2xiJj5zZoUoqt1QwJNPTG8PY5/kbblWOdJawcxFm9iQ61k2Vc6/CSQaI0SOKdGunN4kLJFJpyYNw0OJe4y3mDIuV+L13JAgPg==",
  "fb_dtsg": "NAfxMY1AbIzrcnV_3xxxhyHHw2s04UQlirj6h6tPs69aDIA_pZ5fluA:0:0",
  "jazoest": "25096",
  "lsd": "AdQ0rZHafUVR7XkjnxS3WFrrt3c",
  "__dyn": "1KQdAG1mws8-t0BBBzEnwuo98nwgU2owpUuwcC4o1nEhw23E52q1ew6ywaq1Jw20Ehw73wGwcq0RE1u81x82ew5fw5NyE1582ZwrU2pw4swSw7zwde0UE",
  "__csr": "",
  "__hsdp": "",
  "__hblp": "",
  "__sjsp": "",
  "__req": "2",
  "__fmt": "1",
  "__a": "AYwBkmfca1wh1es-amNW2ZUqpgfMJEYdp3ddMg4UVgQwDrA6BiAqVedelHc-NOMVbjheJq1vk7Y26UJaA8n5K1nY9z7qGLsP9T4",
  "__user": "0"
}

