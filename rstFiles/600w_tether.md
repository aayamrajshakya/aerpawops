## 600W 24V Power Tether

This page is a proposed system design for a low-medium power tether for use on the SAM4 and
aerostat system. For the SAM4 it should provide enough average power to provide indefinite
flight time. On the aerostat it will provide more than enough power for the current portable node
for an indefinite amount of time.

The system is intended to provide power to a tethered aerial system from a standard 120V AC
wall outlet or generator. The system is based around the Vicor cooperation DC-DC converter
modules.

## Major components

### Air side DC-DC converter

[Vicor Corporation V375A24C600B Isolated Module DC DC Converter 1 Output 24V - - 25A
250V - 425V Input](https://www.digikey.com/en/products/detail/vicor-corporation/V375A24C600B/3002300)


<table>
  <tr>
    <td>
      <img src="https://mm.digikey.com/Volume0/opasdata/d220001/derivates/6/300/461/584/MFG_MaxiDCDCseries_web%28640x640%29.jpg?hidebanner=true" width="250"/>
    </td>
    <td>
      <b>General Specs:</b>
      <ul>
        <li>24V regulated output</li>
        <li>250V–425V input</li>
        <li>25A max output current</li>
        <li>600W total power output</li>
        <li>Isolated</li>
        <li>~$550 each</li>
      </ul>
    </td>
  </tr>
</table>

### Tether cable

Custom built cable using PTFE wire and braided jacket.

- [2 x 20 AWG PTFE jacketed cable rated at 600V, 4.5A](https://www.wireandcableyourway.com/belden-83007-20-awg-teflon-hook-up-wire-mil-w-16878-4-type-e)
- [1/8” Expandable cable sleeving](https://www.digikey.com/en/products/detail/techflex/PTP0-25BK1000/14564060)
- [Installation pipe tool](https://www.amazon.com/Stainless-Steel-Tubing-Tube-Fittings/dp/B06Y3MN9DH)

<table>
  <tr>
    <td>
      <img src="https://s.alicdn.com/@sc04/kf/H01a2422ecf3d4aa0b0beb7944bf1c4d63.jpg" width="250"/>
    </td>
    <td>
      <b>General Specs:</b>
      <ul>
        <li>500ft tether estimate cost: $1100.</li>
      </ul>
    </td>
  </tr>
</table>


### Ground DC-DC converter


[CSP-3000-400 - MEAN WELL - TRC Electronics](https://trcelectronics.com/products/mean-well-csp-3000-400?utm_campaign=Shopping%20Display&utm_medium=ppc&utm_source=adwords&utm_term=)

<table>
  <tr>
    <td>
      <img src="https://trcelectronics.com/cdn/shop/files/csp3000_f857f953-9792-4274-b776-ba1aa63f7a0f_437x437.jpg?v=1702005218" width="250"/>
    </td>
    <td>
      <b>General Specs:</b>
      <ul>
        <li>AC-DC 400V, 3000W power supply.</li>
        <li>220V input (120V options are not available).</li>
      </ul>
    </td>
  </tr>
</table>
