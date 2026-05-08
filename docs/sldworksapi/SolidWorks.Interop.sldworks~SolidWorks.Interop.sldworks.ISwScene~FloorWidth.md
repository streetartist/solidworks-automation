# FloorWidth Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorWidth`

Gets or sets the width of the scene floor.
Gets or sets the width of the scene floor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FloorWidth As System.Double
```

```

Dim instance As ISwScene
Dim value As System.Double
 
instance.FloorWidth = value
 
value = instance.FloorWidth
```

```

System.double FloorWidth {get; set;}
```

```

property System.double FloorWidth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Width of the scene floor

Remarks

The setting of this property is valid only if [ISwScene::FloorAutoSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorAutoSize.md) is false.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
