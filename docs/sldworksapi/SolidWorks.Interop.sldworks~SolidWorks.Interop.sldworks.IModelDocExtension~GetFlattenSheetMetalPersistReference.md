# GetFlattenSheetMetalPersistReference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetFlattenSheetMetalPersistReference`

Gets a byte array of persistent reference IDs for the specified entity (a face, edge, or vertex) in a flattened sheet metal part.
Gets a byte array of persistent reference IDs for the specified entity (a face, edge, or vertex) in a flattened sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFlattenSheetMetalPersistReference( _
   ByVal DispObj As System.Object _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim DispObj As System.Object
Dim value As System.Object
 
value = instance.GetFlattenSheetMetalPersistReference(DispObj)
```

```

System.object GetFlattenSheetMetalPersistReference( 
   System.object DispObj
)
```

```

System.Object^ GetFlattenSheetMetalPersistReference( 
   System.Object^ DispObj
) 
```

#### Parameters

*DispObj*
:   Entity (a face, edge, or vertex) in the flattened sheet metal part whose persistent reference IDs you want

#### Return Value

Byte array of persistent reference IDs

Remarks

The sheet metal part must be in the flattened state when this method is called. You can then pass the byte array of persistent reference IDs to [IModelDocExtension::GetSheetMetalObjectsByPersistReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSheetMetalObjectsByPersistReference.md) or [IModelDocExtension::IGetSheetMetalObjectsByPersistReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSheetMetalObjectsByPersistReference.md), which gets the objects that correspond to the persistent reference IDs in the folded configuration of the sheet metal part.

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

Example

[Set and Get Sheet Metal Part's Persistent Reference IDs (C#)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_CSharp.htm)  
[Set and Get Sheet Metal Part's Persistent Reference IDs (VB.NET)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VBNET.htm)  
[Set and Get Sheet Metal Part's Persistent Reference IDs (VBA)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.md)  
[IModelDocExtension::GetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.md)  
[IModelDocExtension::GetPersistReferenceCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount3.md)  
[IModelDocExtension::IGetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.md)  
[IModelDocExtension::IGetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.md)
