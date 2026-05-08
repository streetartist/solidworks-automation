# ExtentCurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ExtentCurve`

Extends a b-spline curve by the specified length.
Extends a b-spline curve by the specified length.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ExtentCurve( _
   ByVal AtStart As System.Boolean, _
   ByVal Length As System.Double, _
   ByVal LinearExt As System.Boolean _
) As Curve
```

```

Dim instance As ICurve
Dim AtStart As System.Boolean
Dim Length As System.Double
Dim LinearExt As System.Boolean
Dim value As Curve
 
value = instance.ExtentCurve(AtStart, Length, LinearExt)
```

```

Curve ExtentCurve( 
   System.bool AtStart,
   System.double Length,
   System.bool LinearExt
)
```

```

Curve^ ExtentCurve( 
   System.bool AtStart,
   System.double Length,
   System.bool LinearExt
) 
```

#### Parameters

*AtStart*
:   True to extend b-spline curve from start point, false to extend b-spline curve from end point

*Length*
:   Length by which to extend b-spline curve

*LinearExt*
:   True if the extension is linear, false if not

#### Return Value

Pointer to newly extended [ICurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) object

Remarks

This method only affects b-spline curves. For all other types of curves, this method does nothing.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::CreateTrimmedCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md)  
[ICurve::IConvertPcurveToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize.md)  
[ICurve::IJoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IJoinCurves.md)  
[ICurve::JoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~JoinCurves.md)  
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.md)  
[ICurve::ReverseCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ReverseCurve.md)  
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.md)
