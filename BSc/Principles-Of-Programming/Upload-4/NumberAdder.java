import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class NumberAdder {

    private String filename = " ";
	private int totalAmount;
    public void readNumbers() {
        File file = new File(filename);
        Scanner fileScan = null;
        this.totalAmount = 0;
       
        
        try {
            fileScan = new Scanner(file);
            while (fileScan.hasNext()) {
                int nextNumber = fileScan.nextInt();
                boolean isNumber = validateNumber(nextNumber);
                writeNumber(nextNumber, isNumber);
            }
        }

        catch (FileNotFoundException ex) {
            System.err.println("No such file. Try again"); 
        }

        finally {
            if (fileScan !=null) {
                fileScan.close();
            }
        }
    }
    
    public void writeNumber(int nextNumber, boolean isNumber) {
        System.out.println(nextNumber);
        this.totalAmount += nextNumber;
    }
    
    
    public void showTotal() {
    	System.out.println("Total is: " + this.totalAmount);
    }
    
    public boolean validateNumber(int nextNumber) {
        boolean validNumber = true;
		return validNumber;    
    }

    public void getFileName() {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter Filename: ");
        filename = scan.next();
        scan.close();
    }    
    
    public static void main(String[] args) {
        NumberAdder na = new NumberAdder();
        na.getFileName();
        na.readNumbers();
        na.showTotal();
        
    }    
}
