# IGetSheetMetalObjectsByPersistReference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSheetMetalObjectsByPersistReference`

Gets the object, or objects, in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part.
Gets the object, or objects, in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSheetMetalObjectsByPersistReference( _
   ByVal Count As System.Integer, _
   ByRef PersistId As System.Byte, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Count As System.Integer
Dim PersistId As System.Byte
Dim ErrorCode As System.Integer
Dim value As System.Object
 
value = instance.IGetSheetMetalObjectsByPersistReference(Count, PersistId, ErrorCode)
```

```

System.object IGetSheetMetalObjectsByPersistReference( 
   System.int Count,
   ref System.byte PersistId,
   out System.int ErrorCode
)
```

```

System.Object^ IGetSheetMetalObjectsByPersistReference( 
   System.int Count,
   System.byte% PersistId,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*Count*
:   Number of persistent reference IDs

*PersistId*
:   Persistent reference IDs returned by [IModelDocExtension::GetFlattenSheetMetalPersistReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetFlattenSheetMetalPersistReference.md) or [IModelDocExtension::IGetFlattenSheetMetalPersistReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetFlattenSheetMetalPersistReference.md)

*ErrorCode*
:   Error as defined by [swPersistReferencedObjectStates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPersistReferencedObjectStates_e.html)

#### Return Value

- in-process, unmanaged C++: Pointer to an array of objects in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetSheetMetalObjectsByPersistReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSheetMetalObjectsByPersistReference.md)  
[IModelDocExtension::GetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.md)  
[IModelDocExtension::GetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.md)  
[IModelDocExtension::GetPersistReferenceCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount3.md)  
[IModelDocExtension::IGetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.md)  
[IModelDocExtension::IGetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.md)
