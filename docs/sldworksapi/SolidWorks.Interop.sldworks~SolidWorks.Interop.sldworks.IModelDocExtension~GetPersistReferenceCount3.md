# GetPersistReferenceCount3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount3`

Gets the size of the persistent reference ID assigned to the selected object in this model document.
Gets the size of the persistent reference ID assigned to the selected object in this model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPersistReferenceCount3( _
   ByVal DispObj As System.Object _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim DispObj As System.Object
Dim value As System.Integer
 
value = instance.GetPersistReferenceCount3(DispObj)
```

```

System.int GetPersistReferenceCount3( 
   System.object DispObj
)
```

```

System.int GetPersistReferenceCount3( 
   System.Object^ DispObj
) 
```

#### Parameters

*DispObj*
:   Selected object

#### Return Value

Size of that object's persistent reference ID

Remarks

Persistent reference ID values obtained using the now obsolete IModelDocExtension::GetPersistReference and its related obsolete methods, IModelDocExtension::GetPersistReferenceCount and IModelDocExtension::GetObjectByPersistReference2, are not compatible with persistent reference IDs obtained using [IModelDocExtension::GetPersistReference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.md) or [IModelDocExtension::IGetPersistReference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.md) and its related methods, [IModelDocExtension::GetObjectByPersistReference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.md) or [IModelDocExtension::IGetObjectByPersistReference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.md) and this method.

**IMPORTANT:** SOLIDWORKS recommends not using this method with IModelDocExtension::IGetPersistReference3 because when these methods are used together, you will experience a significant decrease in performance.

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

Example

[Get Object's Persistent Reference ID (C++)](Get_Object_s_Persistent_Reference_ID_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
