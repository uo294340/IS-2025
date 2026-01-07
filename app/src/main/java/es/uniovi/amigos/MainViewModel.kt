package es.uniovi.amigos

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import kotlinx.coroutines.launch

class MainViewModel : ViewModel() {
    private val _amigosList = MutableLiveData<List<Amigo>>()

    val amigosList: LiveData<List<Amigo>> = _amigosList

    init {
        Log.d("MainViewModel", "MainViewModel created")
    }

    fun getAmigosList() {
        viewModelScope.launch {
            try {
                val response = RetrofitClient.api.getAmigos()

                if (!response.isSuccessful) {
                    Log.e("MainViewModel", "Error en la respuesta: ${response.code()}")
                    return@launch
                }

                _amigosList.setValue(response.body())

                // 3. Comprobar si la lista es nula
                if (amigosList == null) {
                    Log.e("MainViewModel", "La lista de amigos recibida es nula")
                    return@launch
                }

                Log.d("MainViewModel", "Amigos: ${amigosList. value}")

            } catch (e: Exception) {
                Log.e("MainViewModel", "Excepción al obtener amigos: ${e.message}")
            }
        }
    }
}
