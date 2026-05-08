# IGetFlattenSheetMetalPersistReference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetFlattenSheetMetalPersistReference`

Gets a byte array of persistent reference IDs for the specified entity (a face, edge, or vertex) in a flattened sheet metal part.
Gets a byte array of persistent reference IDs for the specified entity (a face, edge, or vertex) in a flattened sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFlattenSheetMetalPersistReference( _
   ByVal DispObj As System.Object, _
   ByVal Count As System.Integer _
) As System.Byte
```

```

Dim instance As IModelDocExtension
Dim DispObj As System.Object
Dim Count As System.Integer
Dim value As System.Byte
 
value = instance.IGetFlattenSheetMetalPersistReference(DispObj, Count)
```

```

System.byte IGetFlattenSheetMetalPersistReference( 
   System.object DispObj,
   System.int Count
)
```

```

System.byte IGetFlattenSheetMetalPersistReference( 
   System.Object^ DispObj,
   System.int Count
) 
```

#### Parameters

*DispObj*
:   Entity (a face, edge, or vertex) in the flattened sheet metal part whose persistent reference IDs you want

*Count*
:   Number of persistent reference IDs

#### Return Value

- in-process, unmanaged C++: Pointer to a byte array of persistent reference IDs

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The sheet metal part must be in the flattened state when this method is called. You can pass the byte array of persistent reference IDs to [IModelDocExtension::GetSheetMetalObjectsByPersistReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSheetMetalObjectsByPersistReference.md) or [IModelDocExtension::IGetSheetMetalObjectsByPersistReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSheetMetalObjectsByPersistReference.md), which gets the objects that correspond to the persistent reference IDs in the folded configuration of the sheet metal part.

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetFlattenSheetMetalPersistReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetFlattenSheetMetalPersistReference.md)  
[IModelDocExtension::GetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.md)  
[IModelDocExtension::GetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.md)  
[IModelDocExtension::GetPersistReferenceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount.md)  
[IModelDocExtension::IGetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.md)  
[IModelDocExtension::IGetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.md)
