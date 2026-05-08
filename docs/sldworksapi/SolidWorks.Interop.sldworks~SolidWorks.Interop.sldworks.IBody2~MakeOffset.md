# MakeOffset Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MakeOffset`

Creates a new temporary body by offsetting the selected surface body by the specified distance and in the specified direction.
Creates a new temporary body by offsetting the selected surface body by the specified distance and in the specified direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeOffset( _
   ByVal Distance As System.Double, _
   ByVal Direction As System.Boolean _
) As Body2
```

```

Dim instance As IBody2
Dim Distance As System.Double
Dim Direction As System.Boolean
Dim value As Body2
 
value = instance.MakeOffset(Distance, Direction)
```

```

Body2 MakeOffset( 
   System.double Distance,
   System.bool Direction
)
```

```

Body2^ MakeOffset( 
   System.double Distance,
   System.bool Direction
) 
```

#### Parameters

*Distance*
:   Distance by which to offset the selected surface body

*Direction*
:   True to offset the selected surface body in the opposite direction, false to offset  
    the surface body along the normal

#### Return Value

Pointer to the newly created [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

This method only supports surface bodies.

Example

[Create Temporary Bodies by Offsetting Surface Body (C#)](Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_CSharp.htm)  
[Create Temporary Bodies by Offsetting Surface Body (VB.NET)](Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_VBNET.htm)  
[Create Temporary Bodies By Offsetting a Surface Body (VBA)](Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
