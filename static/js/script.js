$(document).ready(function(){
    var buscaBtn = $('#lupa')
    var limparBtn = $('#limpar')
    buscaBtn.css('cursor','pointer')
    limparBtn.css('cursor','pointer')
    var buscaForm = $('#busca-form')
    $(buscaBtn).on('click',function(){
            buscaForm.submit()
    })
    // Menu hamburger
    var hamburger = $('.hamburger')
    hamburger.hide()
    $('.menu-suspenso').hide()
    $('.ultimos-posts-suspenso').hide()
    // Abrir
    $('.hamburger-icon').on('click',function(){
        hamburger.fadeIn('slow')
        $('.menu-suspenso').fadeIn('slow')
        $('.ultimos-posts-suspenso').fadeIn('slow')
    })
    // Fechar
    $('.fechar').on('click',function(){
        hamburger.fadeOut('slow')
        $('.menu-suspenso').fadeOut('slow')
        $('.ultimos-posts-suspenso').fadeOut('slow')
    })

})
