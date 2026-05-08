# IGetBCurveParams3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams3`

Obsolete. Superseded by ICurve::GetBCurveParams4.
Obsolete. Superseded by [ICurve::GetBCurveParams4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBCurveParams3( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

```

Dim instance As ICurve
Dim ArraySize As System.Integer
Dim value As System.Double
 
value = instance.IGetBCurveParams3(ArraySize)
```

```

System.double IGetBCurveParams3( 
   System.int ArraySize
)
```

```

System.double IGetBCurveParams3( 
   System.int ArraySize
) 
```

#### Parameters

*ArraySize*
:   Size of the return array

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles describing the parameters of the curve

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Use [ICurve::IGetBCurveParamsSize3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize3.md) to determine the size of the array returned and whether the curve data returned by Curve::IGetBCurveParams3 is cubic rational or not.

To control the accuracy of the curve data, see [IModeler::SetToleranceValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetToleranceValue.md).

The return value retval is an array of doubles. The array size is ( 2 + numKnots + numControlPointDoubles) where numKnots is (numControlPoints + order). The array is as follows:

[ packedDouble1, packedDouble2, knot1, knot2,..., ControlPoint1[Dimension], ControlPoint2[Dimension],... ]

where:

- packedDouble1 is an integer pair containing the Dimension and Order
- packedDouble2  is an integer pair containing the NumControlPoints and Periodicity
- knot1
- knot2

...

- ControlPoint1[dimension]
- ControlPoint2[dimension]

...

The size of the control point array is based on the curve dimension:

- If Dimension = 3, then ControlPoint is an array of 3 doubles ( x, y, z )
- If Dimension = 4, then ControlPoint is an array of 4 doubles ( x, y, z, w ) where w = weight

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::GetBCurveParams3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams3.md)  
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.md)  
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.md)  
[ICurve::CircleParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CircleParams.md)  
[ICurve::ICircleParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ICircleParams.md)  
[ICurve::ILineParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ILineParams.md)  
[ICurve::LineParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~LineParams.md)  
[ICurve::ConvertArcToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.md)  
[ICurve::ConvertLineToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.md)  
[ICurve::GetEllipseParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEllipseParams.md)  
[ICurve::GetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams.md)  
[ICurve::IGetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParams.md)  
[ICurve::IGetEllipseParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetEllipseParams.md)  
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.md)  
[ICurve::IGetSplinePts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePts.md)  
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.md)  
[ICurve::IsCircle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsCircle.md)  
[ICurve::IsEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsEllipse.md)  
[ICurve::IsLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsLine.md)  
[ICurve::MakeBsplineCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve2.md)  
[IEdge::GetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.md)  
[IEdge::IGetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.md)  
[IModeler::CreatePCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePCurve.md)  
[IModeler::ICreatePCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePCurve.md)
