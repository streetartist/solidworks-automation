# CreationType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~CreationType`

Gets the type of slot.
Gets the type of slot.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CreationType As System.Integer
```

```

Dim instance As ISketchSlot
Dim value As System.Integer
 
value = instance.CreationType
```

```

System.int CreationType {get;}
```

```

property System.int CreationType {
   System.int get();
}
```

#### Property Value

Type of slot as defined in [swSketchSlotCreationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchSlotCreationType_e.html)

**NOTE:** Only swSketchSlotCreateType\_line or swSketchSlotCreateType\_arc are valid return values.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSlot Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot.md)  
[ISketchSlot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot_members.md)
