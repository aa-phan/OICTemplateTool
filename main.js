$(document).ready(function() {
    function copyToClipboard(text) {
        if (navigator.clipboard && navigator.clipboard.writeText) { // Check for Clipboard API support
            navigator.clipboard.writeText(text).then(function() {
                console.log('Text successfully copied to clipboard');
                //alert('Message copied to clipboard!'); // Provide feedback to the user
            }).catch(function(err) {
                console.error('Failed to copy text to clipboard', err);
                //alert('Failed to copy message to clipboard.'); // Inform user of failure
            });
        } else {
            // Fallback for older browsers (less reliable, but better than nothing)
            console.warn('Clipboard API not available, falling back to execCommand'); // Notify developers about the fallback
            var tempTextArea = document.createElement("textarea"); // Create a temporary textarea element
            tempTextArea.value = text;
            document.body.appendChild(tempTextArea); // Append the textarea to the document body
            tempTextArea.select(); // Select the text in the textarea
            document.execCommand("copy"); // Execute the copy command
            document.body.removeChild(tempTextArea); // Remove the temporary textarea
            //alert('Message copied to clipboard (using fallback)!');
        }
    }
    

    $('#trigNIDsub').on('click',function() {
        $.ajax({
            url: '/trigger_NID',
            type: 'POST',
            success: function(response) {
                $('#messageArea').text(response.message);
                copyToClipboard(response.message);                        
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('#WIA_Button').on('click', function() {
        $.ajax({
            url: '/trigger_wia_message',
            type: 'POST',
            success: function(response) {
                $('#messageArea').text(response.message);
                copyToClipboard(response.message);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('#trigDRsub').on('click',function() {
        var $form = $(this).closest('form');
        $.ajax({
            url: '/trigger_DR',
            type: 'POST',
            data: $form.serialize(),
            success: function(response) {
                $('#messageArea').text(response.message);
                copyToClipboard(response.message);
                $form[0].reset();
                
            },
            error: function(error) {
                console.log(error);
            }
        });
        return false;
    });
    $('#trigDCsub').on('click',function() {
        var $form = $(this).closest('form');
        $.ajax({
            url: '/trigger_DC',
            type: 'POST',
            data: $form.serialize(),
            success: function(response) {
                $('#messageArea').text(response.message);
                copyToClipboard(response.message);
                $form[0].reset();
                
            },
            error: function(error) {
                console.log(error);
            }
        });
        return false;
    });
    $('#trigATTsub').on('click',function() {
        var $form = $(this).closest('form');
        $.ajax({
            url: '/trigger_ATT',
            type: 'POST',
            data: $form.serialize(),
            success: function(response) {
                $('#messageArea').text(response.message);
                copyToClipboard(response.message);
                $form[0].reset();
                
            },
            error: function(error) {
                console.log(error);
            }
        });
        return false;
    });
    $('#CPW_Button').on('click', function() {
        $.ajax({
            url: '/trigger_CPW',
            type: 'POST',
            success: function(response) {
                $('#messageArea').text(response.message);
                copyToClipboard(response.message);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('#PI_Button').on('click', function() {
        $.ajax({
            url: '/trigger_PI',
            type: 'POST',
            success: function(response) {
                $('#messageArea').text(response.message);
                copyToClipboard(response.message);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('#FI_Button').on('click', function() {
        $.ajax({
            url: '/trigger_FI',
            type: 'POST',
            success: function(response) {
                $('#messageArea').text(response.message);
                copyToClipboard(response.message);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('#SS_Button').on('click', function() {
        $.ajax({
            url: '/trigger_SS',
            type: 'POST',
            success: function(response) {
                $('#messageArea').text(response.message);
                copyToClipboard(response.message);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('#SQ_Button').on('click', function() {
        $.ajax({
            url: '/trigger_SQ',
            type: 'POST',
            success: function(response) {
                $('#messageArea').text(response.message);
                copyToClipboard(response.message);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('#Install_Fail').on('click', function() {
        $.ajax({
            url: '/trigger_IF',
            type: 'POST',
            success: function(response) {
                $('#messageArea').text(response.message);
                copyToClipboard(response.message);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('#Labels_Script').on('click',function() {
        var $form = $(this).closest('form');
        $.ajax({
            url: '/trigger_labels',
            type: 'POST',
            data: $form.serialize(),
            dataType: "json",
            success: function(response) {
                
                //console.log(response.email_template);
                $('#emailButton').data('emailTemplateValue', response.email_template);
                $('#firstButton').data('firstValue', response.first_step);
                $('#secondButton').data('secondValue', response.second_step);
                $('#thirdButton').data('thirdValue', response.third_step);
                $('#fourthButton').data('fourthValue', response.fourth_step);
                $('#fifthButton').data('fifthValue', response.fifth_step);



                $('#messageArea').text("all steps received");
                // copyToClipboard(response.message);
                $form[0].reset();
                
            },
            error: function(error) {
                console.log(error);
            }
        });
        return false;
    });
    $('#emailButton').on('click', function() {
        // Retrieve the stored value using .data()
        var storedEmailTemplate = $(this).data('emailTemplateValue');

        if (storedEmailTemplate) {
            // Do something with the stored value, e.g., display it in a modal, a textarea, etc.
            $('#messageArea').text('Email Template Copied');
            copyToClipboard(storedEmailTemplate);
        } else {
            $('#messageArea').text('No email template data found.');
        }
    });
    $('#firstButton').on('click', function() {
        // Retrieve the stored value using .data()
        var storedFirst = $(this).data('firstValue');

        if (storedFirst) {
            // Do something with the stored value, e.g., display it in a modal, a textarea, etc.
            $('#messageArea').text('First Step Copied');
            copyToClipboard(storedFirst);
        } else {
            $('#messageArea').text('No data found.');
        }
    });
    $('#secondButton').on('click', function() {
        // Retrieve the stored value using .data()
        var storedSecond = $(this).data('secondValue');

        if (storedSecond) {
            // Do something with the stored value, e.g., display it in a modal, a textarea, etc.
            $('#messageArea').text('Second Step Copied');
            copyToClipboard(storedSecond);
        } else {
            $('#messageArea').text('No data found.');
        }
    });
    $('#thirdButton').on('click', function() {
        // Retrieve the stored value using .data()
        var storedThird = $(this).data('thirdValue');

        if (storedThird) {
            // Do something with the stored value, e.g., display it in a modal, a textarea, etc.
            $('#messageArea').text('Third Step Copied');
            copyToClipboard(storedThird);
        } else {
            $('#messageArea').text('No data found.');
        }
    });
    $('#fourthButton').on('click', function() {
        // Retrieve the stored value using .data()
        var storedFourth = $(this).data('fourthValue');

        if (storedFourth) {
            // Do something with the stored value, e.g., display it in a modal, a textarea, etc.
            $('#messageArea').text('Fourth Step Copied');
            copyToClipboard(storedFourth);
        } else {
            $('#messageArea').text('No data found.');
        }
    });
    $('#fifthButton').on('click', function() {
        // Retrieve the stored value using .data()
        var storedFifth = $(this).data('fifthValue');

        if (storedFifth) {
            // Do something with the stored value, e.g., display it in a modal, a textarea, etc.
            $('#messageArea').text('Fifth Step Copied');
            copyToClipboard(storedFifth);
        } else {
            $('#messageArea').text('No data found.');
        }
    });
    $('#CER_Scrub').on('click',function() {
        var $form = $(this).closest('form');
        $.ajax({
            url: '/trigger_CER',
            type: 'POST',
            data: $form.serialize(),
            success: function(response) {

                $('#messageArea').text("CER Scrub Copied");
                copyToClipboard(response.message);
                $form[0].reset();
                
            },
            error: function(error) {
                console.log(error);
            }
        });
        return false;
    });
    $('#CES_Scrub').on('click',function() {
        var $form = $(this).closest('form');
        $.ajax({
            url: '/trigger_CES',
            type: 'POST',
            data: $form.serialize(),
            success: function(response) {

                $('#messageArea').text("CES Scrub Copied");
                copyToClipboard(response.message);
                $form[0].reset();
                
            },
            error: function(error) {
                console.log(error);
            }
        });
        return false;
    });
    $('#NID_RAD_Scrub').on('click',function() {
        var $form = $(this).closest('form');
        $.ajax({
            url: '/trigger_NID_RAD',
            type: 'POST',
            data: $form.serialize(),
            success: function(response) {

                $('#messageArea').text("NID (RAD) Scrub Copied");
                copyToClipboard(response.message);
                $form[0].reset();
                
            },
            error: function(error) {
                console.log(error);
            }
        });
        return false;
    });
    $(window).on('beforeunload', function(){
        fetch('/shutdown', {
            method: 'GET',
            keepalive: true
        }).catch(e=>console.error("Error sending shutdown request:", e))
    });
});
