# CreateOLEObject Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateOLEObject`

Creates an OLE object on the active document.
Creates an OLE object on the active document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateOLEObject( _
   ByVal Aspect As System.Integer, _
   ByVal Position As System.Object, _
   ByVal Buffer As System.Object, _
   ByRef ErrorCode As System.Integer _
) As SwOLEObject
```

```

Dim instance As IModelDocExtension
Dim Aspect As System.Integer
Dim Position As System.Object
Dim Buffer As System.Object
Dim ErrorCode As System.Integer
Dim value As SwOLEObject
 
value = instance.CreateOLEObject(Aspect, Position, Buffer, ErrorCode)
```

```

SwOLEObject CreateOLEObject( 
   System.int Aspect,
   System.object Position,
   System.object Buffer,
   out System.int ErrorCode
)
```

```

SwOLEObject^ CreateOLEObject( 
   System.int Aspect,
   System.Object^ Position,
   System.Object^ Buffer,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*Aspect*
:   Viewing aspect of the OLE object as defined in the DVASPECT enumeration (see **Remarks**)

*Position*
:   Top-left and bottom-right positions (see Remarks)

*Buffer*
:   Data for the OLE object (see Remarks)

*ErrorCode*
:   0 if True or 1 if false

#### Return Value

[OLE object](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md)

Remarks

|  |  |
| --- | --- |
| **Argument** | **Information** |
| Aspect | Uses the DVASPECT enumeration, which has the following values:   - DVASPECT\_CONTENT = 1 - DVASPECT\_THUMBNAIL = 2 - DVASPECT\_ICON = 4 - DVASPECT\_DOCPRINT = 8   See the MSDN documentation for details about the DVASPECT enumeration. |
| Position | Specify:   - Sheet coordinates for drawings. - Screen pixel coordinates for parts and assemblies. |
| Buffer | See [ISwOLEObject::Buffer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Buffer.md) or specify [ISwOLEObject::IGetBuffer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IGetBuffer.md)  - or -  Get the data from your own OLE object.  The data is in the format obtained from the Microsoft MFC object COleClientItem using the GetHGlobalFromILockBytes. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetOLEObjectCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjectCount.md)  
[IModelDocExtension::GetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjects.md)  
[IModelDocExtension::InsertObjectFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertObjectFromFile.md)  
[IModelDocExtension::ICreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ICreateOLEObject.md)  
[IModelDocExtension::IGetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetOLEObjects.md)
