# IGetEllipseParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetEllipseParams`

Gets the parameters for this elliptical curve.
Gets the parameters for this elliptical curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetEllipseParams( _
   ByRef ParamArray As System.Double _
) 
```

```

Dim instance As ICurve
Dim ParamArray As System.Double
 
instance.IGetEllipseParams(ParamArray)
```

```

void IGetEllipseParams( 
   ref System.double ParamArray
)
```

```

void IGetEllipseParams( 
   System.double% ParamArray
) 
```

#### Parameters

*ParamArray*
:   - in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Use [ICurve::IsEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsEllipse.md) to determine if a curve is an ellipse.

The return value is an array of doubles with the following format:

**[** *centerptX, centerptY, centerptZ, majorRad, majorAxisX, majorAxisY, majorAxisZ,  
minorRad, minorAxisX, minorAxisY, minorAxisZ* **]**

where:

- *centerptX, centerptY, centerptZ*  = location of ellipse center
- *majorRad*  = major radius
- *majorAxisX*, *majorAxisY*, *majorAxisZ*  = major axis values
- *minorRad*  = minor radius
- *minorAxisX*, *minorAxisY*, *minorAxisZ* = minor axis values

You must pass an array of 11 doubles that has already been allocated. If you pass a NULL  
pointer or the curve is not an ellipse, then SOLIDWORKS returns S\_false.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::GetEllipseParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEllipseParams.md)  
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.md)
