# Reattach Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~Reattach`

Attaches the datum origin to a different entity.
Attaches the datum origin to a different entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Reattach() As System.Boolean
```

```

Dim instance As IDatumOrigin
Dim value As System.Boolean
 
value = instance.Reattach()
```

```

System.bool Reattach()
```

```

System.bool Reattach(); 
```

#### Return Value

True if the datum origin is attached to a different entity, false if not

Remarks

This method:

- Lets you manipulate the datum origin. It attaches the datum origin to the currently selected entity.
- Expects that only one entity (vertex, edge, or sketch point) is selected. That selected entity must be in the same view as the original entity to which the datum origin was attached.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.md)  
[IDatumOrigin Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.md)
