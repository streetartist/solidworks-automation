# GetOLEObjects Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjects`

Get the OLE objects.
Get the OLE objects.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOLEObjects( _
   ByVal Options As System.Integer _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Options As System.Integer
Dim value As System.Object
 
value = instance.GetOLEObjects(Options)
```

```

System.object GetOLEObjects( 
   System.int Options
)
```

```

System.Object^ GetOLEObjects( 
   System.int Options
) 
```

#### Parameters

*Options*
:   Options as defined in [swOleObjectOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOleObjectOptions_e.html)

#### Return Value

Array of the [OLE objects](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md)

Example

[Determine if OLE Objects Are Linked or Embedded (VBA)](Determine_if_OLE_Objects_are_Linked_or_Embedded_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::CreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateOLEObject.md)  
[IModelDocExtension::GetOLEObjectCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjectCount.md)  
[IModelDocExtension::ICreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ICreateOLEObject.md)  
[IModelDocExtension::IGetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetOLEObjects.md)  
[IModelDocExtension::InsertObjectFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertObjectFromFile.md)
