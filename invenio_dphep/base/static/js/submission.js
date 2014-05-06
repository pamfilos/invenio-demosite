var MaxInputs = 10;
var AddButton = $(".add-more");
var InputsWrapper = $(".add-more").parent();

var x = InputsWrapper.length+2;
var FieldCount=1;

$(".add-more").click(function(e){
    e.preventDefault();
    if(x <= MaxInputs){
        FieldCount++;
        $(InputsWrapper).append('<div><input type="text" placeholder="Insert Data Title" name="sub-analysis-title[]"><input type="text" placeholder="Upload Data or URL" name="sub-analysis-url[]"><input type="text" placeholder="Upload Data Documentation" name="sub-analysis-doc[]"><span class="remove-me glyphicon glyphicon-remove"></span></div>');
        x++;
    }
    return false;
});

$(".remove-me").on('click',function(e){
    e.preventDefault();
    $(this).css("background-color", "red");
    if (x > 1){
        
        $(this).parent('div').remove();
        x--;
    }
    return false;
});