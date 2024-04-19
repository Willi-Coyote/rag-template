from dataclasses import dataclass
from typing import NamedTuple

import jwt
from fastapi import Depends
from starlette.requests import Request as StarletteRequest

from authentication.authentication_exceptions import BadCredentialsException, \
    RequiresAuthenticationException, UnableCredentialsException


@dataclass
class JsonWebToken:
    jwt_access_token: str
    issuer_url: str = f""
    audience: str = ""
    algorithm: str = "RS256"
    jwks_uri: str = f"{issuer_url}.well-known/jwks.json"

    def validate(self):
        try:
            jwks_client = jwt.PyJWKClient(self.jwks_uri)
            jwt_signing_key = jwks_client.get_signing_key_from_jwt(
                self.jwt_access_token
            ).key
            payload = jwt.decode(
                self.jwt_access_token,
                jwt_signing_key,
                algorithms=self.algorithm,
                audience=self.audience,
                issuer=self.issuer_url,
            )
        except jwt.exceptions.PyJWKClientError:
            raise UnableCredentialsException
        except jwt.exceptions.InvalidTokenError:
            raise BadCredentialsException
        return payload


class AuthorizationHeaderElements(NamedTuple):
    authorization_scheme: str
    bearer_token: str
    are_valid: bool


def get_bearer_token(request: StarletteRequest) -> str:
    authorization_header = request.headers.get("Authorization")
    if authorization_header:
        authorization_header_elements = get_authorization_header_elements(authorization_header)
        if authorization_header_elements.are_valid:
            return authorization_header_elements.bearer_token
        else:
            raise BadCredentialsException
    else:
        raise RequiresAuthenticationException


def get_authorization_header_elements(authorization_header: str, ) -> AuthorizationHeaderElements:
    try:
        authorization_scheme, bearer_token = authorization_header.split()
    except ValueError:
        raise BadCredentialsException
    else:
        valid = authorization_scheme.lower() == "bearer" and bool(bearer_token.strip())
        return AuthorizationHeaderElements(authorization_scheme, bearer_token, valid)


def validate_token(token: str = Depends(get_bearer_token)):
    return JsonWebToken(token).validate()
