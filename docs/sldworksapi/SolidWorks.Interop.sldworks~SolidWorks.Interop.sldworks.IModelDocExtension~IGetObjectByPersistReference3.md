# IGetObjectByPersistReference3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3`

Gets the object assigned to the specified persistent reference ID.
Gets the object assigned to the specified persistent reference ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetObjectByPersistReference3( _
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
 
value = instance.IGetObjectByPersistReference3(Count, PersistId, ErrorCode)
```

```

System.object IGetObjectByPersistReference3( 
   System.int Count,
   ref System.byte PersistId,
   out System.int ErrorCode
)
```

```

System.Object^ IGetObjectByPersistReference3( 
   System.int Count,
   System.byte% PersistId,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*Count*
:   Size of persistent reference ID (see **Remarks**)

*PersistId*
:   Object's persistent reference ID (see Remarks)

*ErrorCode*
:   Success or error code as defined by [swPersistReferencedObjectStates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPersistReferencedObjectStates_e.html) (see Remarks)

#### Return Value

Object (see **Remarks**)

Remarks

A persistent reference ID is related to a model. It is portable and can be saved within the model or in other places. Some persistent reference IDs are general to all models and can be instantiated from all models. Your application must handle persistent reference IDs and their relationships among models.

Before calling this method:

1. Call [IModelDocExtension::GetPersistentReferenceCount3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount3.md) to determine the size of the persistent reference ID.
2. Call [IModelDocExtension::IGetPersistReference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.md) to get the object's persistent reference ID.

The swPersistReferencedObject\_Suppressed and swPersistReferencedObject\_Deleted enumerators only apply to references of topological entities.

IModelDocExtension::GetObjectByPersistReference3 was designed to return the base class of a feature to take advantage of the base feature class functionality. Objects returned by IModelDocExtension::GetObjectByPersistReference3 are often features, including [IConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md), [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), and [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md) objects. You must first obtain a reference to a feature, and then use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to get the original object.

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.md)  
[IModelDocExtension::GetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.md)  
[IModelDocExtension::IsSamePersistentID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsSamePersistentID.md)
