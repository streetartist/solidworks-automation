# IsShared Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IsShared`

Gets whether this sketch is used by more than one feature.
Gets whether this sketch is used by more than one feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsShared() As System.Boolean
```

```

Dim instance As ISketch
Dim value As System.Boolean
 
value = instance.IsShared()
```

```

System.bool IsShared()
```

```

System.bool IsShared(); 
```

#### Return Value

True if this sketch is used by more than one feature, false if not

Example

[Determine If Sketch Is Shared (VBA)](Determine_if_Sketch_is_Shared_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)
