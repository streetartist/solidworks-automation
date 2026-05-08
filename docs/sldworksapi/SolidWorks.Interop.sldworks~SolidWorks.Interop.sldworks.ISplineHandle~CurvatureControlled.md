# CurvatureControlled Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~CurvatureControlled`

Gets or sets whether the spline handle has curvature control.
Gets or sets whether the spline handle has curvature control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CurvatureControlled As System.Boolean
```

```

Dim instance As ISplineHandle
Dim value As System.Boolean
 
instance.CurvatureControlled = value
 
value = instance.CurvatureControlled
```

```

System.bool CurvatureControlled {get; set;}
```

```

property System.bool CurvatureControlled {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the spline handle has curvature control, false if not

Remarks

If the spline handle has curvature control, you can use:

- [ISplineHandle::Curvature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Curvature.md)
- [ISplineHandle::RadiusOfCurvature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~RadiusOfCurvature.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md)  
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.md)
