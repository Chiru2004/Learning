import 'dart:convert';
import 'package:http/http.dart' as http;

Future<Map<String, dynamic>> mapResponse(String endpoint) async {

  var headers = {
    'x-rapidapi-key': 'XxXxXxXxXxXxXxXxXxXxXxXx',
    'x-rapidapi-host': 'v1.formula-1.api-sports.io'
  };
  var request = http.Request(
      'GET', Uri.parse('https://v1.formula-1.api-sports.io/$endpoint'));

  request.headers.addAll(headers);

  http.StreamedResponse response = await request.send();
  // Decode the response body as JSON.
  final json = await jsonDecode(await response.stream.bytesToString());
  // Return the decoded JSON as a Map.
  return json as Map<String, dynamic>;
}
