# GetEllipseParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEllipseParams`

Gets the parameters for this elliptical curve.
Gets the parameters for this elliptical curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEllipseParams() As System.Object
```

```

Dim instance As ICurve
Dim value As System.Object
 
value = instance.GetEllipseParams()
```

```

System.object GetEllipseParams()
```

```

System.Object^ GetEllipseParams(); 
```

#### Return Value

Object (see **Remarks**)

Remarks

Use [ICurve::IsEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsEllipse.md) to determine if a curve is an ellipse.

The return value is an array of doubles with the following format:

**[** *centerptX, centerptY, centerptZ, majorRad, majorAxisX, majorAxisY, majorAxisZ,  
minorRad, minorAxisX, minorAxisY, minorAxisZ* **]**

where:

- *centerptX*, *centerptY*, *centerptZ*  = location of ellipse center
- *majorRad*  = major radius
- *majorAxisX*, *majorAxisY*, *majorAxisZ*  = major axis values
- *minorRad*  = minor radius
- *minorAxisX*, *minorAxisY*, *minorAxisZ*  = minor axis values

For Dispatch users, if this curve is not an ellipse, then SOLIDWORKS returns an empty  
VARIANT. Otherwise, SOLIDWORKS returns a SafeArray in Visual Basic for Applications (VBA).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.md)  
[ICurve::IGetEllipseParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetEllipseParams.md)  
[ICurve::IsEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsEllipse.md)
