# FloorDepth Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorDepth`

Gets or sets the depth of the scene floor.
Gets or sets the depth of the scene floor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FloorDepth As System.Double
```

```

Dim instance As ISwScene
Dim value As System.Double
 
instance.FloorDepth = value
 
value = instance.FloorDepth
```

```

System.double FloorDepth {get; set;}
```

```

property System.double FloorDepth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Depth of the scene floor

Remarks

The setting of this property is valid only if [ISwScene::FloorAutoSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorAutoSize.md) is false.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
