# GetScene Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetScene`

Gets the ISwScene object for this configuration.
Gets the ISwScene object for this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetScene() As SWScene
```

```

Dim instance As IConfiguration
Dim value As SWScene
 
value = instance.GetScene()
```

```

SWScene GetScene()
```

```

SWScene^ GetScene(); 
```

#### Return Value

[ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)

Example

[Get and Set Scene Properties (VBA)](Get_and_Set_Scene_Properties_Example_VB.htm)  
[Get and Set Scene Properties (VB.NET)](Get_and_Set_Scene_Properties_Example_VBNET.htm)  
[Get and Set Scene Properties (C#)](Get_and_Set_Scene_Properties_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IModelDocExtension::InsertScene Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertScene.md)  
[IModelDocExtension::DeleteScene Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteScene.md)
