# GetBCurveParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams`

Obsolete. Superseded by ICurve::GetBCurveParams3.
Obsolete. Superseded by [ICurve::GetBCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBCurveParams( _
   ByVal WantCubicIn As System.Boolean _
) As System.Object
```

```

Dim instance As ICurve
Dim WantCubicIn As System.Boolean
Dim value As System.Object
 
value = instance.GetBCurveParams(WantCubicIn)
```

```

System.object GetBCurveParams( 
   System.bool WantCubicIn
)
```

```

System.Object^ GetBCurveParams( 
   System.bool WantCubicIn
) 
```

#### Parameters

*WantCubicIn*
:   True returns cubic rational parameters, false does not

#### Return Value

Array describing the parameters of the curve (see **Remarks**)

Remarks

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

[Get Curve Spline Points (VBA)](Get_Curve_Spline_Points_Example_VB.htm)  
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)  
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)  
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::ConvertArcToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.md)  
[ICurve::ConvertLineToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.md)  
[ICurve::IGetBCurveParamsSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize2.md)  
[ICurve::ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.md)  
[ICurve::IConvertPcurveToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize.md)  
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.md)
