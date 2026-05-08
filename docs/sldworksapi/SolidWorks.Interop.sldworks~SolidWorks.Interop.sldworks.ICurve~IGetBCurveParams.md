# IGetBCurveParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams`

Obsolete. Superseded by ICurve::IGetBCurveParams3.
Obsolete. Superseded by [ICurve::IGetBCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBCurveParams() As System.Double
```

```

Dim instance As ICurve
Dim value As System.Double
 
value = instance.IGetBCurveParams()
```

```

System.double IGetBCurveParams()
```

```

System.double IGetBCurveParams(); 
```

#### Return Value

Pointer to an array of doubles describing the parameters of the curve (see **Remarks**)

Remarks

Call [ICurve::IGetBCurveParamsSize2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize2.md) to determine the size of the array returned and whether the curve data returned by ICurve::IGetBCurveParams is cubic rational or not.

To control the accuracy of the curve data, see [IModeler::SetToleranceValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetToleranceValue.md).

The return value is an array of doubles. The array size is ( 2 + numKnots + numControlPointDoubles) where numKnots is (numControlPoints + order). The array is as follows:

**[** *packedDouble1, packedDouble2, knot1, knot2,..., ControlPoint1[Dimension], ControlPoint2[Dimension],...***]**

where:

- *packedDouble1* is an integer pair containing the *Dimension* and *Order*
- *packedDouble2*  is an integer pair containing the *NumControlPoints* and *Periodicity*
- *knot1*
- *knot2*

...

- *ControlPoint1[dimension]*
- *ControlPoint2[dimension]*

...

The size of the control point array is based on the curve dimension:

- If *Dimension* = 3, then *ControlPoint* is an array of 3 doubles ( x, y, z )
- If *Dimension* = 4, then *ControlPoint* is an array of 4 doubles ( x, y, z, w ) where  
  w = weight

Example

[Get Curve Spline Points (C++)](Get_Curve_Spline_Points_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::GetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams.md)  
[ICurve::ConvertArcToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.md)  
[ICurve::ConvertLineToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.md)  
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.md)  
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.md)  
[ICurve::IConvertPcurveToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize.md)  
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.md)  
[ICurve::IConvertArcToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertArcToBcurveSize.md)  
[ICurve::IConvertLineToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertLineToBcurveSize.md)  
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.md)
