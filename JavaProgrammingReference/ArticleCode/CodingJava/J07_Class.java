
class Message {
    private String word;

    public Message(String word) {
        this.word = word; 
    }

    public String getWord() {
        return this.word;
    }

}

public class J07_Class {
    public static void main(String[] args) {
        Message message = new Message("Object Class Java");
        String word = message.getWord();
        System.out.println("Message = "+ word);
    }
}


