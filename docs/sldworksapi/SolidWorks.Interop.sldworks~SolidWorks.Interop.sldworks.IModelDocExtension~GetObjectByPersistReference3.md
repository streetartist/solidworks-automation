# GetObjectByPersistReference3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3`

Gets the object assigned to the specified persistent reference ID.
Gets the object assigned to the specified persistent reference ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetObjectByPersistReference3( _
   ByVal PersistId As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim PersistId As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object
 
value = instance.GetObjectByPersistReference3(PersistId, ErrorCode)
```

```

System.object GetObjectByPersistReference3( 
   System.object PersistId,
   out System.int ErrorCode
)
```

```

System.Object^ GetObjectByPersistReference3( 
   System.Object^ PersistId,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*PersistId*
:   Object's persistent reference ID (see Remarks)

*ErrorCode*
:   Success or error code as defined by [swPersistReferencedObjectStates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPersistReferencedObjectStates_e.html) (see Remarks)

#### Return Value

Object (see **Remarks**)

Remarks

A persistent reference ID is related to a model. It is portable and can be saved within the model or in other places. Some persistent reference IDs are general to all models and can be instantiated from all models. Your application must handle persistent reference IDs and their relationships among models.

Before calling this method, call [IModelDocExtension::GetPersistReference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.md) to get the object's persistent reference ID.

The swPersistReferencedObject\_Suppressed and swPersistReferencedObject\_Deleted enumerators only apply to references of topological entities.

IModelDocExtension::GetObjectByPersistReference3 was designed to return the base class of a feature to take advantage of the base feature class functionality. Objects returned by IModelDocExtension::GetObjectByPersistReference3 are often features, including [IConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md), [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), and [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md) objects. You must first obtain a reference to a feature, and then use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to get the original object.

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

Example

Sub main () 

    Set swApp = Application.SldWorks

    Set Doc = swApp.ActiveDoc  
    Set SelMgr = Doc.SelectionManager  
    If SelMgr.GetSelectedObjectCount(-1) = 0 Then Debug.Print "No selections found.": Exit Sub 

    Dim persistRef As Variant  
    Dim selObj As Object 

    Set selObj = SelMgr.GetSelectedObject6(1, -1)  
    persistRef = Doc.Extension.GetPersistReference3(selObj)  
    Debug.Print UBound(persistRef)  
    Set selObj = Nothing  
    Set selObj = Doc.Extension.GetObjectByPersistReference3(persistRef, longstatus)  
    Debug.Print (Not selObj Is Nothing) 

    Dim selConfig As Configuration  
    Set selConfig = selObj.GetSpecificFeature2 

End Sub

Example

[Get Object's Persistent Reference ID (VBA)](Get_Object_s_Persistent_Reference_ID_Example_VB.htm)  
[Use Persistent Reference (VBA)](Use_Persistent_Reference_Example_VB.htm)  
[Use Persistent Reference (VB.NET)](Use_Persistent_Reference_Example_VBNET.htm)  
[Use Persistent Reference (C#)](Use_Persistent_Reference_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::IModelDocExtension::IGetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.md)  
[IModelDocExtension::GetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.md)  
[IModelDocExtension::GetPersistReferenceCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount3.md)  
[IModelDocExtension::IsSamePersistentID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsSamePersistentID.md)  
[IView::ReferencedConfigurationID Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfigurationID.md)
