package tetris;

import javax.swing.JPanel;

import java.awt.Color;
import java.awt.Graphics;

public class GameArea extends JPanel {

    public GameArea() {
        this.setBounds(100, 50, 100, 100);
        this.setBackground(Color.red);
    }

    @Override
    protected void paintComponent(Graphics g) {

        super.paintComponent(g);

        g.fillRect(0, 0, 50, 50);
    }

}
