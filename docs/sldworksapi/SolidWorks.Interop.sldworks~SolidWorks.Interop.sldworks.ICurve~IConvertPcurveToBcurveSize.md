# IConvertPcurveToBcurveSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize`

Creates a b-curve from piecewise data.
Creates a b-curve from piecewise data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IConvertPcurveToBcurveSize( _
   ByVal Dim As System.Integer, _
   ByVal Order As System.Integer, _
   ByVal Nsegs As System.Integer, _
   ByRef Coeffs As System.Double, _
   ByVal Basis As System.Integer, _
   ByRef Xform As System.Double, _
   ByVal ScaleFactor As System.Double _
) As System.Integer
```

```

Dim instance As ICurve
Dim Dim As System.Integer
Dim Order As System.Integer
Dim Nsegs As System.Integer
Dim Coeffs As System.Double
Dim Basis As System.Integer
Dim Xform As System.Double
Dim ScaleFactor As System.Double
Dim value As System.Integer
 
value = instance.IConvertPcurveToBcurveSize(Dim, Order, Nsegs, Coeffs, Basis, Xform, ScaleFactor)
```

```

System.int IConvertPcurveToBcurveSize( 
   System.int Dim,
   System.int Order,
   System.int Nsegs,
   ref System.double Coeffs,
   System.int Basis,
   ref System.double Xform,
   System.double ScaleFactor
)
```

```

System.int IConvertPcurveToBcurveSize( 
   System.int Dim,
   System.int Order,
   System.int Nsegs,
   System.double% Coeffs,
   System.int Basis,
   System.double% Xform,
   System.double ScaleFactor
) 
```

#### Parameters

*Dim*
:   Dimension of the curve:

    - 3 = nonrational
    - 4 = rational

*Order*
:   Order of the curve; minimum is 2 (linear)

*Nsegs*
:   Number of segments in the curve; must be at least 1

*Coeffs*
:   Array of coefficients

*Basis*
:   0; not currently used

*Xform*
:   Transformation matrix to apply after conversion to b-curve

*ScaleFactor*
:   Units conversion factor to apply after conversion to b-curve

#### Return Value

Indicates that conversion succeeded or failed

Remarks

Dimension of coefficient vectors dim:

- For rational curves dim = 4.
- For non-rational curves dim = 3.

Order of each segment of the curve order:

1. The order of the curve = degree + 1.
2. The minimum order is 2.

Number of segments in the curve nseg:

- There must be at least one segment (nseg >= 1).
- Adjacent segments must meet.

Coefficient data coeffs:

- Contains order \* nseg vectors of dimension dim. If dim = 3, then the vectors are 3-D vectors giving the x, y and z components. If dim = 4, then each vector has a weight (w) associated with it, and x, y, z and w components are supplied for each vector. The weights supplied must be greater than 0.
- The coefficients are supplied in order, segment by segment.
- The interpretation of the coefficients depends on the representation method chosen; this is determined by the value of the argument basis.

Representation method basis:

The expressions for each segment of the B-curve P(t) in the various representations are shown next. For generality, the rational form is given.

The simplification to the non-rational form can be obtained by setting both the weights and the denominator equal to 1.0

Polynomial coefficients:

The curve equation is given by a rational polynomial of order 'order':

                        n                     n

                        --         i        / --     i

          P(t)   =   >   w  A  t     /   >  w  t

                        --   i  i    /        --  i

                        i=0                 i=0

          where n = order-1

                A = polynomial coefficient

                  i

                w = weight for A

                  i              i

The polynomial coefficients are supplied starting with the constant  term and ending with the term of highest degree.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::ExtentCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ExtentCurve.md)  
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.md)  
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.md)  
[ConvertArcToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.md)  
[ConvertLineToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.md)  
[GetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams.md)  
[ICurve::IConvertArcToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertArcToBcurveSize.md)  
[ICurve::IConvertLineToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertLineToBcurveSize.md)  
[ICurve::IGetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams.md)  
[ICurve::IGetBCurveParamsSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize2.md)  
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.md)
