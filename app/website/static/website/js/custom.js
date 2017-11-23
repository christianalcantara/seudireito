/* Add here all your JS customizations */
$('#selectLanguage').on('changed.bs.select', function (e) {
  var ln = $("#selectLanguage").val();
  console.log('// do something...', ln);
  $('input[name=language]').val(ln);
  $('#formSetLanguage').submit()
});