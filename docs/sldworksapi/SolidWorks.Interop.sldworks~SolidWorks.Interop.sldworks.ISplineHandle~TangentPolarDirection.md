# TangentPolarDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentPolarDirection`

Gets or sets the tangent polar direction, which is the elevation angle of the tangent vector to a plane placed at a point perpendicular to a spline point.
Gets or sets the tangent polar direction, which is the elevation angle of the tangent vector to a plane placed at a point perpendicular to a spline point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TangentPolarDirection As System.Double
```

```

Dim instance As ISplineHandle
Dim value As System.Double
 
instance.TangentPolarDirection = value
 
value = instance.TangentPolarDirection
```

```

System.double TangentPolarDirection {get; set;}
```

```

property System.double TangentPolarDirection {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Tangent polar direction

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md)  
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.md)  
[ISplineHandle::TangentDriving Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentDriving.md)  
[ISplineHandle::TangentMagnitude Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentMagnitude.md)  
[ISplineHandle::TangentRadialDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentRadialDirection.md)
