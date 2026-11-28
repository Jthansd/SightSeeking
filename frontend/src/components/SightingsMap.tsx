import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";
import { icon } from "leaflet";
import "leaflet/dist/leaflet.css";
import markerIconUrl from "leaflet/dist/images/marker-icon.png";
import markerIcon2xUrl from "leaflet/dist/images/marker-icon-2x.png";
import markerShadowUrl from "leaflet/dist/images/marker-shadow.png";
import { SIGHTING_TYPE_LABELS, type SightingApiResponse } from "../types";


const SAN_DIEGO_CENTER: [number, number] = [32.85, -116.9];
const markerIcon = icon({
  iconUrl: markerIconUrl,
  iconRetinaUrl: markerIcon2xUrl,
  shadowUrl: markerShadowUrl,
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

type Props = {
  sightings: SightingApiResponse[];
};

export default function SightingsMap({ sightings }: Props) {
  const mappable = sightings.filter(
    (s) =>
      Number.isFinite(s.locationLatitude) &&
      Number.isFinite(s.locationLongitude) &&
      Math.abs(s.locationLatitude) <= 90 &&
      Math.abs(s.locationLongitude) <= 180
  );
  return (
    <MapContainer
      center={SAN_DIEGO_CENTER}
      zoom={9}
      scrollWheelZoom={false}
      className="sightings-map"
    >
      <TileLayer
        url="https://tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
        {mappable.map((s) => (
        <Marker
        key={s.id}
        position={[s.locationLatitude, s.locationLongitude]}
        icon={markerIcon}
      >
        <Popup>
          <div className="map-popup">
            <strong>
              {s.common_name || SIGHTING_TYPE_LABELS[s.sighting_type]}
            </strong>
            <span>
              {new Date(s.observed_at || s.timestamp).toLocaleString()}
            </span>
            {s.sighting_type === "ANIMAL" && s.animal_count != null && (
              <span>{s.animal_count} spotted</span>
            )}
            {(s.notes || s.description) && <p>{s.notes || s.description}</p>}
          </div>
        </Popup>
      </Marker>
      ))}
    </MapContainer>
  );
}