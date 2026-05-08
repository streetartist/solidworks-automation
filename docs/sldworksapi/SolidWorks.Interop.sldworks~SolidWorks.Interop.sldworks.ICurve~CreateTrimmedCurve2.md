# CreateTrimmedCurve2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2`

Creates a trimmed curve.
Creates a trimmed curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateTrimmedCurve2( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
) As Curve
```

```

Dim instance As ICurve
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim value As Curve
 
value = instance.CreateTrimmedCurve2(X1, Y1, Z1, X2, Y2, Z2)
```

```

Curve CreateTrimmedCurve2( 
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

```

Curve^ CreateTrimmedCurve2( 
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
) 
```

#### Parameters

*X1*
:   x start point

*Y1*
:   y start point

*Z1*
:   z end point

*X2*
:   x end point

*Y2*
:   y end point

*Z2*
:   z end point

#### Return Value

Pointer to the [ICurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) object (see **Remarks**)

Remarks

This method trims the curve from the start point to the end point in a parametric direction. It returns NULL if the curve is discontinued or non-linear between the points.

If your application calls [ISurface::CreateTrimmedSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet4.md) or [ISurface::ICreateTrimmedSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet4.md) to create a sheet with a boundary defined by arcs ([IModeler::CreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateArc.md) or [IModeler::ICreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateArc.md)) or lines ([IModeler::CreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLine.md) or [IModeler::ICreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLine.md)), then your application must first call this method to trim the arc and line curves before passing them to ISurface::CreateTrimmedSheet4 or ISurface::ICreateTrimmedSheet4.

If your application calls ISurface::CreateTrimmedSheet4 or ISurface::ICreateTrimmedSheet4 to create a sheet with an elliptical boundary ([IModeler::CreateEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateEllipse.md) or [IModeler::ICreateEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateEllipse.md)), then you do not need to trim the elliptical curve before passing it to ISurface::CreateTrimmedSheet4 or ISurface::ICreateTrimmedSheet4.

Example

[Create Temporary Extruded Body (VBA)](Create_Temporary_Extruded_Body_Example_VB.htm)  
[Create Temporary Elliptical Extrusion (VBA)](Create_Temporary_Elliptical_Extrusion_Example_VB.htm)  
[Create Temporary Elliptical Extrusion (VB.NET)](Create_Temporary_Elliptical_Extrusion_VBNET.htm)  
[Create Temporary Elliptical Extrusion (C#)](Create_Temporary_Elliptical_Extrusion_CSharp.htm)  
[Create Trimmed Curve (VBA)](Return_Untrimmed_Curve_Example_VB.htm)  
[Create Trimmed Curve (VB.NET)](Return_Untrimmed_Curve_Example_VBNET.htm)  
[Create Trimmed Curve (C#)](Return_Untrimmed_Curve_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::ExtentCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ExtentCurve.md)  
[ICurve::IConvertPcurveToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize.md)  
[ICurve::IsTrimmedCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsTrimmedCurve.md)  
[ICurve::JoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~JoinCurves.md)  
[ICurve::ReverseCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ReverseCurve.md)  
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.md)  
[ICurve::JoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~JoinCurves.md)
