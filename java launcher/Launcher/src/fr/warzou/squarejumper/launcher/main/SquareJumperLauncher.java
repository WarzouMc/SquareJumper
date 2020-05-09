package fr.warzou.squarejumper.launcher.main;

import java.io.IOException;

public class SquareJumperLauncher {

    public static void main(String[] args) {
        String command = "cmd /c start start.bat";
        try {
            Runtime.getRuntime().exec(command);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
