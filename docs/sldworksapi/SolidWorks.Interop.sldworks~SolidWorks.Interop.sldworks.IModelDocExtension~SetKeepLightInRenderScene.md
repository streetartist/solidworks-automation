# SetKeepLightInRenderScene Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetKeepLightInRenderScene`

Sets whether to keep a light when the scene changes.
Sets whether to keep a light when the scene changes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetKeepLightInRenderScene( _
   ByVal ID As System.Integer, _
   ByVal Val As System.Boolean _
) 
```

```

Dim instance As IModelDocExtension
Dim ID As System.Integer
Dim Val As System.Boolean
 
instance.SetKeepLightInRenderScene(ID, Val)
```

```

void SetKeepLightInRenderScene( 
   System.int ID,
   System.bool Val
)
```

```

void SetKeepLightInRenderScene( 
   System.int ID,
   System.bool Val
) 
```

#### Parameters

*ID*
:   Light ID

*Val*
:   True to keep a light when the scene changes, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetKeepLightInRenderScene Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetKeepLightInRenderScene.md)
