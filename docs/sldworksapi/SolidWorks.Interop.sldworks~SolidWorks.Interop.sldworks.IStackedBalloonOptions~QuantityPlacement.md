# QuantityPlacement Property (IStackedBalloonOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~QuantityPlacement`

Gets and sets the placement of a BOM item quantity with respect to its balloon.
Gets and sets the placement of a BOM item quantity with respect to its balloon.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property QuantityPlacement As System.Integer
```

```

Dim instance As IStackedBalloonOptions
Dim value As System.Integer
 
instance.QuantityPlacement = value
 
value = instance.QuantityPlacement
```

```

System.int QuantityPlacement {get; set;}
```

```

property System.int QuantityPlacement {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Placement of BOM item quantity value as defined in [swBalloonQuantityPlacement\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonQuantityPlacement_e.html); only swBalloonQuantityPlacement\_e.swBalloonQuantityPlacement\_Top and swBalloonQuantityPlacement\_e.swBalloonQuantityPlacement\_Bottom are valid options for stacked balloons

Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

Example

See [IStackedBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md)  
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.md)
