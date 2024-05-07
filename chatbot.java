import java.util.Scanner;

public class chatbot {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Hello! I'm your friendly chatbot. What's your name?");
        String name = scanner.nextLine();
        System.out.println("Nice to meet you, " + name + "! How can I assist you today?");

        String input;
        do {
            System.out.print("> ");
            input = scanner.nextLine().toLowerCase();

            String response = getResponse(input);
            System.out.println(response);
        } while (!input.equals("bye"));

        System.out.println("Goodbye, " + name + "! Have a great day.");
        scanner.close();
    }

    public static String getResponse(String input) {
        switch (input) {
            case "hi":
            case "hello":
                return "Hi there! How can I help you?";
            case "how are you":
                return "I'm just a chatbot, but thanks for asking!";
            case "bye":
                return "Goodbye!";
            default:
                return "I'm not sure how to respond to that. Can you ask me something else?";
        }
    }
}
