package es.uniovi.amigos

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.launch

class MainViewModel : ViewModel() {
    private var amigosList: List<Model.Amigo>? = null // Por defecto es nula

    init {
        Log.d("MainViewModel", "MainViewModel created")
    }

    fun getAmigosList() {
        viewModelScope.launch {
            try {
                val response = Model.RetrofitClient.api.getAmigos()

                if (!response.isSuccessful) {
                    Log.e("MainViewModel", "Error en la respuesta: ${response.code()}")
                    return@launch
                }

                amigosList = response.body()

                // 3. Comprobar si la lista es nula
                if (amigosList == null) {
                    Log.e("MainViewModel", "La lista de amigos recibida es nula")
                    return@launch
                }

                 Log.d("MainViewModel", "Amigos: $amigosList")

            } catch (e: Exception) {
                Log.e("MainViewModel", "Excepción al obtener amigos: ${e.message}")
            }
        }
        }
    }
