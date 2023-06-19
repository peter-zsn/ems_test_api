import jwt

AUTH0_CLIENT_ID='gqLsyr56AIXTAD96xVZpsC7iDr5sTr6Eshuainan'
AUTH0_CLIENT_SECRET='_VTDETXuGFMwG9fg6FiHh6-zB-eLfz2BhQ7NXzshuainan5A5BqhWknTjKK-vZ8_VoXC8Lqq'
AUTH0_DOMAIN='shuainan.au.auth0.com'
AUTH0_AUDIENCE='https://api.shuainan.com'

def verfy_jwt_token(token):
    try:
        jwks_client = jwt.PyJWKClient(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
        signing_key = jwks_client.get_signing_key_from_jwt(token).key
        kid= jwt.get_unverified_header(token)
        print(kid)
        return jwt.decode(
            token,
            signing_key,
            algorithms=["RS256"],
            audience=AUTH0_AUDIENCE,
            issuer=f"https://{AUTH0_DOMAIN}/",
            options={
                "verify_aud": True
            }
        )
    except:
        return False
    
if __name__ == '__main__':
    token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il8wc0pGUkt4ZnlsajZScm11bUlPaCJ9.eyJpc3MiOiJodHRwczovL3plcm9jYXAuYXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZDNkOTYzN2FjMzk4MDA2OTQ4NWEwZSIsImF1ZCI6WyJodHRwczovL2FwaS56ZXJvY2FwLmNvbSIsImh0dHBzOi8vemVyb2NhcC5hdS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjg3MTYxNTE1LCJleHAiOjE2ODcxNjUxMTUsImF6cCI6Ijd3S0F6cFVWRXBlRmFPM3kzb1ZGRGRaUktQMVVHalBpIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCJ9.MChMeegboDD4tkcYovRE40Qq-0JkBH-SZdlcKgTvOBwIgdcpBGU3uqqKToRbWUXaYu3CFFBZQyXZAuauFFkEP0Lsed7krxoLfp2smNT_kAMihp-LEWxudoXZsnma7tNnwbs1TCq2xvE50joDQ5_0IZv6mAczQ8o3z1dDQqYZir1KPzAQm9vkr05YK_jErNZytsQmQ6rjLGKcIW-c1VfQmGtWQnsVlSKKNNHhx3iPDsdSpwrvOO4kl9VS4e--Uo6EBKclv_YXjmiyvhRcnLjtVz9IYGeKW1ZxwjWiIhMZ3uT1GPnreuslYpauKguedORymeG6IBdrniTH316PiSOD-g'
    a = verfy_jwt_token(token)
    '''
    {'alg': 'RS256', 'typ': 'JWT', 'kid': '_0sJFRKxfylj6RrmumIOh'}
    {'iss': 'https://zerocap.au.auth0.com/', 'sub': 'auth0|60d3d9637ac3980069485a0e', 'aud': ['https://api.zerocap.com', 'https://zerocap.au.auth0.com/userinfo'], 
    'iat': 1687161515, 'exp': 1687165115, 'azp': '7wKAzpUVEpeFaO3y3oVFDdZRKP1UGjPi', 'scope': 'openid profile email'} 444444
    '''
    print(a, 444444)