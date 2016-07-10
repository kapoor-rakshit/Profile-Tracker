package rkapoors.profiletracker;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.CheckedTextView;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

public class MainActivity extends Activity {

    ListView ls;
    ArrayAdapter<String>ad;
    EditText et;
    private String temp="";
    private String flink="";
    String[] a = {"Codechef","HackerEarth","HackerRank","SPOJ","CodeForces","CodeFights","-/-/--/--/--/-/-","GitHub","LinkedIn","-/-/--/--/--/-/-","NITJ","CBSE"};
    String links[]={"https://www.codechef.com/users/","https://www.hackerearth.com/users/","https://www.hackerrank.com/","http://www.spoj.com/users/","http://codeforces.com/profile/","https://codefights.com/profile/","","https://github.com/","https://in.linkedin.com/in/","","http://nitj.ac.in/","http://cbse.nic.in/"};
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ls=(ListView)findViewById(R.id.list);
        et=(EditText)findViewById(R.id.et1);
        ad=new ArrayAdapter<>(this,android.R.layout.simple_list_item_single_choice,a);
        ls.setAdapter(ad);

      //  Toast.makeText(MainActivity.this,"Attention!!\nMake sure you have entered the correct username",Toast.LENGTH_SHORT).show();

      ls.setOnItemClickListener(new AdapterView.OnItemClickListener() {
          @Override
          public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
              flink="";
              temp=et.getText().toString();
              flink+=links[position];
              flink+=temp;
              if(position==10 || position==11)
              {
                  flink=links[position];
              }

              if(position!=6&&position!=9){
              Intent intent = new Intent(Intent.ACTION_VIEW,Uri.parse(flink));
              startActivity(intent);
          }
              else
              {
                  Toast.makeText(MainActivity.this,"Nothing to display here :)",Toast.LENGTH_SHORT).show();
              }
          }
      });



    }
}
