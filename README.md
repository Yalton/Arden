# Arden 
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <a href="https://github.com/Yalton/Arden">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">Arden - Raspberry Pi Voice Assistant</h3>
  <p align="center">
    A versatile voice assistant designed to run on a Raspberry Pi, offering a wide range of features and integrations.
    <br />
    <a href="https://github.com/Yalton/Arden"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Yalton/Arden">View Demo</a>
    ·
    <a href="https://github.com/Yalton/Arden/issues">Report Bug</a>
    ·
    <a href="https://github.com/Yalton/Arden/issues">Request Feature</a>
  </p>
</div>
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

Arden is a versatile voice assistant designed to run on a Raspberry Pi. It offers a wide range of features and integrations, making it a powerful tool for everyday use. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* [![Python][python-badge]][Python-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Clone the repository to your local system 

### Prerequisites

You will require some local system packages to make the script function properly 
* apt
  ```sh
  apt install portaudio19-dev espeak mpg123 libasound2-dev flac at
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/Yalton/Arden.git
   ```
3. Install NPM packages
   ```sh
   pip install -r requirements.txt
   ```
4. Enter your API keys in config.ini
   ```
   [API_KEYS]
    OpenWeatherMap = API_KEY
    OpenAI = API_KEY
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>
 -->


<!-- ROADMAP -->
## Roadmap

- [ ] Get news updates by integrating with a news API, such as NewsAPI, to fetch and read the latest headlines or news articles based on your interests or preferred sources.
- [ ] Connect to your calendar (e.g., Google Calendar) to read, create, or modify events.
- [ ] Integrate with a music or podcast service to play tracks based on your preferences or requests.
- [ ] Connect to an email service (e.g., Gmail) or messaging platform to send emails or messages on your behalf.
- [ ] Control smart home devices by integrating with their respective APIs, allowing you to control things like lights, thermostats, or door locks.
- [ ] Access currency conversion rates or stock market updates by integrating with a financial API.
- [ ] Translate text between languages using a translation API.


See the [open issues](https://github.com/Yalton/Arden/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Dalton Bailey - [@yalt7117](https://twitter.com/yalt7117) - drbailey117@gmail.com

Project Link: [https://github.com/Yalton/Arden](https://github.com/Yalton/Arden)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org
[contributors-shield]: https://img.shields.io/github/contributors/Yalton/Arden.svg?style=for-the-badge
[contributors-url]: https://github.com/Yalton/Arden/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Yalton/Arden.svg?style=for-the-badge
[forks-url]: https://github.com/Yalton/Arden/network/members
[stars-shield]: https://img.shields.io/github/stars/Yalton/Arden.svg?style=for-the-badge
[stars-url]: https://github.com/Yalton/Arden/stargazers
[issues-shield]: https://img.shields.io/github/issues/Yalton/Arden.svg?style=for-the-badge
[issues-url]: https://github.com/Yalton/Arden/issues
[license-shield]: https://img.shields.io/github/license/Yalton/Arden.svg?style=for-the-badge
[license-url]: https://github.com/Yalton/Arden/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/dalton-r-bailey
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
