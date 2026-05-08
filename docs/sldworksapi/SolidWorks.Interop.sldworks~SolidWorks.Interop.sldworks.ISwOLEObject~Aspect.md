# Aspect Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Aspect`

Gets the viewing aspect for this OLE object.
Gets the viewing aspect for this OLE object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Aspect As System.Integer
```

```

Dim instance As ISwOLEObject
Dim value As System.Integer
 
value = instance.Aspect
```

```

System.int Aspect {get;}
```

```

property System.int Aspect {
   System.int get();
}
```

#### Property Value

Viewing aspect as defined in the DVASPECT enumeration (see Remarks)

Remarks

The ViewingAspect argument uses the DVASPECT enumeration, which has the following values:

- DVASPECT\_CONTENT = 1
- DVASPECT\_THUMBNAIL = 2
- DVASPECT\_ICON = 4
- DVASPECT\_DOCPRINT = 8

See the MSDN documentation for additional details about the DVASPECT enumeration.

Example

See the [ISwOLEObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md)  
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.md)
