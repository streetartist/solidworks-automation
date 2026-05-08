# FloorAlignment Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorAlignment`

Gets or sets the plane with which to align the scene floor.
Gets or sets the plane with which to align the scene floor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FloorAlignment As System.Integer
```

```

Dim instance As ISwScene
Dim value As System.Integer
 
instance.FloorAlignment = value
 
value = instance.FloorAlignment
```

```

System.int FloorAlignment {get; set;}
```

```

property System.int FloorAlignment {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Scene floor alignment plane as defined by [swSceneFloorAlign\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneFloorAlign_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
