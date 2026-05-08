# FloorRotation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorRotation`

Gets or sets the rotation of the scene floor relative to the environment of this scene.
Gets or sets the rotation of the scene floor relative to the environment of this scene.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FloorRotation As System.Double
```

```

Dim instance As ISwScene
Dim value As System.Double
 
instance.FloorRotation = value
 
value = instance.FloorRotation
```

```

System.double FloorRotation {get; set;}
```

```

property System.double FloorRotation {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.0 <= Rotation in degrees <= 360.0

Remarks

This property is valid only if [ISwScene::FloorAutoSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorAutoSize.md) is false.

Example

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
