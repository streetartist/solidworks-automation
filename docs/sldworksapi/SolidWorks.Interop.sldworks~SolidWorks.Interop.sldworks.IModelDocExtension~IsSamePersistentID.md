# IsSamePersistentID Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsSamePersistentID`

Gets whether the two specified objects have the same persistent reference IDs.
Gets whether the two specified objects have the same persistent reference IDs.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsSamePersistentID( _
   ByVal PersistentID1 As System.Object, _
   ByVal PersistentID2 As System.Object _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim PersistentID1 As System.Object
Dim PersistentID2 As System.Object
Dim value As System.Integer
 
value = instance.IsSamePersistentID(PersistentID1, PersistentID2)
```

```

System.int IsSamePersistentID( 
   System.object PersistentID1,
   System.object PersistentID2
)
```

```

System.int IsSamePersistentID( 
   System.Object^ PersistentID1,
   System.Object^ PersistentID2
) 
```

#### Parameters

*PersistentID1*
:   Object

*PersistentID2*
:   Object

#### Return Value

Object equality as defined by [swObjectEquality](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swObjectEquality.html)

Remarks

Use this method when your application is passed two entities that your application did not select, and your application needs to know if they are the same entity.

Example

[Compare Selected Objects and Their Persistent Reference IDs (VB.NET)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_VBNET.htm)  
[Compare Selected Objects and Their Persistent Reference IDs (VBA)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_VB.htm)  
[Compare Selected Objects and Their Persistent Reference IDs (C#)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.md)  
[IModelDocExtension::GetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.md)  
[IModelDocExtension::GetPersistReferenceCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount3.md)  
[IModelDocExtension::IGetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.md)  
[IModelDocExtension::IGetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.md)  
[ISldWorks::IsSame Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsSame.md)
