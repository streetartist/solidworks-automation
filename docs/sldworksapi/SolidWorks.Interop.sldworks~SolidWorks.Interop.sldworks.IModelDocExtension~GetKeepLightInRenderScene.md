# GetKeepLightInRenderScene Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetKeepLightInRenderScene`

Gets whether a light is kept when the scene changes.
Gets whether a light is kept when the scene changes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetKeepLightInRenderScene( _
   ByVal ID As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim ID As System.Integer
Dim value As System.Boolean
 
value = instance.GetKeepLightInRenderScene(ID)
```

```

System.bool GetKeepLightInRenderScene( 
   System.int ID
)
```

```

System.bool GetKeepLightInRenderScene( 
   System.int ID
) 
```

#### Parameters

*ID*
:   Light ID

#### Return Value

True if the light is kept when the scene changes, false if the light is deleted when the scene changes

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::SetKeepLightInRenderScene Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetKeepLightInRenderScene.md)
