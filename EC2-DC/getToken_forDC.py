from keycloak import KeycloakOpenID
import jwt

print('requesting the token for data consumer')
# client info
keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
                    client_id="fa-console",
                    realm_name="UAV-AC",
                    client_secret_key="0459cceb-bbc3-415c-92a9-0f557774b5bb",
                    verify=True)

# Get WellKnow
config_well_know = keycloak_openid.well_know()

# Get Token
token = keycloak_openid.token("u1", "u1u1u1")
#token = keycloak_openid.token("u2", "u2u2u2")
#token = keycloak_openid.token("u3", "u3u3u3")
#token = keycloak_openid.token("u4", "u4u4u4")
#token = keycloak_openid.token("u5", "u5u5u5")
#token = keycloak_openid.token("u6", "u6u6u6")


userinfo = keycloak_openid.userinfo(token['access_token'])

token_info = keycloak_openid.introspect(token['access_token'])

with open("KeycloakToken.txt", "w") as f4:
    f4.write(token['access_token'])
f4.close()
print('successfully received the token')

# Verify & Decode Token
KEYCLOAK_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n" + keycloak_openid.public_key() + "\n-----END PUBLIC KEY-----"
options = {"verify_signature": True, "verify_aud": True, "verify_exp": True}
decoded = jwt.decode(token['access_token'], KEYCLOAK_PUBLIC_KEY, audience='account', algorithms=['RS256'])

print('data consumer information = ', decoded)
