# Curvature Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Curvature`

Gets or sets the degree of curvature at any point where curvature control was added.
Gets or sets the degree of curvature at any point where curvature control was added.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Curvature As System.Double
```

```

Dim instance As ISplineHandle
Dim value As System.Double
 
instance.Curvature = value
 
value = instance.Curvature
```

```

System.double Curvature {get; set;}
```

```

property System.double Curvature {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Degree of curvature

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
[ISplineHandle::RadiusOfCurvature Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~RadiusOfCurvature.md)
