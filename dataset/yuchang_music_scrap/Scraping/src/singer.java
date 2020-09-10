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

public class singer {
	final static int N = 32914898;
	public static void main(String[] args) throws IOException {
		JSONArray jsonA = new JSONArray();
//		for (int n = 1; n <= N; n++) {
		for (int n = (2879819); n <= 2879819; n++) {
			JSONObject jsonO = new JSONObject();
			String URL = "https://www.melon.com/artist/timeline.htm?artistId=" + n;
			Document doc = Jsoup.connect(URL).get();
			Elements temp = doc.select("body div");
			Iterator<Element> e_temp = temp.select("div").iterator();
			String isExist = e_temp.next().attr("id");

			// 가수정보가 없을 경우 pass
			if (isExist.equals("conts"))
				continue;

			// 가수정보가 있을 경우 크롤링
			Elements s1 = doc.select(".wrap_dtl_atist");
			Iterator<Element> e_title = s1.select(".title_atist").iterator(); // 제목
			Iterator<Element> e_album = s1.select("#artistImgArea a").iterator(); // 앨범사진
			Iterator<Element> e_artist = s1.select(".wrap_atistname a").iterator(); // 멤버
			Iterator<Element> e_info = s1.select(".list dd").iterator(); // 앨범, 발매일, 장르
			Iterator<Element> e_like = s1.select(".button_etc.like.type02 .cnt").iterator(); // 좋아요 수

			ArrayList<String> list;
			String[] arr;
			String str;
			
			// 가수번호
			jsonO.put("id", n);
			
			// 노래이름
			str = e_title.next().text();
			str = str.substring(5);
			jsonO.put("title", str);
			
			// 멤버명
			list = new ArrayList<String>();
			while (e_artist.hasNext()) {
				list.add(e_artist.next().attr("title"));
			}
			jsonO.put("artist", list);
			
			// 앨범사진
			str = e_album.next().attr("src");
			jsonO.put("artist_img", str);
			
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
			
			jsonA.add(jsonO);
		}

		// 파일로 저장
		FileWriter file = new FileWriter("C:\\Users\\multicampus\\Desktop\\tes.json");
		file.write(jsonA.toJSONString());
		file.flush();
		file.close();
	}

}
