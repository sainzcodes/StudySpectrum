public class BankAccount {
  public static void main(String[] arg){

    double balance = 1000.75;
    double amountToWithdraw = 250;

    double updatedBalance = balance - amountToWithdraw;
    double amountForEachFriend = updatedBalance / 3;
    Boolean canPurchaseTicket = amountForEachFriend >= amountToWithdraw;
    System.out.println(canPurchaseTicket);
    System.out.println("I gave each friend " + amountForEachFriend + "...");

  }
}
