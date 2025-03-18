package com.youtube.live._03;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class InputNameGUI {
    private JPanel jPanel;
    private JLabel jLabelTitle;
    private JTextField jTextFieldName;
    private JLabel jLabelName;
    private JButton jButtonShow;
    private JLabel jLabelShowName;

    public InputNameGUI() {
        jButtonShow.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = jTextFieldName.getText();
                jLabelShowName.setText("Your Name: "+ name);
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Input Name GUI");
        frame.setContentPane(new InputNameGUI().jPanel);
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setSize(500, 250);
        frame.setVisible(true);
    }
}
