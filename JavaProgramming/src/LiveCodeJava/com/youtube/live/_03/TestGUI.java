package com.youtube.live._03;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TestGUI {
    private JPanel jPanel;
    private JLabel jLabelTitle;
    private JTextField jTextFiledName;
    private JLabel jLabelName;
    private JButton jButtonShow;
    private JLabel jLabelShowName;

    public TestGUI() {
        jButtonShow.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = jTextFiledName.getText();
                jLabelShowName.setText("Your Name: "+ name);
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Test GUI");
        frame.setContentPane(new TestGUI().jPanel);
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setSize(500, 250);
        frame.setVisible(true);
    }
}
