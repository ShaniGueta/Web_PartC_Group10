
// ------------------ schedule an appointment from today --------------//
if (document.querySelector('#dateAppointment') !== null){
   const today = new Date().toISOString().split('T')[0];
    document.querySelector('#dateAppointment').min = today;
}
