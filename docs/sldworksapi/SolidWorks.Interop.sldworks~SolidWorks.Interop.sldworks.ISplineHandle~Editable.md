# Editable Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Editable`

Gets or sets whether this spline handle can be edited.
Gets or sets whether this spline handle can be edited.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Editable As System.Boolean
```

```

Dim instance As ISplineHandle
Dim value As System.Boolean
 
instance.Editable = value
 
value = instance.Editable
```

```

System.bool Editable {get; set;}
```

```

property System.bool Editable {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

Trueif the spline can be edited, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md)  
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.md)
