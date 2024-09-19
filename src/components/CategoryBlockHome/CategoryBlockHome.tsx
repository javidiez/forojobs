import styles from "./categoryBlockHome.module.css"

interface CategoryBlockHomeProps {
    title: string;
    category: string;
    subCategories: string
}

export const CategoryBlockHome = (props: CategoryBlockHomeProps) => {

    return (
        <table className={`table table-borderles ${styles.table}`}>
            <thead>
                <tr>
                    <th colSpan={4} className={`${styles.bg_blue} text-light`}>
                    <h2>{props.title}</h2>
                    </th>

                </tr>
            </thead>
            <tbody>
                <tr>
                    <th className="fs-5" colSpan={4}>Ofertas de trabajo</th>
                </tr>
                <tr>
                <th className="fs-5" colSpan={4}>Ofertas de trabajo</th>
                </tr>
                <tr>
                <th className="fs-5" colSpan={4}>Ofertas de trabajo</th>
                </tr>
            </tbody>
        </table>
    )
}