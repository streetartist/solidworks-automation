# BackgroundBottomGradientColor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundBottomGradientColor`

Gets or sets the bottom color of the graduated range of background colors of this scene.
Gets or sets the bottom color of the graduated range of background colors of this scene.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BackgroundBottomGradientColor As System.Integer
```

```

Dim instance As ISwScene
Dim value As System.Integer
 
instance.BackgroundBottomGradientColor = value
 
value = instance.BackgroundBottomGradientColor
```

```

System.int BackgroundBottomGradientColor {get; set;}
```

```

property System.int BackgroundBottomGradientColor {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

RGB color

Remarks

This property is valid only if [ISwScene::BackgroundType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundType.md) is [swSceneBackgroundType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneBackgroundType_e.html).swBackgroundType\_Graduated.

Set the top color of the graduated range of background colors with [ISwScene::BackgroundTopGradientColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundTopGradientColor.md).

Example

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
