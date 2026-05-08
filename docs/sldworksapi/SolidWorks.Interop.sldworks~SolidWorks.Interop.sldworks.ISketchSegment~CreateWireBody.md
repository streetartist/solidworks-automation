# CreateWireBody Method (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~CreateWireBody`

Creates a wire body using the selected sketch segment.
Creates a wire body using the selected sketch segment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateWireBody() As Body2
```

```

Dim instance As ISketchSegment
Dim value As Body2
 
value = instance.CreateWireBody()
```

```

Body2 CreateWireBody()
```

```

Body2^ CreateWireBody(); 
```

#### Return Value

[Body2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

Wire bodies contain wires, loops, coedges, edges, and vertices. Wires typically represent profiles, construction lines, and center lines of swept shapes. Wires can also represent wire frames that, when surfaced, form shells.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)
