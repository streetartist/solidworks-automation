# FloorAutoSize Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorAutoSize`

Gets or sets whether to resize the scene floor based on the model bounding box.
Gets or sets whether to resize the scene floor based on the model bounding box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FloorAutoSize As System.Boolean
```

```

Dim instance As ISwScene
Dim value As System.Boolean
 
instance.FloorAutoSize = value
 
value = instance.FloorAutoSize
```

```

System.bool FloorAutoSize {get; set;}
```

```

property System.bool FloorAutoSize {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to resize the scene floor based on the model bounding box, false to manually specify the width, depth, and rotation of the scene floor

Example

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
