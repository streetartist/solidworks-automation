# Boundaries Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Boundaries`

Gets or sets the boundaries for this OLE object.
Gets or sets the boundaries for this OLE object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Boundaries As System.Object
```

```

Dim instance As ISwOLEObject
Dim value As System.Object
 
instance.Boundaries = value
 
value = instance.Boundaries
```

```

System.object Boundaries {get; set;}
```

```

property System.Object^ Boundaries {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of these coordinates:

- Drawings: sheet coordinates
- Parts or assemblies: screen pixel coordinates

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md)  
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.md)  
[ISwOLEObject::IGetBoundaries Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IGetBoundaries.md)  
[ISwOLEObject::ISetBoundaries Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~ISetBoundaries.md)
