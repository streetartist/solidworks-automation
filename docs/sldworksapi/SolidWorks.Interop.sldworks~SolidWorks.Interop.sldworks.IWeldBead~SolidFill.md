# SolidFill Property (IWeldBead)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead~SolidFill`

Gets or sets whether to fill the weld bead annotation.
Gets or sets whether to fill the weld bead annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SolidFill As System.Boolean
```

```

Dim instance As IWeldBead
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

True to fill the weld bead, false to not (see **Remarks**)

Remarks

To get the triangular-shaped weld treatment, use the polygon-related [IDisplayData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md) APIs, which provide you with the geometry information. See the example for more information.

Example

See the [IWeldBead](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldBead Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead.md)  
[IWeldBead Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead_members.md)
