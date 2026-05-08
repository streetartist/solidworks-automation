# GetRenderMaterialsCount2 Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount2`

Gets the number of appearances applied to this model document in the specified display states.
Gets the number of appearances applied to this model document in the specified display states.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRenderMaterialsCount2( _
   ByVal DisplayStateOption As System.Integer, _
   ByVal DisplayStateNames As System.Object _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim DisplayStateOption As System.Integer
Dim DisplayStateNames As System.Object
Dim value As System.Integer
 
value = instance.GetRenderMaterialsCount2(DisplayStateOption, DisplayStateNames)
```

```

System.int GetRenderMaterialsCount2( 
   System.int DisplayStateOption,
   System.object DisplayStateNames
)
```

```

System.int GetRenderMaterialsCount2( 
   System.int DisplayStateOption,
   System.Object^ DisplayStateNames
) 
```

#### Parameters

*DisplayStateOption*
:   Display states as defined in [swDisplayStateOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayStateOpts_e.html)

*DisplayStateNames*
:   Array of display state names

#### Return Value

Number of [appearances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)

Example

[Add and Delete Appearances from Specific Display States (VBA)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm)  
[Add and Delete Appearances from Specific Display States (VB.NET)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm)  
[Add and Delete Appearances from Specific Display States (C#)](Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::UpdateRenderMaterialsInSceneGraph Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateRenderMaterialsInSceneGraph.md)  
[IModelDocExtension::GetRenderMaterials2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterials2.md)  
[IModelDocExtension::CreateRenderMaterial Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateRenderMaterial.md)
