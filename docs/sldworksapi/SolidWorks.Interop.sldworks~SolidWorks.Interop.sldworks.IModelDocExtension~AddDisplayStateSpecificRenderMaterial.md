# AddDisplayStateSpecificRenderMaterial Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDisplayStateSpecificRenderMaterial`

Adds the specified appearance to the specified display states in the active configuration and returns the IDs assigned to that appearance.
Adds the specified appearance to the specified display states in the active configuration and returns the IDs assigned to that appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddDisplayStateSpecificRenderMaterial( _
   ByVal PRenderMaterial As RenderMaterial, _
   ByVal DisplayStateOption As System.Integer, _
   ByVal DisplayStateNames As System.Object, _
   ByRef PWMaterialId1 As System.Integer, _
   ByRef PWMaterialId2 As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim PRenderMaterial As RenderMaterial
Dim DisplayStateOption As System.Integer
Dim DisplayStateNames As System.Object
Dim PWMaterialId1 As System.Integer
Dim PWMaterialId2 As System.Integer
Dim value As System.Boolean
 
value = instance.AddDisplayStateSpecificRenderMaterial(PRenderMaterial, DisplayStateOption, DisplayStateNames, PWMaterialId1, PWMaterialId2)
```

```

System.bool AddDisplayStateSpecificRenderMaterial( 
   RenderMaterial PRenderMaterial,
   System.int DisplayStateOption,
   System.object DisplayStateNames,
   out System.int PWMaterialId1,
   out System.int PWMaterialId2
)
```

```

System.bool AddDisplayStateSpecificRenderMaterial( 
   RenderMaterial^ PRenderMaterial,
   System.int DisplayStateOption,
   System.Object^ DisplayStateNames,
   [Out] System.int PWMaterialId1,
   [Out] System.int PWMaterialId2
) 
```

#### Parameters

*PRenderMaterial*
:   [Appearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md) to add

*DisplayStateOption*
:   Display states as defined in [swDisplayStateOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayStateOpts_e.html)

*DisplayStateNames*
:   Names of display states to which to add the appearance

*PWMaterialId1*
:   First ID of appearance

*PWMaterialId2*
:   Second ID of appearance

#### Return Value

True if appearance is added, false if not

Example

[Add and Delete Appearances from Specific Display States (C#)](Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm)  
[Add and Delete Appearances from Specific Display States (VB.NET)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm)  
[Add and Delete Appearances from Specific Display States (VBA)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDisplayStateSpecificRenderMaterial.md)  
[IModelDocExtension::IAddDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IAddDisplayStateSpecificRenderMaterial.md)  
[IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial.md)  
[IConfiguration::CreateDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.md)  
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)
