# BackgroundTopGradientColor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundTopGradientColor`

Gets or sets the background color of this scene.
Gets or sets the background color of this scene.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BackgroundTopGradientColor As System.Integer
```

```

Dim instance As ISwScene
Dim value As System.Integer
 
instance.BackgroundTopGradientColor = value
 
value = instance.BackgroundTopGradientColor
```

```

System.int BackgroundTopGradientColor {get; set;}
```

```

property System.int BackgroundTopGradientColor {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

RGB color

Remarks

| If [ISwScene::BackgroundType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundType.md) is... | Then this property sets... |
| --- | --- |
| [swSceneBackgroundType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneBackgroundType_e.html).swBackgroundType\_Plain | a single background color. |
| swSceneBackgroundType\_e.swBackgroundType\_Graduated | the top color in the graduated range of background colors; Use [ISwScene::BackgroundBottomGradientColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundBottomGradientColor.md) to set the bottom color in the graduated range of background colors. |

Example

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
