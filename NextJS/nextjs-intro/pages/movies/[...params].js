import Seo from "@/components/Seo/Seo";
import { useRouter } from "next/router";

export default function PaymentDetailsBase() {
  const router = useRouter();
  const [title, id] = router.query.params || [];
  return (
    <div>
      <Seo title={title} />
      <h4>{title}</h4>
    </div>
  );
}

export function getServerSideProps({ params: { params } }) {
  return {
    props: {
      params,
    },
  };
}
