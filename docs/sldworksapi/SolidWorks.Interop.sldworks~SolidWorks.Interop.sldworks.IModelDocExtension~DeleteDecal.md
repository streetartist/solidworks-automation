# DeleteDecal Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDecal`

Removes the specified decal from this model.
Removes the specified decal from this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteDecal( _
   ByVal DecalID As System.Integer, _
   ByVal BReassignIdsAndInvalidate As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim DecalID As System.Integer
Dim BReassignIdsAndInvalidate As System.Boolean
Dim value As System.Boolean
 
value = instance.DeleteDecal(DecalID, BReassignIdsAndInvalidate)
```

```

System.bool DeleteDecal( 
   System.int DecalID,
   System.bool BReassignIdsAndInvalidate
)
```

```

System.bool DeleteDecal( 
   System.int DecalID,
   System.bool BReassignIdsAndInvalidate
) 
```

#### Parameters

*DecalID*
:   [Decal ID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~DecalID.md)

*BReassignIdsAndInvalidate*
:   True if the decal IDs are reassigned and this decal ID is invalidated, false if not

#### Return Value

True if the decal is removed from the model, false if not

Remarks

By default, decal IDs are persistent, which means if three decals (IDs 1, 2, and 3) were applied to the model, and you removed decal ID 2, then the remaining decal IDs are 1 and 3. However, if you set BReassignIdsAndInvalidate to true, then decal ID 2 is invalidated and decal ID 3 becomes decal ID 2.

Example

[Delete Decal (VBA)](Delete_Decal_Example_VB.htm)  
[Delete Decal (VB.NET)](Delete_Decal_Example_VBNET.htm)  
[Delete Decal (C#)](Delete_Decal_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.md)  
[IModelDocExtension::AddDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDecal.md)  
[IModelDocExtension::CreateDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateDecal.md)  
[IModelDocExtension::DeleteAllDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAllDecals.md)  
[IModelDocExtension::GetDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecal.md)  
[IModelDocExtension::GetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecals.md)  
[IModelDocExtension::GetDecalsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecalsCount.md)  
[IModelDocExtension::HideDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HideDecal.md)  
[IModelDocExtension::IGetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetDecals.md)  
[IModelDocExtension::MoveDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MoveDecal.md)  
[IModelDocExtension::ReverseDecalsOrder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReverseDecalsOrder.md)
