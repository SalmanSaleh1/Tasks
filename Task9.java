import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class BasicApiTest {

    @Test
    public void testGetRequest() {
        // Set Base URI
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";

        // Perform GET request
        Response response = given()
                .when()
                .get("/posts/1")
                .then()
                .statusCode(200) // Validate status code
                .body("id", equalTo(1)) // Validate response body
                .extract()
                .response();

        // Additional validation using JUnit assertions
        assertEquals(200, response.getStatusCode(), "Expected status code is not returned");
    }
}
