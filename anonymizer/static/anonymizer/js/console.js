var TestConsole = function(params){

    var that = this;
    var $target = params.$target;

    this.requestUrlPreffix = function() {
        return '/anonymizer/connection/' + params.consoleId + '/query/?q=';
    };

    this.history = {
        commands: [],
        position: -1,

        add: function(newCommand) {
            this.commands.push(newCommand);
            this.position = this.commands.length - 1;
        },

        getPrev: function() {
            if (this.position < 0) {
                return ''
            }

            var cmd = this.commands[this.position];
            this.position--;

            return cmd
        },

        getNext: function() {
            if (this.position >= this.commands.length - 1) {
                return ''
            }

            this.position++;
            return this.commands[this.position]
        }
    };

    this.status = 'DEFAULT';

    $target.on('keydown', function(e) {
        if (e.keyCode == 13) { //send request on enter
            //allow only one request at a time
            if (that.status == 'PENDING') {
                e.preventDefault();
                e.stopPropagation();

                return;
            }
            that.status = 'PENDING';

            var content = this.value;
            var q = content.substr(content.lastIndexOf("\n") + 2);

            that.history.add(q);

            $.ajax({
                type: "GET",
                url: that.requestUrlPreffix() + q,
                success: function(data, textStatus, jqXHR) {
                    var new_val = $target.val() + '\n' + jqXHR.responseText;
                    if (jqXHR.responseText) {
                        new_val += '\n$';
                    } else {
                        new_val += '$';
                    }

                    $target.val(new_val);
                    $target.scrollTop($target[0].scrollHeight);
                    that.status = 'DEFAULT';
                },
                error: function(jqXHR, textStatus) {
                    $target.val( $target.val() + '\n[ERROR]: ' + jqXHR.responseText + '\n$');
                    $target.scrollTop($target[0].scrollHeight);
                    that.status = 'DEFAULT';
                }
            });

            e.preventDefault();
            e.stopPropagation();
        }
        else if ([38, 40].indexOf(e.keyCode) >= 0) { // key up/down
            var command = '';
            if (e.keyCode === 38) {
                command = that.history.getPrev();
            } else {
                command = that.history.getNext();
            }

            if (command !== undefined) {
                var allLines = $target.val().split('\n');
                allLines.splice(-1,1);
                allLines.push('$' + command);
                var newContent = allLines.join('\n');
                $target.val(newContent);
                $target.scrollTop($target[0].scrollHeight);
            }

            e.preventDefault();
            e.stopPropagation();
        }
        else if (e.keyCode == 8) { //don't allow backspace before current line
            var content = $target.val();
            if (content[content.length - 1] === '$') {
                e.preventDefault();
                e.stopPropagation();
            }
        }
    });

    $target.on('cut', function () {
        return false;
    });

    return this;
};


