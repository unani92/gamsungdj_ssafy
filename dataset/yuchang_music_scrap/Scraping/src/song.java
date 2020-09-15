import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class song {
	final static int N = 32914898;
	public static void main(String[] args) throws IOException {
		JSONArray jsonA = new JSONArray();
//		for (int n = 1; n <= N; n++) {
		for (int n = (32914898-100); n <= 32914898; n++) {
			JSONObject jsonO = new JSONObject();
			String URL = "https://www.melon.com/song/detail.htm?songId=" + n;
			Document doc = Jsoup.connect(URL).get();
			Elements temp = doc.select("body div");
			Iterator<Element> e_temp = temp.select("div").iterator();
			String isExist = e_temp.next().attr("id");

			// 곡정보가 없을 경우 pass
			if (isExist.equals("conts"))
				continue;

			// 곡정보가 있을 경우 크롤링
			Elements s1 = doc.select(".section_info");
			Elements s2 = doc.select(".section_lyric");
			Iterator<Element> e_title = s1.select(".song_name").iterator(); // 제목
			Iterator<Element> e_album = s1.select(".image_typeAll img").iterator(); // 앨범사진
			Iterator<Element> e_artist = s1.select(".artist a").iterator(); // 가수
			Iterator<Element> e_info = s1.select(".list dd").iterator(); // 앨범, 발매일, 장르
			Iterator<Element> e_like = s1.select(".button_etc.like.type02 .cnt").iterator(); // 좋아요 수
			Iterator<Element> e_lyric = s2.select("#lyricArea div").iterator(); // 가사

			ArrayList<String> list;
			String[] arr;
			String str;
			
			// 노래번호
			jsonO.put("id", n);
			
			// 노래이름
			str = e_title.next().text();
			str = str.substring(3);
			jsonO.put("title", str);
			
			// 가수
			list = new ArrayList<String>();
			while (e_artist.hasNext()) {
				list.add(e_artist.next().attr("title"));
			}
			jsonO.put("artist", list);
			
			// 앨범사진
			str = e_album.next().attr("src");
			jsonO.put("album_img", str);
			
			// 앨범명
			str = e_info.next().text();
			jsonO.put("album", str);
			
			// 발매일
			str = e_info.next().text();
			jsonO.put("date", str);
			
			// 장르
			arr = e_info.next().text().split(", ");
			list = new ArrayList<String>();
			for (int i = 0; i < arr.length; i++) {
				list.add(arr[i]);
			}
			jsonO.put("genre", list);
			
			// FLAC
			str = e_info.next().text();
			jsonO.put("flac", str);
			
			// 좋아요 수
			str = e_like.next().text();
			jsonO.put("like", str);
			
			// 가사
			str = e_lyric.next().text();
			if(str.substring(0, 8).equals("[가사 준비중]"))
				str = null;
			jsonO.put("lyrin", str);
			
			jsonA.add(jsonO);
		}

		// 파일로 저장
		FileWriter file = new FileWriter("C:\\Users\\multicampus\\Desktop\\song.json");
		file.write(jsonA.toJSONString());
		file.flush();
		file.close();
	}

}
