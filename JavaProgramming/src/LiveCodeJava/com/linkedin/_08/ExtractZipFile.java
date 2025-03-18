package com.linkedin._08;

import java.io.*;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class ExtractZipFile {
    public static void main(String[] args) {
        String fileZip = "src\\com.linkedin\\_08\\AlgoKelvinFile.zip";
        String extractPath = "src\\com.linkedin\\_08";

        extractFileZip(fileZip, extractPath);

    }

    private static void extractFileZip(String fileZip, String extractPath) {
        try {
            ZipInputStream zipInputStream = new ZipInputStream(new FileInputStream(fileZip));
            ZipEntry zipEntry =  zipInputStream.getNextEntry();
            while (zipEntry != null) {
                String path = extractPath + File.separator + zipEntry.getName();
                if (!zipEntry.isDirectory()) {
                    BufferedOutputStream bufferedOutputStream = new BufferedOutputStream(new FileOutputStream(path));
                    byte[] bytes = new byte[4096];
                    int readByte = 0;
                    while ((readByte = zipInputStream.read(bytes)) != -1) {
                        bufferedOutputStream.write(bytes, 0, readByte);
                    }
                    bufferedOutputStream.close();
                } else {
                    File directory = new File(path);
                    directory.mkdirs();
                }
                zipInputStream.closeEntry();
                zipEntry = zipInputStream.getNextEntry();
            }
            zipInputStream.close();

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
