# IsPenetrating Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision~IsPenetrating`

Gets whether the components involved in this collision penetrate one another.
Gets whether the components involved in this collision penetrate one another.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsPenetrating() As System.Boolean
```

```

Dim instance As ICollision
Dim value As System.Boolean
 
value = instance.IsPenetrating()
```

```

System.bool IsPenetrating()
```

```

System.bool IsPenetrating(); 
```

#### Return Value

True if components penetrate one another, false if they are only in contact

Example

See the [ICollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICollision Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision.md)  
[ICollision Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision_members.md)
