# FloorOffset Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorOffset`

Gets or sets the height of the model above or below the floor of this scene.
Gets or sets the height of the model above or below the floor of this scene.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FloorOffset As System.Double
```

```

Dim instance As ISwScene
Dim value As System.Double
 
instance.FloorOffset = value
 
value = instance.FloorOffset
```

```

System.double FloorOffset {get; set;}
```

```

property System.double FloorOffset {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance between the scene floor and the model

Example

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
