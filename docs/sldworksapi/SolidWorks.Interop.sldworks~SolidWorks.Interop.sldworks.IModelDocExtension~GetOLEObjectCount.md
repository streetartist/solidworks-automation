# GetOLEObjectCount Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjectCount`

Gets the number of OLE objects.
Gets the number of OLE objects.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOLEObjectCount( _
   ByVal Options As System.Integer _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim Options As System.Integer
Dim value As System.Integer
 
value = instance.GetOLEObjectCount(Options)
```

```

System.int GetOLEObjectCount( 
   System.int Options
)
```

```

System.int GetOLEObjectCount( 
   System.int Options
) 
```

#### Parameters

*Options*
:   Options as defined in [swOleObjectOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOleObjectOptions_e.html)

#### Return Value

Number of OLE objects

Remarks

Call this method before calling [IModelDocExtension::IGetOLEObjects](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetOLEObjects.md).

Example

[Determine if OLE Objects Are Linked or Embedded (VBA)](Determine_if_OLE_Objects_are_Linked_or_Embedded_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::CreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateOLEObject.md)  
[IModelDocExtension::GetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjects.md)  
[IModelDocExtension::ICreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ICreateOLEObject.md)  
[IModelDocExtension::IGetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetOLEObjects.md)  
[IModelDocExtension::InsertObjectFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertObjectFromFile.md)
