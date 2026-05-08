# Select Method (ISwOLEObject)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Select`

Selects an OLE object.
Selects an OLE object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select( _
   ByVal Append As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISwOLEObject
Dim Append As System.Boolean
Dim value As System.Boolean
 
value = instance.Select(Append)
```

```

System.bool Select( 
   System.bool Append
)
```

```

System.bool Select( 
   System.bool Append
) 
```

#### Parameters

*Append*
:   True appends the OLE object to the selection list, false replaces the selection list with this OLE object

#### Return Value

True if the OLE object is selected, false if it is not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md)  
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.md)
