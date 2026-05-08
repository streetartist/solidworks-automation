# Update Method (IDragArrowManipulator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Update`

Displays a handle after having modified the length of the handle.
Displays a handle after having modified the length of the handle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Update() As System.Boolean
```

```

Dim instance As IDragArrowManipulator
Dim value As System.Boolean
 
value = instance.Update()
```

```

System.bool Update()
```

```

System.bool Update(); 
```

#### Return Value

True if the length of the handle was updated, false if not

Remarks

To change the length of a handle, use [IDragArrowManipulator::Length](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Length.md) or [IDragArrowManipulator::LengthOppositeDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~LengthOppositeDirection.md), then use this method to see display the modified handle in the graphics area.

Example

See [IDragArrowManipulator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md)  
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.md)  
[IDragArrowManipulator::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Length.md)  
[IDragArrowManipulator::LengthOppositeDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~LengthOppositeDirection.md)
