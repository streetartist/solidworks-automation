# GetMaterial Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMaterial`

Gets the appearance for the specified appearance ID in the specified configuration in this model document
Gets the appearance for the specified appearance ID in the specified configuration in this model document

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMaterial( _
   ByVal ID As System.Integer, _
   ByVal Configuration As System.String _
) As RenderMaterial
```

```

Dim instance As IModelDocExtension
Dim ID As System.Integer
Dim Configuration As System.String
Dim value As RenderMaterial
 
value = instance.GetMaterial(ID, Configuration)
```

```

RenderMaterial GetMaterial( 
   System.int ID,
   System.string Configuration
)
```

```

RenderMaterial^ GetMaterial( 
   System.int ID,
   System.String^ Configuration
) 
```

#### Parameters

*ID*
:   Appearance Id

*Configuration*
:   Name of the configuration where the appearance is applied

#### Return Value

[Appearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IModelDocExtension::AddDefaultRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDefaultRenderMaterial.md)  
[IModelDocExtension::AddRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddRenderMaterial.md)  
[IModelDocExtension::CreateRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateRenderMaterial.md)  
[IModelDocExtension::DeleteRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteRenderMaterial.md)  
[IModelDocExtension::GetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterials.md)  
[IModelDocExtension::GetRenderMaterialsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount.md)  
[IModelDocExtension::IGetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetRenderMaterials.md)  
[IModelDocExtension::UpdateRenderMaterialsInSceneGraph Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateRenderMaterialsInSceneGraph.md)
