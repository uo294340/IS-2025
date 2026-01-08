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
    private var userName: String? = null
    var userId: Int? = null

    fun setUserName(name: String) {
        userName = name
        Log. d("MainViewModel", "Nombre de usuario establecido: $userName")
        viewModelScope.launch {
            try {
                val response = RetrofitClient.api.getAmigoByName(name)

                if (response.isSuccessful) {
                    val amigo = response.body()
                    if (amigo != null) {
                        userId = amigo. id
                        Log.d("MainViewModel", "ID de usuario obtenido: $userId")
                    } else {
                        Log.e("MainViewModel", "El cuerpo de la respuesta es nulo")
                    }
                } else {
                    Log.e("MainViewModel", "Error al obtener usuario: ${response.code()}")
                }
            } catch (e: Exception) {
                Log.e("MainViewModel", "Excepción al obtener usuario: ${e.message}")
            }
        }
    }

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
                    try {
                        val payload = LocationPayload(
                            lati = location.latitude,
                            longi = location.longitude
                        )
                        val response = RetrofitClient.api.updateAmigoPosition(2, payload)

                        if (response.isSuccessful) {
                            Log. d("GPS", "Ubicación actualizada en el servidor correctamente")
                        } else {
                            Log.e("GPS", "Error al actualizar ubicación: ${response.code()}")
                        }
                    } catch (e: Exception) {
                        Log.e("GPS", "Excepción al actualizar ubicación: ${e.message}")
                    }
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
