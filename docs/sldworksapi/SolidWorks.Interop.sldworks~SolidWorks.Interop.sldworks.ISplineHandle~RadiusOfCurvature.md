# RadiusOfCurvature Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~RadiusOfCurvature`

Gets or sets the radius of curvature at any spline point.
Gets or sets the radius of curvature at any spline point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RadiusOfCurvature As System.Double
```

```

Dim instance As ISplineHandle
Dim value As System.Double
 
instance.RadiusOfCurvature = value
 
value = instance.RadiusOfCurvature
```

```

System.double RadiusOfCurvature {get; set;}
```

```

property System.double RadiusOfCurvature {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Radius of curvature

Remarks

Curvature control must be enabled for this property to have an effect. Use [ISplineHandle::CurvatureControlled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~CurvatureControlled.md) to see if curvature control is enabled or to set curvature control for this spline handle.

Example

See the [ISplineHandle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md)  
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.md)  
[ISplineHandle::Curvature Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Curvature.md)
