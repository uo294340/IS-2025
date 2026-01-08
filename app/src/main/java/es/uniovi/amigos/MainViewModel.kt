package es.uniovi.amigos

import android.app.Application
import android.util.Log
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import kotlinx.coroutines.launch
import kotlinx.coroutines.delay


class MainViewModel(application: Application) : AndroidViewModel(application) {
    private val _amigosList = MutableLiveData<List<Amigo>>()
    private val locationFlow = application.createLocationFlow()
    val amigosList: LiveData<List<Amigo>> = _amigosList

    init {
        Log.d("MainViewModel", "MainViewModel created")
        startPolling() // Empezamos el polling
        startLocationUpdates()
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
    private fun startPolling() {
        viewModelScope.launch {
            while (true) {
                Log.d("Polling", "Timer disparado, pidiendo amigos...")
                getAmigosList()
                delay(5000)
            }
        }
    }
    fun startLocationUpdates() {
        // Lanzamos una corutina para consumir asíncronamente del Flow
        viewModelScope. launch {
            locationFlow.collect { result ->
                // Este bloque se llamará cada vez que el Flow emita un valor
                if (result is LocationResult.NewLocation) {
                    val location = result.location
                    Log. d("GPS", "Nueva ubicación:  ${location.latitude}, ${location. longitude}")
                } else if (result is LocationResult.ProviderDisabled) {
                    Log. w("GPS", "El proveedor de GPS está desactivado.")
                } else if (result is LocationResult.PermissionDenied) {
                    Log.e("GPS", "Permiso de ubicación denegado.")
                    // Esto no debería pasar si la Activity lo hizo bien
                }
            }
        }
    }
}
