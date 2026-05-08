# QuantityPlacement Property (IBalloonOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~QuantityPlacement`

Gets and sets the placement of the BOM item quantity with respect to its balloon.
Gets and sets the placement of the BOM item quantity with respect to its balloon.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property QuantityPlacement As System.Integer
```

```

Dim instance As IBalloonOptions
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

Placement of the BOM item quantity as defined in [swBalloonQuantityPlacement\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonQuantityPlacement_e.html)

Remarks

See the SOLIDWORKS Help for additional details about balloons.

Example

See [IBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.md)  
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.md)
