# IGetRenderMaterials Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetRenderMaterials`

Obsolete. Superseded by IModelDocExtension::GetRenderMaterials2.
Obsolete. Superseded by [IModelDocExtension::GetRenderMaterials2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterials2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetRenderMaterials( _
   ByVal Count As System.Integer _
) As RenderMaterial
```

```

Dim instance As IModelDocExtension
Dim Count As System.Integer
Dim value As RenderMaterial
 
value = instance.IGetRenderMaterials(Count)
```

```

RenderMaterial IGetRenderMaterials( 
   System.int Count
)
```

```

RenderMaterial^ IGetRenderMaterials( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of appearance

#### Return Value

- unmanaged C++: Pointer to an array of [appearances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IModelDocExtension::GetRenderMaterialsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount.md) to get the value of Count.

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
[IModelDocExtension::GetMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMaterial.md)  
[IModelDocExtension::GetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterials.md)  
[IModelDocExtension::UpdateRenderMaterialsInSceneGraph Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateRenderMaterialsInSceneGraph.md)
