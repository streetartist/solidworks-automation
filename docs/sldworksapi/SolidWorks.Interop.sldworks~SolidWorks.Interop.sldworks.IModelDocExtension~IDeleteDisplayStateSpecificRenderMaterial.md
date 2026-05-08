# IDeleteDisplayStateSpecificRenderMaterial Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial`

Deletes the specified materials, using the IDs of the materials, from the active configuration.
Deletes the specified materials, using the IDs of the materials, from the active configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IDeleteDisplayStateSpecificRenderMaterial( _
   ByVal IdCount As System.Integer, _
   ByRef PWMaterialId1 As System.Integer, _
   ByRef PWMaterialId2 As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim IdCount As System.Integer
Dim PWMaterialId1 As System.Integer
Dim PWMaterialId2 As System.Integer
Dim value As System.Boolean
 
value = instance.IDeleteDisplayStateSpecificRenderMaterial(IdCount, PWMaterialId1, PWMaterialId2)
```

```

System.bool IDeleteDisplayStateSpecificRenderMaterial( 
   System.int IdCount,
   ref System.int PWMaterialId1,
   ref System.int PWMaterialId2
)
```

```

System.bool IDeleteDisplayStateSpecificRenderMaterial( 
   System.int IdCount,
   System.int% PWMaterialId1,
   System.int% PWMaterialId2
) 
```

#### Parameters

*IdCount*
:   Number of material IDs

*PWMaterialId1*
:   - in-process, unmanaged C++: Pointer to an array of the first IDs of the material to delete

    :   - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*PWMaterialId2*
:   - in-process, unmanaged C++: Pointer to an array of the second IDs of the material to delete

    :   - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if the materials are deleted, false if not

Remarks

Before calling this method, call:

- [IModelDocExtension::GetRenderMaterialsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount.md) to get the value for IdCount.
- [IRenderMaterial::GetMaterialIds](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetMaterialIds.md) to the get the values for PWMaterialId1 and PWMaterialId2, the IDs of the materials added to the model.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::IAddDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IAddDisplayStateSpecificRenderMaterial.md)  
[IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDisplayStateSpecificRenderMaterial.md)  
[IModelDocExtension::AddDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDisplayStateSpecificRenderMaterial.md)  
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)
