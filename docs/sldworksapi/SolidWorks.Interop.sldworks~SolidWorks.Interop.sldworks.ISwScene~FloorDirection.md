# FloorDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorDirection`

Gets or sets whether to flip the direction of the floor of this scene.
Gets or sets whether to flip the direction of the floor of this scene.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FloorDirection As System.Boolean
```

```

Dim instance As ISwScene
Dim value As System.Boolean
 
instance.FloorDirection = value
 
value = instance.FloorDirection
```

```

System.bool FloorDirection {get; set;}
```

```

property System.bool FloorDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the direction of the floor, false to not

Example

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
