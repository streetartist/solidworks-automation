# Clsid Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Clsid`

Gets the class ID of this OLE object.
Gets the class ID of this OLE object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Clsid As System.String
```

```

Dim instance As ISwOLEObject
Dim value As System.String
 
value = instance.Clsid
```

```

System.string Clsid {get;}
```

```

property System.String^ Clsid {
   System.String^ get();
}
```

#### Property Value

Either an alpha-numeric string or the class ID of the host application

Example

See the [ISwOLEObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md)  
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.md)
