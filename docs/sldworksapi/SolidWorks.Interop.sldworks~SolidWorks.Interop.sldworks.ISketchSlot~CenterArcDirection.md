# CenterArcDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~CenterArcDirection`

Gets the direction of the slot.
Gets the direction of the slot.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CenterArcDirection As System.Integer
```

```

Dim instance As ISketchSlot
Dim value As System.Integer
 
value = instance.CenterArcDirection
```

```

System.int CenterArcDirection {get;}
```

```

property System.int CenterArcDirection {
   System.int get();
}
```

#### Property Value

-1 for clockwise, 1 for counter-clockwise

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSlot Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot.md)  
[ISketchSlot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot_members.md)  
[ISketchSlot::CreationType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~CreationType.md)
