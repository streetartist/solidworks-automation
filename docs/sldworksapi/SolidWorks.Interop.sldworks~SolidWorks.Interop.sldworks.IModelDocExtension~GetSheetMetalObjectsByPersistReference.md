# GetSheetMetalObjectsByPersistReference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSheetMetalObjectsByPersistReference`

Gets the objects in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part.
Gets the objects in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSheetMetalObjectsByPersistReference( _
   ByVal PersistId As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim PersistId As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object
 
value = instance.GetSheetMetalObjectsByPersistReference(PersistId, ErrorCode)
```

```

System.object GetSheetMetalObjectsByPersistReference( 
   System.object PersistId,
   out System.int ErrorCode
)
```

```

System.Object^ GetSheetMetalObjectsByPersistReference( 
   System.Object^ PersistId,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*PersistId*
:   Persistent reference IDs returned by [IModelDocExtension::GetFlattenSheetMetalPersistReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetFlattenSheetMetalPersistReference.md) or [IModelDocExtension::IGetFlattenSheetMetalPersistReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetFlattenSheetMetalPersistReference.md)

*ErrorCode*
:   Error as defined by [swPersistReferencedObjectStates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPersistReferencedObjectStates_e.html)

#### Return Value

Objects in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part

Remarks

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

Example

[Set and Get Sheet Metal Part's Persistent Reference IDs (C#)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_CSharp.htm)  
[Set and Get Sheet Metal Part's Persistent Reference IDS (VB.NET)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VBNET.htm)  
[Set and Get Sheet Metal Part's Persistent Reference IDs (VBA)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::IGetSheetMetalObjectsByPersistReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSheetMetalObjectsByPersistReference.md)  
[IModelDocExtension::GetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.md)  
[IModelDocExtension::GetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.md)  
[IModelDocExtension::GetPersistReferenceCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount3.md)  
[IModelDocExtension::IGetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.md)  
[IModelDocExtension::IGetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.md)
