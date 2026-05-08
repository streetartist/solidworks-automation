# ScaleHatchPattern Property (IDetailCircle)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~ScaleHatchPattern`

Gets or sets whether to scale the hatch pattern for this detail circle.
Gets or sets whether to scale the hatch pattern for this detail circle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ScaleHatchPattern As System.Boolean
```

```

Dim instance As IDetailCircle
Dim value As System.Boolean
 
instance.ScaleHatchPattern = value
 
value = instance.ScaleHatchPattern
```

```

System.bool ScaleHatchPattern {get; set;}
```

```

property System.bool ScaleHatchPattern {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to scale the hatch pattern based on the scale of the detail view, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)
