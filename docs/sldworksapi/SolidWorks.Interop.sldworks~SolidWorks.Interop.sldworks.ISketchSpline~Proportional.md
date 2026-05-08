# Proportional Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~Proportional`

Gets or sets whether the spline resizes proportionally when you drag an endpoint the spline.
Gets or sets whether the spline resizes proportionally when you drag an endpoint the spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Proportional As System.Boolean
```

```

Dim instance As ISketchSpline
Dim value As System.Boolean
 
instance.Proportional = value
 
value = instance.Proportional
```

```

System.bool Proportional {get; set;}
```

```

property System.bool Proportional {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to resize the spline proportionally, false to not

Example

[Get and Set Spline Properties (VBA)](Get_and_Set_Spline_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)
