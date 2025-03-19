package com.linkedin._07;

import java.io.FileOutputStream;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class CompressToZipFile {
    public static void main(String[] args) {
        String[] nameFile = {"CodingJava.txt", "LoveCoding.txt", "MyData.txt"};
        String[] writeFile = {
                "I Want to Learn Coding Java Programming",
                "I Love My Channel to Sharing Coding Java",
                "I 'm Kelvin - AlgoKelvin Channel"
        };
        compressToZip("AlgoKelvinFile.zip", nameFile, writeFile);
        compressToZip("AlgoKelvinFile2.zip", nameFile, writeFile);
    }
    private static void compressToZip(
            String fileZip,
            String[] nameFile,
            String[] writeFile
    ) {
        try {
            ZipOutputStream zipOutputStream = new ZipOutputStream(
                    new FileOutputStream(fileZip)
            );
            for (int i = 0; i < nameFile.length; i++) {
                zipOutputStream.putNextEntry(new ZipEntry(nameFile[i]));
                zipOutputStream.write(writeFile[i].getBytes());
                zipOutputStream.closeEntry();
            }
            zipOutputStream.close();
        } catch (Exception e) {
            System.out.println("Error Compress to Zip File");
        }
    }
}
