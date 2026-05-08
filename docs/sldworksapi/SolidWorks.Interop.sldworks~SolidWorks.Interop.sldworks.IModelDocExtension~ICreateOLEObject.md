# ICreateOLEObject Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ICreateOLEObject`

Creates an OLE object on the active document.
Creates an OLE object on the active document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateOLEObject( _
   ByVal Aspect As System.Integer, _
   ByRef Position As System.Double, _
   ByVal ByteCount As System.Integer, _
   ByRef Buffer As System.Byte, _
   ByRef ErrorCode As System.Integer _
) As SwOLEObject
```

```

Dim instance As IModelDocExtension
Dim Aspect As System.Integer
Dim Position As System.Double
Dim ByteCount As System.Integer
Dim Buffer As System.Byte
Dim ErrorCode As System.Integer
Dim value As SwOLEObject
 
value = instance.ICreateOLEObject(Aspect, Position, ByteCount, Buffer, ErrorCode)
```

```

SwOLEObject ICreateOLEObject( 
   System.int Aspect,
   ref System.double Position,
   System.int ByteCount,
   ref System.byte Buffer,
   out System.int ErrorCode
)
```

```

SwOLEObject^ ICreateOLEObject( 
   System.int Aspect,
   System.double% Position,
   System.int ByteCount,
   System.byte% Buffer,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*Aspect*
:   Viewing aspect of the OLE object as defined in the DVASPECT enumeration (see **Remarks**)

*Position*
:   Top-left and bottom-right positions (see Remarks)

*ByteCount*
:   Number of bytes

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
[IModelDocExtension::CreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateOLEObject.md)  
[IModelDocExtension::GetOLEObjectCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjectCount.md)  
[IModelDocExtension::GetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjects.md)  
[IModelDocExtension::IGetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetOLEObjects.md)  
[IModelDocExtension::InsertObjectFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertObjectFromFile.md)
