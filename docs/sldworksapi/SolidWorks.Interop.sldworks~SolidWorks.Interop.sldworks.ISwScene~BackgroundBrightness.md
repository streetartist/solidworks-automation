# BackgroundBrightness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundBrightness`

Gets or sets the brightness of the background.
Gets or sets the brightness of the background.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BackgroundBrightness As System.Double
```

```

Dim instance As ISwScene
Dim value As System.Double
 
instance.BackgroundBrightness = value
 
value = instance.BackgroundBrightness
```

```

System.double BackgroundBrightness {get; set;}
```

```

property System.double BackgroundBrightness {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Brightness

Remarks

This property is valid only when:

- a ray-trace rendering engine is activated
- [ISwScene::BackgroundType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundType.md) is not [swSceneBackgroundType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneBackgroundType_e.html).swBackgroundType\_None

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
