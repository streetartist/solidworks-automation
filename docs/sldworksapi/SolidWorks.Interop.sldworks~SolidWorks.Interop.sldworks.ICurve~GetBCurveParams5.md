# GetBCurveParams5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams5`

Gets a data object containing the parameters of a Bézier curve.
Gets a data object containing the parameters of a Bézier curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBCurveParams5( _
   ByVal WantCubicIn As System.Boolean, _
   ByVal WantNRational As System.Boolean, _
   ByVal ForceNonPeriodic As System.Boolean, _
   ByVal IsClosed As System.Boolean _
) As SplineParamData
```

```

Dim instance As ICurve
Dim WantCubicIn As System.Boolean
Dim WantNRational As System.Boolean
Dim ForceNonPeriodic As System.Boolean
Dim IsClosed As System.Boolean
Dim value As SplineParamData
 
value = instance.GetBCurveParams5(WantCubicIn, WantNRational, ForceNonPeriodic, IsClosed)
```

```

SplineParamData GetBCurveParams5( 
   System.bool WantCubicIn,
   System.bool WantNRational,
   System.bool ForceNonPeriodic,
   System.bool IsClosed
)
```

```

SplineParamData^ GetBCurveParams5( 
   System.bool WantCubicIn,
   System.bool WantNRational,
   System.bool ForceNonPeriodic,
   System.bool IsClosed
) 
```

#### Parameters

*WantCubicIn*
:   True to return cubic parameters, false to not

*WantNRational*
:   True to return non-rational parameters; false to return rational parameters

*ForceNonPeriodic*
:   True to convert the curve from periodic to nonperiodic, false to not (see **Remarks**)

*IsClosed*
:   True for a closed curve, false for an open curve (see **Remarks**)

#### Return Value

An [ISplineParamData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.md) object (see **Remarks**)

Remarks

To control the accuracy of the curve data, see [IModeler::SetToleranceValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetToleranceValue.md).

If a Bézier curve is closed (IsClosed = true) and periodic (ForceNonPeriodic = false), the seam at the juncture of the beginning and end of the curve is continuous and smooth. The data returned in this form contains a single knot at the juncture.

If a Bézier curve is closed (IsClosed = true) and non-periodic (ForceNonPeriodic = true), the seam at the juncture is continuous, contains a cusp, and is not smooth. The data returned in this form contains multiple knots at each end of the curve.

Obsolete versions of this method automatically treated closed Bézier curves as periodic. The cusp at the juncture of a closed non-periodic curve (e.g., a tear drop) was lost using these methods. This method provides more flexibility for specifying precisely which form of the curve to get to prevent unintentional data loss.

This method returns the parameterization data of the Bézier curve in an ISplineParamData object instead of an array. Call the methods and properties of [ISplineParamData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.md) to obtain the control points, knot points, dimension, order, and periodicity of the curve.

Example

[Get BCurve Spline Points (C#)](Get_BCurve_Spline_Points_Example_CSharp.htm)  
[Get BCurve Spline Points (VB.NET)](Get_BCurve_Spline_Points_Example_VBNET.htm)  
[Get BCurve Spline Points (VBA)](Get_BCurve_Spline_Points_Example_VB.htm)  
[Edit Spline (VBA)](Edit_Spline_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.md)  
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.md)  
[ICurve::CircleParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CircleParams.md)  
[ICurve::ICircleParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ICircleParams.md)  
[ICurve::ILineParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ILineParams.md)  
[ICurve::LineParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~LineParams.md)  
[ICurve::ConvertArcToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.md)  
[ICurve::ConvertLineToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.md)  
[ICurve::GetEllipseParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEllipseParams.md)  
[ICurve::IGetEllipseParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetEllipseParams.md)  
[ICurve::GetPCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams2.md)  
[ICurve::IGetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParams.md)  
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.md)  
[ICurve::IGetBCurveParamsSize3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize3.md)  
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.md)  
[ICurve::IsCircle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsCircle.md)  
[ICurve::IsEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsEllipse.md)  
[ICurve::IsLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsLine.md)  
[ICurve::MakeBsplineCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve2.md)  
[IEdge::GetCurveParams3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams3.md)  
[IEdge::IGetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.md)  
[IModeler::CreatePCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePCurve.md)  
[IModeler::ICreatePCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePCurve.md)
