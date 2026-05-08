# GetPersistReference3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3`

Gets the persistent reference ID for the specified object in this model document.
Gets the persistent reference ID for the specified object in this model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPersistReference3( _
   ByVal DispObj As System.Object _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim DispObj As System.Object
Dim value As System.Object
 
value = instance.GetPersistReference3(DispObj)
```

```

System.object GetPersistReference3( 
   System.object DispObj
)
```

```

System.Object^ GetPersistReference3( 
   System.Object^ DispObj
) 
```

#### Parameters

*DispObj*
:   Object

#### Return Value

Array containing the persistent reference ID assigned to that object

Remarks

Persistent reference ID values obtained using the now obsolete IModelDocExtension::GetPersistReference and its related obsolete methods, IModelDocExtension::GetPersistReferenceCount and IModelDocExtension::GetObjectByPersistReference2, are not compatible with persistent reference IDs obtained using this method and its related methods, [IModelDocExtension::GetPersistReferenceCount3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount3.md) and [IModelDocExtension::GetObjectByPersistReference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.md) or [IModelDocExtension::IGetObjectByPersistReference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.md).

A persistent reference ID is related to a model. It is portable and can be saved within the model or in other places. Some persistent reference IDs are general to all models and can be instantiated from all models. Your application must handle persistent reference IDs and their relationships among models.

The internal representations of the return value array may change, possibly from rebuild to rebuild, or more likely, from one release of SOLIDWORKS to the next, but their usage in finding the correct entity will be consistent across rebuilds and SOLIDWORKS releases.

To compare the referenced entities, you could use the Visual Basic Is operator to find out if the entities are the same.

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

Example

[Check Faces for Faults (VBA)](Check_Faces_for_Faults_Example_VB.htm)  
[Use Persistent Reference (VBA)](Use_Persistent_Reference_Example_VB.htm)  
[Get Object's Persistent Reference ID (VBA)](Get_Object_s_Persistent_Reference_ID_Example_VB.htm)  
[Get Object's Persistent Reference ID (C++)](Get_Object_s_Persistent_Reference_ID_Example_CPlusPlus_COM.htm)  
[Compare Selected Objects and Their Persistent Reference IDs (C#)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_CSharp.htm)  
[Compare Selected Objects and Their Persistent Reference IDs (VB.NET)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_VBNET.htm)  
[Compare Selected Objects and Their Persistent Reference IDs (VBA)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::IGetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.md)  
[IModelDocExtension::IsSamePersistentID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsSamePersistentID.md)  
[IView::ReferencedConfigurationID Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfigurationID.md)
