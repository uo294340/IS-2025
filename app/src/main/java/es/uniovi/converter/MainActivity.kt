package es.uniovi.converter

import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.EditText
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.lifecycle.lifecycleScope
import kotlinx.coroutines.launch
import org.json.JSONObject
import java.io.BufferedReader
import java.io.InputStreamReader
import java.net.HttpURLConnection
import java.net.URL

class MainActivity : AppCompatActivity() {
    private var euroToDollar: Double = 1.16
    private lateinit var editTextEuros: EditText
    private lateinit var editTextDollars: EditText

    override fun onCreate(savedInstanceState: Bundle?) {
        //fetchExchangeRate()
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        editTextEuros = findViewById(R.id.editTextEuros)
        editTextDollars = findViewById(R.id.editTextDollars)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

    }
    private fun convert(source: EditText, destination: EditText, factor: Double) {
        val text = source.text.toString()
        val value = text.toDoubleOrNull()
        if (value == null) {
            destination.setText("")
            return
        }
        destination.setText((value * factor).toString())
    }

    fun onClickToDollars(view: View) {
        convert(editTextEuros, editTextDollars, euroToDollar)
        Toast.makeText(this, "Conversión a dólares realizada", Toast.LENGTH_SHORT).show()
    }

    // Se llama cuando el usuario pulsa el botón de dólares → euros
    fun onClickToEuros(view: View) {
        convert(editTextDollars, editTextEuros, 1 / euroToDollar)
        Toast.makeText(this, "Conversión a euros realizada", Toast.LENGTH_SHORT).show()
    }

    private fun fetchExchangeRate() {
        lifecycleScope.launch {
            try {
                val response = Models.RetrofitClient.api.convert("EUR", "USD", 1.0)
                val exchangeRateResponse = response.body()
                if (!response.isSuccessful || exchangeRateResponse == null) {
                    Log.e("MainActivity", "Error al obtener el cambio: ${response.code()}")
                    return@launch
                }
                euroToDollar = exchangeRateResponse.rates.USD
                Toast.makeText(
                    this@MainActivity,
                    "Cambio actualizado: $euroToDollar",
                    Toast.LENGTH_SHORT
                ).show()
                Log.d("MainActivity", "Cambio actualizado: $euroToDollar")
            } catch (e: Exception) {
                Log.e("MainActivity", "Excepción al obtener el cambio", e)
            }
        }
    }
}