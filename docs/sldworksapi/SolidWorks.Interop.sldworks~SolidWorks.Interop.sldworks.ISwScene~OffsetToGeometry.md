# OffsetToGeometry Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~OffsetToGeometry`

Resets the floor offset.
Resets the floor offset.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function OffsetToGeometry() As System.Boolean
```

```

Dim instance As ISwScene
Dim value As System.Boolean
 
value = instance.OffsetToGeometry()
```

```

System.bool OffsetToGeometry()
```

```

System.bool OffsetToGeometry(); 
```

#### Return Value

True if successful, false if not

Remarks

Calling this method invalidates previous calls to [ISwScene::FloorOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorOffset.md) and [ISwScene::FloorOffsetDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorOffsetDirection.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
