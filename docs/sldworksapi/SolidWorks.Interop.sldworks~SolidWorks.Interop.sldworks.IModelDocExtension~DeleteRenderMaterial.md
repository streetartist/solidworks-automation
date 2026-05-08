# DeleteRenderMaterial Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteRenderMaterial`

Not supported in SOLIDWORKS 2011 and later. Superseded by IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial and IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial.
Not supported in SOLIDWORKS 2011 and later. Superseded by [IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDisplayStateSpecificRenderMaterial.md) and [IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteRenderMaterial( _
   ByVal PwMaterialId As System.Integer, _
   ByVal BReassignIdsAndInvalidate As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim PwMaterialId As System.Integer
Dim BReassignIdsAndInvalidate As System.Boolean
Dim value As System.Boolean
 
value = instance.DeleteRenderMaterial(PwMaterialId, BReassignIdsAndInvalidate)
```

```

System.bool DeleteRenderMaterial( 
   System.int PwMaterialId,
   System.bool BReassignIdsAndInvalidate
)
```

```

System.bool DeleteRenderMaterial( 
   System.int PwMaterialId,
   System.bool BReassignIdsAndInvalidate
) 
```

#### Parameters

*PwMaterialId*
:   Appearance ID

*BReassignIdsAndInvalidate*
:   True if the appearance IDs are reassigned and this appearance ID is invalidated, false if not

#### Return Value

True if the appearance is deleted, false if not

Remarks

By default, appearance IDs are persistent, which means if three appearances (IDs 1, 2, and 3) were applied to the model, and you removed appearance ID 2, then the remaining appearance IDs are 1 and 3. However, if you set BReassignIdsAndInvalidate to true, then appearance ID 2 is invalidated and appearance ID 3 becomes appearance ID 2.

To get the IDs of all of the appearances applied to this model document, call [IModelDocExtension::GetRenderMaterialsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
