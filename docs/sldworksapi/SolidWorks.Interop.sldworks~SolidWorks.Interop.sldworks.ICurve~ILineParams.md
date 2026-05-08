# ILineParams Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ILineParams`

Gets the parameters of a curve that is a line.
Gets the parameters of a curve that is a line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ILineParams As System.Double
```

```

Dim instance As ICurve
Dim value As System.Double
 
value = instance.ILineParams
```

```

System.double ILineParams {get;}
```

```

property System.double ILineParams {
   System.double get();
}
```

#### Property Value

Pointer to an array of doubles (see **Remarks**)

Remarks

The return value is an array of 6 double values:

[ rootPoint.x, rootPoint.y, rootPoint.z, direction.x, direction.y, direction.z ]

SOLIDWORKS stores rootPoint in meters.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::LineParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~LineParams.md)  
[ICurve::IsLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsLine.md)  
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.md)
