# InsertObjectFromFile Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertObjectFromFile`

Inserts an OLE object from a file.
Inserts an OLE object from a file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertObjectFromFile( _
   ByVal FilePath As System.String, _
   ByVal CreateLink As System.Boolean, _
   ByVal Aspect As System.Integer, _
   ByVal XPos As System.Double, _
   ByVal YPos As System.Double, _
   ByVal ZPos As System.Double _
) As SwOLEObject
```

```

Dim instance As IModelDocExtension
Dim FilePath As System.String
Dim CreateLink As System.Boolean
Dim Aspect As System.Integer
Dim XPos As System.Double
Dim YPos As System.Double
Dim ZPos As System.Double
Dim value As SwOLEObject
 
value = instance.InsertObjectFromFile(FilePath, CreateLink, Aspect, XPos, YPos, ZPos)
```

```

SwOLEObject InsertObjectFromFile( 
   System.string FilePath,
   System.bool CreateLink,
   System.int Aspect,
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

```

SwOLEObject^ InsertObjectFromFile( 
   System.String^ FilePath,
   System.bool CreateLink,
   System.int Aspect,
   System.double XPos,
   System.double YPos,
   System.double ZPos
) 
```

#### Parameters

*FilePath*
:   Path and filename for the OLE object file

*CreateLink*
:   True to create an external link to the OLE object file, false to embed the OLE object on the document

*Aspect*
:   Viewing aspect of the object as defined in the DVASPECT enumeration (see **Remarks**)

*XPos*
:   x coordinate for the OLE object

*YPos*
:   y coordinate for the OLE object

*ZPos*
:   z coordinate for the OLE object

#### Return Value

Newly inserted [object](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md)

Remarks

Currently, only the drawing documents use the x,y,z coordinate position. Part and assembly documents place the inserted object at the upper-right corner of the model view.

The aspect argument uses the DVASPECT enumeration, which has the following values:

- DVASPECT\_CONTENT = 1
- DVASPECT\_THUMBNAIL = 2
- DVASPECT\_ICON = 4
- DVASPECT\_DOCPRINT = 8

See the MSDN documentation for additional details about the DVASPECT enumeration.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::CreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateOLEObject.md)  
[IModelDocExtension::GetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjects.md)  
[IModelDocExtension::GetOLEObjectCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjectCount.md)  
[IModelDocExtension::ICreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ICreateOLEObject.md)  
[IModelDocExtension::IGetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetOLEObjects.md)
