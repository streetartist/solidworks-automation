# SolidFill Property (ISketchHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~SolidFill`

Gets or sets whether to enable solid fill for the sketch hatch.
Gets or sets whether to enable solid fill for the sketch hatch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SolidFill As System.Boolean
```

```

Dim instance As ISketchHatch
Dim value As System.Boolean
 
instance.SolidFill = value
 
value = instance.SolidFill
```

```

System.bool SolidFill {get; set;}
```

```

property System.bool SolidFill {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable solid fill, false to not

Example

See the [ISketchHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md)  
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.md)
