const siteTemplate = document.querySelector("[sites-template]")

url="https://github.com/JoelBondy/Suruthua/blob/main/metakram/content.txt"
fetch(url)
.then(res => res.json())
.then(data => {
    const site = siteTemplate.content.cloneNode(true)
    console.log(site)
})


