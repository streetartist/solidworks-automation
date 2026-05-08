# AddRenderMaterial Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddRenderMaterial`

Not supported in SOLIDWORKS 2011 and later. Superseded by IModelDocExtension::AddDisplayStateSpecificRenderMaterial and IModelDocExtension::IAddDisplayStateSpecificRenderMaterial.
Not supported in SOLIDWORKS 2011 and later. Superseded by [IModelDocExtension::AddDisplayStateSpecificRenderMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDisplayStateSpecificRenderMaterial.md) and [IModelDocExtension::IAddDisplayStateSpecificRenderMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddRenderMaterial( _
   ByVal PRenderMaterial As RenderMaterial, _
   ByRef PwMaterialId As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim PRenderMaterial As RenderMaterial
Dim PwMaterialId As System.Integer
Dim value As System.Boolean
 
value = instance.AddRenderMaterial(PRenderMaterial, PwMaterialId)
```

```

System.bool AddRenderMaterial( 
   RenderMaterial PRenderMaterial,
   out System.int PwMaterialId
)
```

```

System.bool AddRenderMaterial( 
   RenderMaterial^ PRenderMaterial,
   [Out] System.int PwMaterialId
) 
```

#### Parameters

*PRenderMaterial*
:   [Appearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md) to add to the model

*PwMaterialId*
:   Appearance ID

#### Return Value

True if the appearance is added to the model, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
