package javacase.SecurityCaseStudy;


//import com.google.gson.Gson;
//import org.json.JSONObject;

import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

public class ByteEncryptJson {
    public static void main(String[] args) {

        // Create Map Data
        Map<Object, Object> mapData = new HashMap<>();
        mapData.put("cardNumber", "1234567893");
        mapData.put("pin", "012345");

        // Create Json
//        JSONObject json = new JSONObject(mapData);
//        System.out.println(json);

    }

}
