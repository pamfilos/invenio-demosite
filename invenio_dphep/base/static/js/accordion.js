// Accordion Javascript Module v1.0

(function (f) {
    var c = f(window);
    var d = f("body");
    var e = false;
    var j = (typeof matchMedia !== "undefined");
    if (j) {
        k();
        c.on("resize", function () {
            clearTimeout(this.resizeTimeout);
            this.resizeTimeout = setTimeout(k, 200)
        })
    } else {
        e = true;
        d.addClass("wide")
    }

    function k() {
        if (window.matchMedia("screen and (min-width: 761px)").matches) {
            e = true;
            d.addClass("wide")
        } else {
            e = false;
            d.removeClass("wide")
        }
        f(".panel-notmob, .panel-content, .panel-title").removeAttr("style");
        f(".panel-content a").blur();
    }
    var g = {
        expandHorz: function (l) {
            f(".panel-title").stop(true, true).fadeOut(200);
            l.stop().removeClass("compressed").addClass("expanded").animate({
                width: "64%"
            }, 700);
            f(".panel-content", l).stop(true, true).delay(400).fadeIn(400);
            l.siblings(".panel-notmob").stop().removeClass("expanded").addClass("compressed").animate({
                width: "12%"
            }, 700);
            l.siblings(".panel-notmob").find(".panel-content").stop(true, true).fadeOut(400, function () {
                f(this).delay(500).removeAttr("style")
            });
            // i("open", (f(".panel").index(l) + 1), l.attr("id"))
        },
        contractHorz: function () {
            f(".panel-notmob").stop().animate({
                width: "25%"
            }, 700, function () {
                f(".panel-title").fadeIn(250)
            }).removeClass("expanded compressed");
            f(".panel-content").stop(true, true).delay(200).fadeOut(500)
        },
        expandVert: function (l) {
            f(".panel-title").stop(true, true).fadeOut(200);
            l.stop().removeClass("compressed").addClass("expanded").animate({
                height: "22em"
            }, 700);
            l.siblings(".panel").stop().removeClass("expanded").addClass("compressed").animate({
                height: "3em"
            }, 700);
            f(".panel-content", l).stop(true, true).delay(400).fadeIn(400);
            l.siblings(".panel-notmob").find(".panel-content").stop(true, true).fadeOut(400, function () {
                f(this).delay(500).removeAttr("style")
            });
            	i("open", (f(".panel-notmob").index(l) + 1), l.attr("id"))
        },
        contractVert: function () {
            f(".panel-notmob").stop().animate({
                height: "5.5em"
            }, 700, function () {
                f(".panel-title").fadeIn(250)
            }).removeClass("expanded compressed");
            f(".panel-content").stop(true, true).fadeOut(500)
        },
    };
    var h = 200;
    var a;
    f(".accordion").on("mouseleave", function () {
        clearTimeout(a);
        h = 200
    });
    f(".panel-notmob").hover(function () {
        var l = f(this);
        clearTimeout(a);
        a = setTimeout(function () {
            if (e) {
                g.expandHorz(l)
            } else {
                // g.expandVert(l)
            }
            h = 0
        }, h)
    }, function () {
        if (e) {
            g.contractHorz(f(this))
        } else {
            // g.contractVert()
        }
    });
    f(".panel-notmob").on("click focus", function (l) {
        if (!f(this).hasClass("expanded")) {
            if (e) {
                g.expandHorz(f(this))
            } else {
                // g.expandVert(f(this))
            }
        }
    });
    f(".panel-notmob > a").on("blur", function () {
        if (e) {
            g.contractHorz()
        } else {
            // g.contractVert()
        }
    });
})(window.jQuery);