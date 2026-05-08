# DeSelectByID Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeSelectByID`

Removes the selected object from the selection list.
Removes the selected object from the selection list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeSelectByID( _
   ByVal SelID As System.String, _
   ByVal SelParams As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim SelID As System.String
Dim SelParams As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean
 
value = instance.DeSelectByID(SelID, SelParams, X, Y, Z)
```

```

System.bool DeSelectByID( 
   System.string SelID,
   System.string SelParams,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.bool DeSelectByID( 
   System.String^ SelID,
   System.String^ SelParams,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*SelID*
:   ID of object

*SelParams*
:   Type name of object (uppercase)

*X*
:   X selection location

*Y*
:   Z selection location

*Z*
:   Z selection location

#### Return Value

True if object is deselected, false otherwise

Remarks

See [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) for more information about selections.

Example

[Rotate, Scale, and Copy Sketch (C#)](Rotate_Scale_Copy_Sketch_Example_CSharp.htm)  
[Rotate, Scale, and Copy Sketch (VB.NET)](Rotate_Scale_Copy_Sketch_Example_VBNET.htm)  
[Rotate, Scale, and Copy Sketch (VBA)](Rotate_Scale_Copy_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
