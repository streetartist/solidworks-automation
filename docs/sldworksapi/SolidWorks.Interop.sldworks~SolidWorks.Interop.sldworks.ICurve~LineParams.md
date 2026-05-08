# LineParams Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~LineParams`

Gets the parameters of a curve that is a line.
Gets the parameters of a curve that is a line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property LineParams As System.Object
```

```

Dim instance As ICurve
Dim value As System.Object
 
value = instance.LineParams
```

```

System.object LineParams {get;}
```

```

property System.Object^ LineParams {
   System.Object^ get();
}
```

#### Property Value

Array of doubles (see **Remarks**)

Remarks

The return value is an array of 6 double values:

[ rootPoint.x, rootPoint.y, rootPoint.z, direction.x, direction.y, direction.z ]

SOLIDWORKS stores rootPoint in meters.

Example

[Get Angle Between Plane and Line (VBA)](Get_Angle_Between_Plane_and_Line_Example_VB.htm)  
[Get Line Parameters (VBA)](Get_Line_Parameters_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::ILineParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ILineParams.md)  
[ICurve::IsLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsLine.md)  
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.md)
