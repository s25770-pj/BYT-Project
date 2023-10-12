export const convertNumber = (number) => {
    if(number<999) return number;
    const suffixes = ['', 'k', 'm', 'b', 't'];
    const suffixNum = Math.floor(('' + number).length / 3);
    const shortValue = parseFloat((suffixNum !== 0 ? (number / Math.pow(1000, suffixNum)) : number).toPrecision(2));
    return shortValue + suffixes[suffixNum];
};