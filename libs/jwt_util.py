import jwt

AUTH0_CLIENT_ID='gqLsyr56AIXTAD96xVZpsC7iDr5sTr6E'
AUTH0_CLIENT_SECRET='_VTDETXuGFMwG9fg6FiHh6-zB-eLfz2BhQ7NXz5A5BqhWknTjKK-vZ8_VoXC8Lqq'
AUTH0_DOMAIN='dev-rz4pu53g5jc2vgj2.us.auth0.com'
AUTH0_AUDIENCE='https://dev-rz4pu53g5jc2vgj2.us.auth0.com/api/v2/'

def verfy_jwt_token(token):
    try:
        jwks_client = jwt.PyJWKClient(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
        signing_key = jwks_client.get_signing_key_from_jwt(token).key
        kid= jwt.get_unverified_header(token).get('kid', '')
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
    token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVvdnQ0RU9VVWlseWpZYml3eDhLNCJ9.eyJpc3MiOiJodHRwczovL2Rldi1yejRwdTUzZzVqYzJ2Z2oyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJncUxzeXI1NkFJWFRBRDk2eFZacHNDN2lEcjVzVHI2RUBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9kZXYtcno0cHU1M2c1amMydmdqMi51cy5hdXRoMC5jb20vYXBpL3YyLyIsImlhdCI6MTY4NjkyMzYyMiwiZXhwIjoxNjg3MDEwMDIyLCJhenAiOiJncUxzeXI1NkFJWFRBRDk2eFZacHNDN2lEcjVzVHI2RSIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.oC2Sr5jcPMMcYvLrDCtRCmkg38th9TQLHX9vaczCNmvgux388JcFRlPP5D813GA2Y3qjhrWLceoalLNBM7CM45s8VOyoHDPU6nNH_GqiZZpYtETuNDxVJxSjDN8DL2tISnAgutYlAbpJpORi7viI54qbgSb8EGc0V20ogbROXqy-R0--2wBQ8ANmIBTLLwJW4icnKpzHv2bwHT_FERLMWce5WDgPFeReF8sBN2MGueKkCFAh4O2EVum31xczPUbxZgSIiedo19n2f7Kt6C-aKERO9wEMD_RsRZ87ZKrU2toTQWuYOR9XYYpHHPmSrnowXLnMbWiYr2-Gpv1e-QjPYg'
    a = verfy_jwt_token(token)
    print(a, 444444)