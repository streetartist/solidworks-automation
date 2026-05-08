# FixedAspectRatio Property (ISwScene)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FixedAspectRatio`

Gets or sets whether to fix the aspect ratio of the scene floor.
Gets or sets whether to fix the aspect ratio of the scene floor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FixedAspectRatio As System.Boolean
```

```

Dim instance As ISwScene
Dim value As System.Boolean
 
instance.FixedAspectRatio = value
 
value = instance.FixedAspectRatio
```

```

System.bool FixedAspectRatio {get; set;}
```

```

property System.bool FixedAspectRatio {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to fix the aspect ratio of the scene floor, false to allow the scene floor width and height to change independently

Remarks

If this property is set to true, then you need only specify one of the following:

- [ISwScene::FloorDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorDepth.md)
- [ISwScene::FloorWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorWidth.md)

To change the [aspect ratio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~AspectRatio.md), set this property to false and set both of the following:

- ISwScene::FloorDepth
- ISwScene::FloorWidth

Example

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
