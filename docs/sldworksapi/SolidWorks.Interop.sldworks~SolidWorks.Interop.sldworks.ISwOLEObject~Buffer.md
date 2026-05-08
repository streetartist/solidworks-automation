# Buffer Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Buffer`

Gets the data for this OLE object.
Gets the data for this OLE object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Buffer As System.Object
```

```

Dim instance As ISwOLEObject
Dim value As System.Object
 
value = instance.Buffer
```

```

System.object Buffer {get;}
```

```

property System.Object^ Buffer {
   System.Object^ get();
}
```

#### Property Value

Array of buffer data

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md)  
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.md)  
[ISwOLEObject::IGetBuffer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IGetBuffer.md)  
[ISwOLEObject::BufferSize Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~BufferSize.md)
