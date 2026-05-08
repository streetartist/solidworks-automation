# MakeBsplineCurve2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve2`

Creates a b-spline curve.
Creates a b-spline curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeBsplineCurve2() As Curve
```

```

Dim instance As ICurve
Dim value As Curve
 
value = instance.MakeBsplineCurve2()
```

```

Curve MakeBsplineCurve2()
```

```

Curve^ MakeBsplineCurve2(); 
```

#### Return Value

B-spline [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Remarks

This method uses the input curve as it is and allows lines and arcs.

To convert the arc or line to a b-spline, use any of these methods:

- [ICurve::ConvertArcToBcurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.md)
- [ICurve::ConvertLineToBcurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.md)
- [ICurve::GetBCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams3.md) and [ICurve::IGetBCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams3.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::CreateTrimmedCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md)  
[ICurve::ExtentCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ExtentCurve.md)  
[ICurve::IConvertPcurveToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize.md)  
[ICurve::IJoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IJoinCurves.md)  
[ICurve::JoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~JoinCurves.md)  
[ICurve::IReverseCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IReverseCurve.md)  
[ICurve::ReverseCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ReverseCurve.md)  
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.md)
