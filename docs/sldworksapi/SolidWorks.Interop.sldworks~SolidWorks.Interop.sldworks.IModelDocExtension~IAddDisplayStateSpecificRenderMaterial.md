# IAddDisplayStateSpecificRenderMaterial Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IAddDisplayStateSpecificRenderMaterial`

Adds the specified material to the specified display states in the active configuration and returns the IDs assigned to that material.
Adds the specified material to the specified display states in the active configuration and returns the IDs assigned to that material.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddDisplayStateSpecificRenderMaterial( _
   ByVal PRenderMaterial As RenderMaterial, _
   ByVal DisplayStateOption As System.Integer, _
   ByVal DisplayStateCount As System.Integer, _
   ByRef DisplayStateNames As System.String, _
   ByRef PWMaterialId1 As System.Integer, _
   ByRef PWMaterialId2 As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim PRenderMaterial As RenderMaterial
Dim DisplayStateOption As System.Integer
Dim DisplayStateCount As System.Integer
Dim DisplayStateNames As System.String
Dim PWMaterialId1 As System.Integer
Dim PWMaterialId2 As System.Integer
Dim value As System.Boolean
 
value = instance.IAddDisplayStateSpecificRenderMaterial(PRenderMaterial, DisplayStateOption, DisplayStateCount, DisplayStateNames, PWMaterialId1, PWMaterialId2)
```

```

System.bool IAddDisplayStateSpecificRenderMaterial( 
   RenderMaterial PRenderMaterial,
   System.int DisplayStateOption,
   System.int DisplayStateCount,
   ref System.string DisplayStateNames,
   out System.int PWMaterialId1,
   out System.int PWMaterialId2
)
```

```

System.bool IAddDisplayStateSpecificRenderMaterial( 
   RenderMaterial^ PRenderMaterial,
   System.int DisplayStateOption,
   System.int DisplayStateCount,
   System.String^% DisplayStateNames,
   [Out] System.int PWMaterialId1,
   [Out] System.int PWMaterialId2
) 
```

#### Parameters

*PRenderMaterial*
:   [Material](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md) to add

*DisplayStateOption*
:   Display states as defined in [swDisplayStateOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayStateOpts_e.html)

*DisplayStateCount*
:   Number of display states (see **Remarks**)

*DisplayStateNames*
:   - in-process, unmanaged C++: Pointer to an array of the names of the display states to which to add material
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*PWMaterialId1*
:   First ID of material

*PWMaterialId2*
:   Second ID of material

#### Return Value

True if material is added, false if not

Remarks

Before calling this method, call [IConfiguration::GetDisplayStatesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.md) to get DisplayStateCount.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial.md)  
[IModelDocExtension::AddDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDisplayStateSpecificRenderMaterial.md)  
[IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDisplayStateSpecificRenderMaterial.md)  
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)
