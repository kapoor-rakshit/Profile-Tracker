package rkapoors.profiletracker;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.CheckedTextView;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import java.util.HashSet;
import java.util.Set;

public class MainActivity extends Activity {

    ListView ls;
    ArrayAdapter<String>ad;
    AutoCompleteTextView et;
    private String temp="";
    private String flink="";

    public static final String USERNAME="username";
    public static final String SEARCHHISTORY="searchhistory";
    private SharedPreferences settings;
    private Set<String> history;

    String[] a = {"Codechef","HackerEarth","HackerRank","SPOJ","CodeForces","CodeFights","-/-/--/--/--/-/-","GitHub","LinkedIn","-/-/--/--/--/-/-","NITJ","CBSE"};
    String links[]={"https://www.codechef.com/users/","https://www.hackerearth.com/users/","https://www.hackerrank.com/","http://www.spoj.com/users/","http://codeforces.com/profile/","https://codefights.com/profile/","","https://github.com/","https://in.linkedin.com/in/","","http://nitj.ac.in/","http://cbse.nic.in/"};
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ls=(ListView)findViewById(R.id.list);
        et=(AutoCompleteTextView) findViewById(R.id.et1);
        settings=getSharedPreferences(USERNAME,0);
        history = new HashSet<String>(settings.getStringSet(SEARCHHISTORY, new HashSet<String>()));
        setautocompletesource();

        et.setOnKeyListener(new View.OnKeyListener() {
            @Override
            public boolean onKey(View v, int keyCode, KeyEvent event) {
                if((event.getAction()==KeyEvent.ACTION_DOWN)&&(keyCode==KeyEvent.KEYCODE_ENTER))
                {
                    addsearchinput(et.getText().toString());
                    return true;
                }
                return false;
            }
        });

        ad=new ArrayAdapter<>(this,android.R.layout.simple_list_item_single_choice,a);
        ls.setAdapter(ad);

      ls.setOnItemClickListener(new AdapterView.OnItemClickListener() {
          @Override
          public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
              flink="";
              temp=et.getText().toString();
              flink+=links[position];
              flink+=temp;
              history.add(et.getText().toString());
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
                  Toast.makeText(MainActivity.this,"Nothing to display here !!",Toast.LENGTH_SHORT).show();
              }
          }
      });
    }
    private void setautocompletesource()
    {
        ArrayAdapter<String> adapter=new ArrayAdapter<>(this,android.R.layout.simple_list_item_1,history.toArray(new String[history.size()]));
        et.setAdapter(adapter);
    }
    private void addsearchinput(String input)
    {
        if(!history.contains(input))
        {
            history.add(input);
            setautocompletesource();
        }
    }
   private void saveprefs()
    {
        settings=getSharedPreferences(USERNAME,0);
        SharedPreferences.Editor editor=settings.edit();
        editor.putStringSet(SEARCHHISTORY,history);
        editor.apply();
    }
   @Override
    protected void onStop()
    {
        super.onStop();
        saveprefs();
    }
}
