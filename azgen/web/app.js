// create Vue app
var app = new Vue({
  // element to mount to
  el: '#app',
  data () {
    return {
      info: null
    }
  },
  methods: {
    calcAZ: function () {
      var lat = document.getElementById('lat').value;
      var long = document.getElementById('long').value;
      var alt = document.getElementById('alt').value;

      var data = {
        "summit_ref": "W6SC229",
        "summit_lat": lat,
        "summit_long": long,
        "summit_alt": alt,
        "deg_delta": 0.010,
        "sota_summit_alt_thres": 25
      }

      axios
        .post('http://localhost:8080', data)
        .then(response => (this.info = response.data.az))
    }
  }
})
