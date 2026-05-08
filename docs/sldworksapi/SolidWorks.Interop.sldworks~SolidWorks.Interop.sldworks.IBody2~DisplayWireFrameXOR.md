# DisplayWireFrameXOR Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DisplayWireFrameXOR`

Displays a temporary body in the given part's context in XOR mode.
Displays a temporary body in the given part's context in XOR mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub DisplayWireFrameXOR( _
   ByVal Part As System.Object, _
   ByVal Color As System.Integer _
) 
```

```

Dim instance As IBody2
Dim Part As System.Object
Dim Color As System.Integer
 
instance.DisplayWireFrameXOR(Part, Color)
```

```

void DisplayWireFrameXOR( 
   System.object Part,
   System.int Color
)
```

```

void DisplayWireFrameXOR( 
   System.Object^ Part,
   System.int Color
) 
```

#### Parameters

*Part*
:   Part

*Color*
:   Color of part

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::IDisplayWireFrameXOR Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDisplayWireFrameXOR.md)
