# FileName Property (ISwOLEObject)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~FileName`

Gets the path and name of the external file to which this OLE object is linked.
Gets the path and name of the external file to which this OLE object is linked.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property FileName As System.String
```

```

Dim instance As ISwOLEObject
Dim value As System.String
 
value = instance.FileName
```

```

System.string FileName {get;}
```

```

property System.String^ FileName {
   System.String^ get();
}
```

#### Property Value

Path and name of external file to which this OLE object is linked

Example

See the [ISwOLEObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md)  
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.md)  
[ISwOLEObject::IsLinked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IsLinked.md)
