package javacase.JwtToken;

import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;

import java.util.Base64;

public class JwtToken {
    public String generateToken(String jsonRequest, String clientKey){
        String jwtSecret = Base64.getEncoder().encodeToString(clientKey.getBytes());
        return Jwts.builder()
                .setHeaderParam("alg", "HS256")
                .setHeaderParam("typ", "JWT")
                .setPayload(jsonRequest)
                .signWith(SignatureAlgorithm.HS256, jwtSecret)
                .compact();
    }
}

