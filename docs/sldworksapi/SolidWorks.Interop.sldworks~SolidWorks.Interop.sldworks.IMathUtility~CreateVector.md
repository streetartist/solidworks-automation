# CreateVector Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateVector`

Creates a math vector.
Creates a math vector.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateVector( _
   ByVal ArrayDataIn As System.Object _
) As System.Object
```

```

Dim instance As IMathUtility
Dim ArrayDataIn As System.Object
Dim value As System.Object
 
value = instance.CreateVector(ArrayDataIn)
```

```

System.object CreateVector( 
   System.object ArrayDataIn
)
```

```

System.Object^ CreateVector( 
   System.Object^ ArrayDataIn
) 
```

#### Parameters

*ArrayDataIn*
:   Array of doubles representing the x,y,z components of the vector

#### Return Value

Newly created [math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) or NULL if the operation fails

Example

[Create Temporary Extruded Body (VBA)](Create_Temporary_Extruded_Body_Example_VB.htm)  
[Get Angle of Hole Not Normal to a Face (VBA)](Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm)  
[Locate Apex of Conical Face (VBA)](Locate_Apex_of_Conical_Face_Example_VB.htm)  
[Create Drag Arrow Manipulator (C#)](Create_Drag_Arrow_Manipulator_Example_CSharp.htm)  
[Create Drag Arrow Manipulator (VB.NET)](Create_Drag_Arrow_Manipulator_Example_VBNET.htm)  
[Create Drag Arrow Manipulator (VBA)](Create_Drag_Arrow_Manipulator_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.md)  
[IMathUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.md)  
[IMathUtility::ICreateVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateVector.md)
