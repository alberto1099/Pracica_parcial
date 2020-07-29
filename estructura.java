import javax.sound.sampled.SourceDataLine;

public class estructura {
    public static void main(String[] args) {

        int notas[] = new int[5];
        notas[0] = 5;
        notas[1] = 3;
        notas[2] = 4;
        notas[3] = 4;
        notas[4] = 2;
        double prom = 0;
        int cont = 0;

        for (int i = 0; i < notas.length; i++) {
            prom += notas[i];

        }

        double pro = prom / (notas.length);
        System.out.println("el promedio es " + pro);

    }

}