# IsLinked Property (ISwOLEObject)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IsLinked`

Gets whether the OLE objects are linked to external files or not.
Gets whether the OLE objects are linked to external files or not.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IsLinked As System.Boolean
```

```

Dim instance As ISwOLEObject
Dim value As System.Boolean
 
value = instance.IsLinked
```

```

System.bool IsLinked {get;}
```

```

property System.bool IsLinked {
   System.bool get();
}
```

#### Property Value

True if the OLE objects are linked to external files, false if they are embedded

Example

See the [ISwOLEObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md) examples.

Example

[Determine If OLE Objects are Linked or Embedded (VBA)](Determine_if_OLE_Objects_are_Linked_or_Embedded_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md)  
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.md)  
[ISwOLEObject::FileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~FileName.md)
