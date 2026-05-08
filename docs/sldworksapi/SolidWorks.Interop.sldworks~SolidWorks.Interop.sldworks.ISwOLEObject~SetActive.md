# SetActive Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~SetActive`

Activates or deactivates the OLE object.
Activates or deactivates the OLE object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetActive( _
   ByVal Active As System.Boolean _
) As System.Object
```

```

Dim instance As ISwOLEObject
Dim Active As System.Boolean
Dim value As System.Object
 
value = instance.SetActive(Active)
```

```

System.object SetActive( 
   System.bool Active
)
```

```

System.Object^ SetActive( 
   System.bool Active
) 
```

#### Parameters

*Active*
:   True activates the OLE object, false deactivates the OLE object

#### Return Value

True gets the activated OLE object, false returns null

Example

[Activate OLE Object (VBA)](Activate_OLE_Object_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md)  
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.md)
