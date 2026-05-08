# DeleteDisplayStateSpecificRenderMaterial Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDisplayStateSpecificRenderMaterial`

Deletes the specified appearances, using the IDs of the appearances, from the active configuration.
Deletes the specified appearances, using the IDs of the appearances, from the active configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteDisplayStateSpecificRenderMaterial( _
   ByVal PWMaterialId1 As System.Object, _
   ByVal PWMaterialId2 As System.Object _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim PWMaterialId1 As System.Object
Dim PWMaterialId2 As System.Object
Dim value As System.Boolean
 
value = instance.DeleteDisplayStateSpecificRenderMaterial(PWMaterialId1, PWMaterialId2)
```

```

System.bool DeleteDisplayStateSpecificRenderMaterial( 
   System.object PWMaterialId1,
   System.object PWMaterialId2
)
```

```

System.bool DeleteDisplayStateSpecificRenderMaterial( 
   System.Object^ PWMaterialId1,
   System.Object^ PWMaterialId2
) 
```

#### Parameters

*PWMaterialId1*
:   :   Array of the first IDs of the appearances to delete

*PWMaterialId2*
:   :   Array of the second IDs of the appearance to delete

#### Return Value

True if the appearances are deleted, false if not

Remarks

Call [IRenderMaterial::GetMaterialIds](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetMaterialIds.md) to the get IDs of the appearances added to the model, then call IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial to delete the appearances.

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
[IModelDocExtension::AddDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDisplayStateSpecificRenderMaterial.md)  
[IModelDocExtension::IAddDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IAddDisplayStateSpecificRenderMaterial.md)  
[IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial.md)  
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)
