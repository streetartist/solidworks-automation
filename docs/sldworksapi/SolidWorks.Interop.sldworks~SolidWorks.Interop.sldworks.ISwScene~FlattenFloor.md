# FlattenFloor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FlattenFloor`

Get or sets whether to flatten the floor of a spherical environment to improve the look of models that naturally rest on flat floors.
Get or sets whether to flatten the floor of a spherical environment to improve the look of models that naturally rest on flat floors.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FlattenFloor As System.Boolean
```

```

Dim instance As ISwScene
Dim value As System.Boolean
 
instance.FlattenFloor = value
 
value = instance.FlattenFloor
```

```

System.bool FlattenFloor {get; set;}
```

```

property System.bool FlattenFloor {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flatten the floor, false to not

Remarks

This property is valid only if [ISwScene::BackgroundType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundType.md) is [swSceneBackgroundType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneBackgroundType_e.html).swBackgroundType\_UseEnvironment.

Example

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
