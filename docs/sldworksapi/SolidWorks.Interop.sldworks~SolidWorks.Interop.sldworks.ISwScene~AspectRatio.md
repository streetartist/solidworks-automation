# AspectRatio Property (ISwScene)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~AspectRatio`

Gets the aspect ratio of the scene floor.
Gets the aspect ratio of the scene floor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property AspectRatio As System.Double
```

```

Dim instance As ISwScene
Dim value As System.Double
 
value = instance.AspectRatio
```

```

System.double AspectRatio {get;}
```

```

property System.double AspectRatio {
   System.double get();
}
```

#### Property Value

Aspect ratio

Remarks

To change the aspect ratio, set [ISwScene::FixedAspectRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FixedAspectRatio.md) to false and specify:

- [ISwScene::FloorDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorDepth.md)
- [ISwScene::FloorWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorWidth.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
