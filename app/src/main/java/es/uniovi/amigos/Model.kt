package es.uniovi.amigos
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET


    data class Amigo(
        val name: String,
        val lati: Double,
        val longi: Double
        )
    interface AmigosApiService {
        @GET("/api/amigos")
        suspend fun getAmigos(): Response<List<Amigo>>
    }

    object RetrofitClient {

        private const val BASE_URL = "https://lamprophonic-bubblier-malinda.ngrok-free.dev/"

        val api: AmigosApiService by lazy {
            Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build()
                .create(AmigosApiService::class.java)
        }
    }
