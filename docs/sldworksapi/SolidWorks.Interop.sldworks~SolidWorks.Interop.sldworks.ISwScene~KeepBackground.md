# KeepBackground Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~KeepBackground`

Gets or sets whether to retain the background when replacing the scene.
Gets or sets whether to retain the background when replacing the scene.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KeepBackground As System.Boolean
```

```

Dim instance As ISwScene
Dim value As System.Boolean
 
instance.KeepBackground = value
 
value = instance.KeepBackground
```

```

System.bool KeepBackground {get; set;}
```

```

property System.bool KeepBackground {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to retain the background when replacing a scene, false to not

Remarks

This property is valid only if [ISwScene::BackgroundType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundType.md) is set to one of the following:

- [swSceneBackgroundType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneBackgroundType_e.html).swBackgroundType\_Image
- swSceneBackgroundType\_e.swBackgroundType\_Graduated
- swSceneBackgroundType\_e.swBackgroundType\_Plain

Example

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
