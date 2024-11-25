package javacase.JwtToken;

import com.google.gson.Gson;
import org.json.JSONException;
import org.json.JSONObject;

public class JwtTokenMain {
    public static void main(String[] args) throws JSONException {
        JwtToken jwt = new JwtToken();

        JSONObject json = new JSONObject();
        json.put("app_code", "MCPDC");
        json.put("amount", 10000);
        json.put("partner_trx_id", "REQ0000001");
        json.put("terminal_code", "99999998");
        json.put("merchant_code", "TCA09101010");
        json.put("payment_method", "CARD");

        String token = jwt.generateToken(new Gson().toJson(json), "c31efe3217c0d5bccbcc28761ba441dc");
        System.out.println("Token: "+ token);

    }
}
