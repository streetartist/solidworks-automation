# AddOrEditFloorAppearance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~AddOrEditFloorAppearance`

Adds or modifies the floor appearance of this scene.
Adds or modifies the floor appearance of this scene.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub AddOrEditFloorAppearance( _
   ByVal Appearance As RenderMaterial _
) 
```

```

Dim instance As ISwScene
Dim Appearance As RenderMaterial
 
instance.AddOrEditFloorAppearance(Appearance)
```

```

void AddOrEditFloorAppearance( 
   RenderMaterial Appearance
)
```

```

void AddOrEditFloorAppearance( 
   RenderMaterial^ Appearance
) 
```

#### Parameters

*Appearance*
:   [IRenderMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
